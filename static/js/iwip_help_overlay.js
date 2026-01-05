/* iwip_help_overlay.js
   Steuert das UI-Hilfe-Overlay (öffnen/schließen, Fokus, ESC)
*/

(() => {
  const overlay = document.getElementById('iwip_help_overlay');
  if (!overlay) return;

  const close_btn = overlay.querySelector('.iwip_help_close');

  const open_overlay = (trigger_btn) => {
    overlay.hidden = false;
    trigger_btn.setAttribute('aria-expanded', 'true');

    // Trigger merken, um Fokus korrekt zurückzugeben
    if (!trigger_btn.id) {
      trigger_btn.id = 'iwip_help_trigger_' + Math.random().toString(16).slice(2);
    }
    overlay.dataset.trigger_id = trigger_btn.id;

    document.documentElement.classList.add('iwip_no_scroll');
    close_btn?.focus();
  };

  const close_overlay = () => {
    overlay.hidden = true;
    document.documentElement.classList.remove('iwip_no_scroll');

    const trigger_id = overlay.dataset.trigger_id;
    if (trigger_id) {
      const trigger_btn = document.getElementById(trigger_id);
      trigger_btn?.setAttribute('aria-expanded', 'false');
      trigger_btn?.focus();
    }
  };

  // Öffnen per Klick auf Help-Button
  document.addEventListener('click', (e) => {
    const help_btn = e.target.closest('.iwip_help_btn');
    if (help_btn) {
      open_overlay(help_btn);
      return;
    }

    // Klick auf Overlay-Hintergrund schließt
    if (e.target === overlay) {
      close_overlay();
    }
  });

  // Schließen per Close-Button
  close_btn?.addEventListener('click', close_overlay);

  // Schließen per ESC
  document.addEventListener('keydown', (e) => {
    if (!overlay.hidden && e.key === 'Escape') {
      close_overlay();
    }
  });
})();