// ------------------------------
// Manuelles Drucken (Blog & Reveal)
// ------------------------------
function triggerPrint() {
  window.print();
}

// ------------------------------
// Reveal-spezifischer Logik-Block (ohne Autoprint!)
// ------------------------------
// Hinweis:
// Kein automatisches Drucken mehr! Damit vermeiden wir Browser-Warnungen.
// Reveal bleibt davon unberührt – Drucken funktioniert über den Button.
document.addEventListener("DOMContentLoaded", function () {
  // Falls wir später reveal-spezifische Funktionen ergänzen wollen:
  if (typeof Reveal !== "undefined") {
    // Aktuell keine Autoprint-Funktion – bewusst leer.
  }
});