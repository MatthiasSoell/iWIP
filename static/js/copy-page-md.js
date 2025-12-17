// static/js/copy-page-md.js
// Kopiert Seiten-Markdown + (optional) OER-Metadaten.
// Normalisiert HTML-Reste (style/ul/li/details) und macht relative Links/Bilder absolut.
// Feedback: Badge am Button.

document.addEventListener("DOMContentLoaded", function () {
  const btn = document.getElementById("md-copy-btn");
  if (!btn) return;

  // Badge
  const badge = document.createElement("span");
  badge.textContent = "✓";
  badge.setAttribute("aria-hidden", "true");
  Object.assign(badge.style, {
    position: "absolute",
    top: "-6px",
    right: "-6px",
    minWidth: "18px",
    height: "18px",
    lineHeight: "18px",
    textAlign: "center",
    borderRadius: "999px",
    fontSize: "12px",
    fontWeight: "700",
    border: "1px solid var(--border)",
    background: "var(--primary)",
    color: "var(--theme)",
    boxShadow: "0 2px 6px rgba(0,0,0,.15)",
    opacity: "0",
    transform: "scale(.85)",
    transition: "opacity .12s ease, transform .12s ease",
    pointerEvents: "none",
  });

  const cs = getComputedStyle(btn);
  if (cs.position === "static") btn.style.position = "relative";
  btn.appendChild(badge);

  let busy = false;

  btn.addEventListener("click", async function () {
    if (busy) return;
    busy = true;

    const rawNode = document.getElementById("md-rawcontent");
    if (!rawNode) {
      busy = false;
      return;
    }

    // 1) Seiteninhalt
    let md = normalizeForCopy(rawNode.textContent || "");

    // 2) OER-Meta davor (wenn vorhanden)
    const meta = getOerMetaMarkdown();
    if (meta) md = meta + "\n\n" + md;

    const ok = await copyText(md);
    if (ok) flashBadge();

    setTimeout(() => (busy = false), 350);
  });

  async function copyText(text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch (e) {
      try {
        fallbackCopy(text);
        return true;
      } catch (e2) {
        return false;
      }
    }
  }

  function flashBadge() {
    badge.style.opacity = "1";
    badge.style.transform = "scale(1)";
    setTimeout(() => {
      badge.style.opacity = "0";
      badge.style.transform = "scale(.85)";
    }, 900);
  }

  function getOerMetaMarkdown() {
    const scripted = document.getElementById("md-oer-meta");
    if (scripted && (scripted.textContent || "").trim()) {
      return normalizeForCopy(scripted.textContent);
    }
    return "";
  }

  function normalizeForCopy(input) {
    let s = input;

    // Entities -> Zeichen
    s = decodeHTMLEntities(s);

    // ---- Shortcodes raus (auch escaped Varianten) ----
    s = s.replace(/\{\{<\s*\/?\s*oer-meta\s*\/?\s*>}}/g, "");
    s = s.replace(/\{\{\s*<\s*\/?\s*oer-meta\s*\/?\s*>\s*}}/g, ""); // falls anders formatiert
    s = s.replace(/\{\{&lt;\s*\/?\s*oer-meta\s*\/?\s*&gt;\s*}}/g, ""); // falls schon escaped im Text

    // Copy-Button entfernen (falls im Inhalt)
    s = s.replace(/<button[^>]*id="md-copy-btn"[^>]*>[\s\S]*?<\/button>\s*/g, "");

    // Print-/Export-HTML entfernen
    s = s.replace(/<div class="top-toggle">[\s\S]*?<\/div>\s*/g, "");

    // Styles komplett entfernen
    s = s.replace(/<style[\s\S]*?<\/style>\s*/g, "");

    // Agenda-Wrapper entfernen (Inhalt bleibt)
    s = s.replace(/<div class="agenda">\s*/g, "");
    s = s.replace(/\s*<\/div>\s*/g, "\n");

    // <details>/<summary> in Markdown umwandeln (lesbar, ohne HTML)
    // summary als "🔽 ..." und Inhalt danach normal
    s = s.replace(
      /<details>\s*<summary>([\s\S]*?)<\/summary>\s*([\s\S]*?)<\/details>/g,
      (_, summary, body) => {
        const sum = stripHTML(summary).trim();
        const b = stripHTML(body).trim();
        return `\n\n> 🔽 ${sum}\n\n${b}\n\n`;
      }
    );

    // <ul><li>…</li></ul> in Markdown-Liste
    s = s.replace(/<ul[^>]*>/g, "\n");
    s = s.replace(/<\/ul>/g, "\n");
    s = s.replace(/<li[^>]*>/g, "- ");
    s = s.replace(/<\/li>/g, "\n");

    // Restliche simple HTML-Tags raus (em, strong, span, p, br, etc.)
    s = s.replace(/<br\s*\/?>/gi, "\n");
    s = s.replace(/<\/p>\s*<p>/gi, "\n\n");
    s = s.replace(/<\/?p[^>]*>/gi, "");
    s = s.replace(/<\/?span[^>]*>/gi, "");
    s = s.replace(/<\/?em>/gi, "*");
    s = s.replace(/<\/?strong>/gi, "**");
    s = s.replace(/<\/?div[^>]*>/gi, "\n");
    s = s.replace(/<\/?section[^>]*>/gi, "\n");

    // HTML-Links -> Markdown-Links (falls noch vorhanden)
    s = s.replace(
      /<a\s+[^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g,
      (_, href, text) => `[${stripHTML(text).replace(/\s+/g, " ").trim()}](${href})`
    );

    // Callout-Marker entfernen: [!TIPP] etc. (auch mit '>' davor)
    s = s.replace(/^\s*>?\s*\[![A-ZÄÖÜß_-]+\]\s*$/gim, "");

    // Leere „Inhalte“-Zeile optional glätten (dein Beispiel startet damit)
    s = s.replace(/^\s*-\s*Inhalte\s*\n+/i, "");

    // Relative Links/Bilder absolut machen (damit Notion etc. rendern kann)
    s = absolutizeMarkdownUrls(s);

    // Aufräumen
    s = s.replace(/\r\n/g, "\n");
    s = s.replace(/[ \t]+\n/g, "\n");
    s = s.replace(/\n{3,}/g, "\n\n").trim() + "\n";

    return s;
  }

  function absolutizeMarkdownUrls(text) {
    const origin = window.location.origin;
    const pageDir = window.location.href.replace(/[#?].*$/, "").replace(/\/[^/]*$/, "/");

    // markdown images: ![alt](url)
    text = text.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (m, alt, url) => {
      const fixed = makeAbsolute(url.trim(), origin, pageDir);
      return `![${alt}](${fixed})`;
    });

    // markdown links: [text](url)
    text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (m, label, url) => {
      const fixed = makeAbsolute(url.trim(), origin, pageDir);
      return `[${label}](${fixed})`;
    });

    return text;
  }

  function makeAbsolute(url, origin, pageDir) {
    // lassen: http(s), mailto, tel, #, data
    if (/^(https?:|mailto:|tel:|#|data:)/i.test(url)) return url;

    // schon absoluter Pfad
    if (url.startsWith("/")) return origin + url;

    // relative: an Seitenverzeichnis hängen
    return pageDir + url.replace(/^\.\//, "");
  }

  function stripHTML(html) {
    const t = document.createElement("div");
    t.innerHTML = html;
    return t.textContent || t.innerText || "";
  }

  function decodeHTMLEntities(str) {
    const t = document.createElement("textarea");
    t.innerHTML = str;
    return t.value;
  }

  function fallbackCopy(text) {
    const ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "absolute";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    document.execCommand("copy");
    document.body.removeChild(ta);
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.querySelector("[data-copy-citation]");
  const target = document.getElementById("oer-citation-text");

  if (!btn || !target) return;

  btn.addEventListener("click", () => {
    navigator.clipboard.writeText(target.innerText).then(() => {
      showCopyBadge("Zitiervorschlag kopiert");
    });
  });
});