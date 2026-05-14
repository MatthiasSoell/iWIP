(() => {
  const STORAGE_KEY = 'iwip_content_emoji_visibility';
  const HIDE_CLASS = 'hide-content-emojis';
  const TOGGLE_SELECTOR = '[data-content-emoji-toggle]';
  const ICON_SELECTOR = '[data-content-emoji-toggle-icon]';

  const STATE = {
    visible: {
      icon: '⚪',
      actionLabel: 'Emojis ausblenden'
    },
    hidden: {
      icon: '😄',
      actionLabel: 'Emojis anzeigen'
    }
  };

  const getStorage = () => {
    try {
      return window.localStorage;
    } catch (error) {
      return null;
    }
  };

  const storage = getStorage();

  const readVisibility = () => {
    if (!storage) {
      return 'visible';
    }

    try {
      return storage.getItem(STORAGE_KEY) === 'hidden' ? 'hidden' : 'visible';
    } catch (error) {
      return 'visible';
    }
  };

  const writeVisibility = (visibility) => {
    if (!storage) {
      return;
    }

    try {
      storage.setItem(STORAGE_KEY, visibility);
    } catch (error) {
      // Ignore storage failures and keep the session-local toggle working.
    }
  };

  const updateButtons = (visibility) => {
    const state = STATE[visibility];
    const isHidden = visibility === 'hidden';

    document.querySelectorAll(TOGGLE_SELECTOR).forEach((button) => {
      button.setAttribute('aria-pressed', String(isHidden));
      button.setAttribute('aria-label', state.actionLabel);
      button.setAttribute('title', state.actionLabel);

      const icon = button.querySelector(ICON_SELECTOR);

      if (icon) {
        icon.textContent = state.icon;
      }
    });
  };

  const applyVisibility = (visibility) => {
    const isHidden = visibility === 'hidden';
    document.documentElement.classList.toggle(HIDE_CLASS, isHidden);
    document.body.classList.toggle(HIDE_CLASS, isHidden);
    updateButtons(visibility);
  };

  const buildBlogToggleButton = () => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'iwip_content_emoji_toggle';
    button.setAttribute('data-content-emoji-toggle', '');
    button.setAttribute('aria-pressed', 'false');
    button.setAttribute('aria-label', STATE.visible.actionLabel);
    button.setAttribute('title', STATE.visible.actionLabel);

    const icon = document.createElement('span');
    icon.className = 'iwip_content_emoji_toggle_icon';
    icon.setAttribute('data-content-emoji-toggle-icon', '');
    icon.setAttribute('aria-hidden', 'true');
    icon.textContent = STATE.visible.icon;

    button.appendChild(icon);
    return button;
  };

  const findPresentationButton = (topToggle) => {
    const buttons = Array.from(topToggle.querySelectorAll('button'));

    return buttons.find((button) => {
      const onclick = button.getAttribute('onclick') || '';
      const title = (button.getAttribute('title') || '').toLowerCase();
      const text = (button.textContent || '').trim();

      return (
        onclick.includes('/praesentation/') ||
        title.includes('pr\u00e4sentation') ||
        title.includes('praesentation') ||
        text.includes('🖥️')
      );
    });
  };

  const ensureBlogTopToggleButtons = () => {
    document.querySelectorAll('.top-toggle').forEach((topToggle) => {
      if (topToggle.querySelector(TOGGLE_SELECTOR)) {
        return;
      }

      const button = buildBlogToggleButton();
      const infoButton = topToggle.querySelector('.iwip_help_btn');
      const presentationButton = findPresentationButton(topToggle);

      if (presentationButton && presentationButton.parentElement === topToggle) {
        topToggle.insertBefore(button, presentationButton.nextSibling);
        return;
      }

      if (infoButton && infoButton.parentElement === topToggle) {
        topToggle.insertBefore(button, infoButton);
        return;
      }

      topToggle.appendChild(button);
    });
  };

  const registerToggleEvents = () => {
    document.querySelectorAll(TOGGLE_SELECTOR).forEach((button) => {
      if (button.dataset.contentEmojiToggleBound === 'true') {
        return;
      }

      button.dataset.contentEmojiToggleBound = 'true';
      button.addEventListener('click', () => {
        const isHidden = document.documentElement.classList.contains(HIDE_CLASS);
        const nextVisibility = isHidden ? 'visible' : 'hidden';
        applyVisibility(nextVisibility);
        writeVisibility(nextVisibility);
      });
    });
  };

  const init = () => {
    ensureBlogTopToggleButtons();
    registerToggleEvents();
    applyVisibility(readVisibility());
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
