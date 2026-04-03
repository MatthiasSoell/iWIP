#!/usr/bin/env bash
# generate_blog_index.sh – Erzeugt eine Rohfassung der Blog-Wissensbasis
# aus den Frontmattern aller veröffentlichten Blogartikel.
#
# Nutzung:  ./scripts/generate_blog_index.sh > /tmp/blog_index_raw.md
# Danach:   Schlüsselkonzepte und Verweishaken in
#           ai_agents/blog_wissensbasis.md manuell kuratieren.

set -euo pipefail

BLOG_DIR="content/blog"
COUNTER=0

echo "# Blog-Wissensbasis – Rohfassung ($(date +%Y-%m-%d))"
echo ""
echo "Automatisch generiert. Schlüsselkonzepte und Verweishaken manuell ergänzen."
echo ""
echo "---"
echo ""

find "$BLOG_DIR" -name "index.md" -not -name ".index.md" -print0 | sort -z | while IFS= read -r -d '' file; do
    COUNTER=$((COUNTER + 1))

    # Titel extrahieren
    title=$(sed -n '/^---$/,/^---$/{ s/^title: *"\{0,1\}\([^"]*\)"\{0,1\}$/\1/p; }' "$file" | head -1)
    [ -z "$title" ] && title="[Titel fehlt]"

    # Bereich aus Pfad ableiten
    rel_path="${file#content/blog/}"
    bereich=$(echo "$rel_path" | cut -d'/' -f1)

    # Summary extrahieren (einzeilig)
    summary=$(sed -n '/^---$/,/^---$/{ s/^summary: *"\{0,1\}\([^"]*\)"\{0,1\}$/\1/p; }' "$file" | head -1)

    # H2-Überschriften als Kernthemen
    h2s=$(grep '^## ' "$file" | sed 's/^## //' | head -8)

    echo "## $COUNTER. $title"
    echo "- **Pfad**: content/blog/$rel_path"
    echo "- **Bereich**: $bereich"
    if [ -n "$summary" ]; then
        echo "- **Summary**: $summary"
    fi
    echo "- **H2-Kapitel**:"
    echo "$h2s" | while IFS= read -r h; do
        [ -n "$h" ] && echo "  - $h"
    done
    echo "- **Schlüsselkonzepte**: [TODO: manuell ergänzen]"
    echo "- **Verweishaken**: [TODO: manuell ergänzen]"
    echo ""
done
