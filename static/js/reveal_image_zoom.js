(() => {
  const init = () => {
    if (!document.querySelector('.reveal')) return;

    const zoomableImages = Array.from(document.querySelectorAll('.reveal img.zoomable'));
    if (zoomableImages.length === 0) return;

    const overlay = document.createElement('div');
    overlay.className = 'iwip_overlay iwip_overlay--image';
    overlay.hidden = true;
    overlay.setAttribute('aria-hidden', 'true');

    const panel = document.createElement('div');
    panel.className = 'iwip_overlay_panel';

    const imageWrap = document.createElement('div');
    imageWrap.className = 'iwip_reveal_image_wrap';

    const overlayImage = document.createElement('img');
    overlayImage.alt = '';

    imageWrap.appendChild(overlayImage);
    panel.appendChild(imageWrap);
    overlay.appendChild(panel);
    document.body.appendChild(overlay);

    const closeOverlay = () => {
      overlay.hidden = true;
      overlay.setAttribute('aria-hidden', 'true');
      overlayImage.removeAttribute('src');
    };

    const openOverlay = (img) => {
      overlayImage.src = img.currentSrc || img.src;
      overlayImage.alt = img.alt || '';
      overlay.hidden = false;
      overlay.setAttribute('aria-hidden', 'false');
    };

    zoomableImages.forEach((img) => {
      img.addEventListener('click', () => openOverlay(img));
    });

    overlay.addEventListener('click', closeOverlay);

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && !overlay.hidden) {
        closeOverlay();
      }
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();