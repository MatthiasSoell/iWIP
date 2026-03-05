(() => {
  const init = () => {
    const root = document.documentElement;
    const overlayById = new Map();

    const anyOpen = () => Array.from(overlayById.values()).some((el) => !el.hidden);

    const openOverlay = (overlay, triggerBtn) => {
      overlay.hidden = false;
      if (triggerBtn) {
        if (!triggerBtn.id) triggerBtn.id = `iwip_overlay_trigger_${Math.random().toString(16).slice(2)}`;
        overlay.dataset.triggerId = triggerBtn.id;
        triggerBtn.setAttribute('aria-expanded', 'true');
      }
      root.classList.add('iwip_no_scroll');
      const closeBtn = overlay.querySelector('[data-iwip-overlay-close], .iwip_help_close');
      if (closeBtn) closeBtn.focus();
    };

    const closeOverlay = (overlay) => {
      overlay.hidden = true;
      const triggerId = overlay.dataset.triggerId;
      if (triggerId) {
        const triggerBtn = document.getElementById(triggerId);
        if (triggerBtn) {
          triggerBtn.setAttribute('aria-expanded', 'false');
          triggerBtn.focus();
        }
      }
      if (!anyOpen()) root.classList.remove('iwip_no_scroll');
    };

    const registerOverlay = (overlay) => {
      if (!overlay || !overlay.id) return;
      if (overlayById.has(overlay.id)) return;

      // Overlay aus Reveal-Container lösen -> volle Viewport-Fläche
      if (overlay.parentElement !== document.body) {
        document.body.appendChild(overlay);
      }

      overlayById.set(overlay.id, overlay);

      overlay.addEventListener('click', (event) => {
        if (event.target === overlay) closeOverlay(overlay);
      });

      overlay
        .querySelectorAll('[data-iwip-overlay-close], .iwip_help_close')
        .forEach((btn) => btn.addEventListener('click', () => closeOverlay(overlay)));
    };

    document.querySelectorAll('[data-iwip-overlay]').forEach(registerOverlay);

    const helpOverlay = document.getElementById('iwip_help_overlay');
    if (helpOverlay) registerOverlay(helpOverlay);

    if (helpOverlay) {
      document.querySelectorAll('.iwip_help_btn, #iwip_help_trigger').forEach((triggerBtn) => {
        if (!triggerBtn.hasAttribute('data-iwip-overlay-target')) {
          triggerBtn.setAttribute('data-iwip-overlay-target', 'iwip_help_overlay');
        }
        if (!triggerBtn.hasAttribute('aria-controls')) {
          triggerBtn.setAttribute('aria-controls', 'iwip_help_overlay');
        }
        if (!triggerBtn.hasAttribute('aria-expanded')) {
          triggerBtn.setAttribute('aria-expanded', 'false');
        }
      });
    }

    document.querySelectorAll('[data-iwip-overlay-target]').forEach((triggerBtn) => {
      const targetId = triggerBtn.getAttribute('data-iwip-overlay-target');
      const overlay = overlayById.get(targetId);
      if (!overlay) return;
      triggerBtn.addEventListener('click', () => openOverlay(overlay, triggerBtn));
    });

    document.addEventListener('keydown', (event) => {
      if (event.key !== 'Escape') return;
      const open = Array.from(overlayById.values()).find((el) => !el.hidden);
      if (open) closeOverlay(open);
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();