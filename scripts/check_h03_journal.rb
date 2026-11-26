#!/usr/bin/env ruby
# Checks H03 file snapshots. The evaluator checks planning content separately.

require "date"
require "yaml"

class UnsupportedJournalLayout < StandardError; end

STATE_FIELDS = %w[planning_focus main_line commitments constraints open_item].freeze
EVENT_FIELDS = %w[id date type content rationale refers_to rejected_alternative dialogue_ref].freeze
EVENT_TYPES = %w[decision revision open resolved].freeze
SNAPSHOT_NAME = /\Asession_\d{3,}\.md\z/

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
  open_ids = []
  events.each do |event|
    id = format("J-%03d", ids.length + 1)
    type = event["type"]
    raise "Ungültige Historienfelder für #{id}" unless
      event["id"] == id && (event.keys - EVENT_FIELDS).empty? && EVENT_TYPES.include?(type)
    date = event["date"].to_s
    raise "Kein ISO-Datum für #{id}" unless date.match?(/\A\d{4}-\d{2}-\d{2}\z/) && Date.iso8601(date)
    text_fields = ["content"] + (%w[rationale rejected_alternative dialogue_ref] & event.keys)
    text_fields.each do |key|
      raise "Fehlender oder ungültiger Text in #{key} für #{id}" unless
        event[key].is_a?(String) && !event[key].strip.empty?
    end

    references = Array(event["refers_to"])
    raise "Nur frühere IDs sind als Referenz zulässig für #{id}" unless (references - ids).empty?
    raise "Fehlender Bezug auf einen früheren offenen Punkt für #{id}" if
      type == "resolved" && (references & open_ids).empty?

    ids << id
    open_ids << id if type == "open"
  end
  events
end

def archived_journals(directory)
  archive = File.join(directory, "journal_history")
  raise "Archivbeleg fehlt (leeres journal_history bei leerem Archiv)" unless File.directory?(archive)

  Dir.children(archive).grep(SNAPSHOT_NAME).to_h do |name|
    [name, File.binread(File.join(archive, name))]
  end
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
  event_ids = {}
  revision_predecessors = { "A6" => %w[A2 A3], "B3" => %w[A6] }
  { "A2" => "decision", "A3" => "decision", "A6" => "revision", "B3" => "revision" }.each do |turn, expected|
    checkpoint = turn
    events = journal_events(journals.fetch(turn))
    raise "Frühere Historie wurde geändert" unless events.first(history.length) == history

    added = events.drop(history.length).select { |event| event["type"] == expected }
    raise "Kein neuer #{expected}-Eintrag" if added.empty?
    if expected == "revision"
      added.each do |event|
        raise "Fehlender Revisionsbezug für #{event["id"]}" if Array(event["refers_to"]).empty?
      end
      references = added.flat_map { |event| Array(event["refers_to"]) }
      revision_predecessors.fetch(turn).each do |previous_turn|
        raise "Revisionsbezug auf #{previous_turn} fehlt" if (references & event_ids.fetch(previous_turn)).empty?
      end
    end

    event_ids[turn] = added.map { |event| event["id"] }
    history = events
  end

  checkpoint = "A6"
  baseline = archived_journals(File.join(ARGV.first, checkpoint))
  %w[B1 B2].each do |turn|
    checkpoint = turn
    raise "Sitzungsarchiv hat sich seit A6 geändert" unless
      archived_journals(File.join(ARGV.first, turn)) == baseline
  end

  checkpoint = "B3"
  archive = archived_journals(File.join(ARGV.first, checkpoint))
  unless baseline.all? { |name, bytes| archive[name] == bytes }
    raise "Bisherige Sitzungsarchive wurden verändert oder entfernt"
  end
  added = archive.keys - baseline.keys
  unless added.size == 1 && archive.fetch(added.first) == journals.fetch("A6").b
    raise "Erwartet genau einen neuen Sitzungs-Snapshot, bytegleich zu A6"
  end
rescue UnsupportedJournalLayout, Psych::SyntaxError, Psych::DisallowedClass => e
  warn "#{checkpoint}: Journalformat manuell prüfen (#{e.message})"
  exit 2
rescue SystemCallError, RuntimeError, ArgumentError => e
  abort "#{checkpoint}: #{e.message}"
end
puts "H03: Journalstruktur und Sitzungsarchiv geprüft. Journalinhalt, inhaltliche Referenzen und Dialog separat prüfen."
