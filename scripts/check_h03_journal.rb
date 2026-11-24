#!/usr/bin/env ruby
# Checks H03 file snapshots. The evaluator checks planning content separately.

require "date"
require "yaml"

class UnsupportedJournalLayout < StandardError; end

STATE_FIELDS = %w[planning_focus main_line commitments constraints open_item].freeze
EVENT_FIELDS = %w[id date type content rationale refers_to rejected_alternative].freeze
EVENT_TYPES = %w[decision revision open resolved].freeze

def read_yaml(text)
  fenced = text.match(/\A\s*```ya?ml[ \t]*\r?\n(.*?)^```[ \t]*\s*\z/m)
  YAML.safe_load(fenced ? fenced[1] : text, permitted_classes: [Date])
end

def journal_events(text)
  sections = text.match(/^\#{1,2} Current State[ \t]*\r?\n(.*?)^\#{1,2} Decision History[ \t]*\r?\n(.*)\z/m)
  raise UnsupportedJournalLayout, "Erwartet Current State und Decision History" unless sections

  state = read_yaml(sections[1])
  raise UnsupportedJournalLayout, "Current State ist keine YAML-Zuordnung" unless state.is_a?(Hash)
  raise "Current State braucht genau die fünf vorgesehenen Felder" unless
    state.length == STATE_FIELDS.length && (state.keys - STATE_FIELDS).empty?

  history = sections[2]
  entries = history.scan(/^\#{2,4} (J-\d+)[ \t]*\r?\n(.*?)(?=^\#{2,4} J-\d+[ \t]*\r?\n|\z)/m)
  events = if entries.empty?
             read_yaml(history)
           else
             entries.map do |id, body|
               fields = read_yaml(body)
               raise UnsupportedJournalLayout, "Kein YAML-Eintrag für #{id}" unless fields.is_a?(Hash)
               raise "Abweichende ID in #{id}" if fields.key?("id") && fields["id"] != id

               fields.merge("id" => id)
             end
           end
  unless events.is_a?(Array) && events.all? { |event| event.is_a?(Hash) }
    raise UnsupportedJournalLayout, "Decision History ist keine unterstützte YAML-Liste"
  end

  ids = []
  events.each do |event|
    id = format("J-%03d", ids.length + 1)
    type = event["type"]
    raise "Ungültige Historienfelder für #{id}" unless
      event["id"] == id && (event.keys - EVENT_FIELDS).empty? && EVENT_TYPES.include?(type)
    date = event["date"].to_s
    raise "Kein ISO-Datum für #{id}" unless date.match?(/\A\d{4}-\d{2}-\d{2}\z/) && Date.iso8601(date)
    required = %w[decision revision].include?(type) ? %w[content rationale] : %w[content]
    raise "Fehlender Text für #{id}" unless required.all? { |key| event[key].is_a?(String) && !event[key].strip.empty? }

    references = Array(event["refers_to"])
    raise "Nur frühere IDs sind als Referenz zulässig für #{id}" unless (references - ids).empty?
    raise "Fehlender Revisions- oder Erledigungsbezug für #{id}" if
      %w[revision resolved].include?(type) && references.empty?

    ids << id
  end
  events
end

abort "Aufruf: ruby scripts/check_h03_journal.rb SNAPSHOT-ORDNER" unless ARGV.length == 1

checkpoints = %w[A1 A2 A3 A4 A5 A6 B1 B2 B3]
journals = {}
checkpoint = nil
begin
  checkpoints.each do |turn|
    checkpoint = turn
    directory = File.join(ARGV.first, turn)
    raise "Snapshot-Verzeichnis fehlt" unless File.directory?(directory)
    raise "Unerwarteter freigegebener Übergabestand" if File.exist?(File.join(directory, "planning_state.md"))

    path = File.join(directory, "planning_journal.md")
    journals[turn] = File.binread(path).force_encoding("UTF-8") if File.file?(path)
    raise "Unerwartete Journaldifferenz zur Soll-Existenz" unless journals.key?(turn) == (turn != "A1")
  end

  { "A4" => "A3", "A5" => "A3", "B1" => "A6", "B2" => "A6" }.each do |turn, baseline|
    checkpoint = turn
    raise "Journal ist nicht bytegleich zu #{baseline}" unless journals[turn] == journals[baseline]
  end

  history = []
  prior_decisions = []
  { "A2" => "decision", "A3" => "decision", "A6" => "revision", "B3" => "revision" }.each do |turn, expected|
    checkpoint = turn
    events = journal_events(journals.fetch(turn))
    raise "Frühere Historie wurde geändert" unless events.first(history.length) == history

    added = events.drop(history.length).select { |event| event["type"] == expected }
    raise "Kein neuer #{expected}-Eintrag" if added.empty?
    if expected == "revision" && added.none? { |event| (Array(event["refers_to"]) & prior_decisions).any? }
      raise "Revision verweist nicht auf einen einschlägigen früheren Eintrag"
    end

    ids = added.map { |event| event["id"] }
    prior_decisions = expected == "revision" ? ids : prior_decisions + ids
    history = events
  end
rescue UnsupportedJournalLayout, Psych::SyntaxError, Psych::DisallowedClass => e
  warn "#{checkpoint}: Journalformat manuell prüfen (#{e.message})"
  exit 2
rescue SystemCallError, RuntimeError, ArgumentError => e
  abort "#{checkpoint}: #{e.message}"
end
puts "H03: Technische Teilprüfungen bestanden. Journalinhalt, inhaltliche Referenzen und Dialog separat prüfen."
