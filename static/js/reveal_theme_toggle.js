(() => {
  const STORAGE_KEY = 'iwip_reveal_theme';
  const DARK_CLASS = 'reveal-dark';
  const BUTTON_SELECTOR = '.reveal-theme-toggle';
  const ICON_SELECTOR = '[data-reveal-theme-icon]';
  const ICONS = {
    light: '🌙',
    dark: '☀️'
  };
  const LABELS = {
    light: 'Dunklen Kontrastmodus aktivieren',
    dark: 'Hellen Standardmodus aktivieren'
  };

  const getStorage = () => {
    try {
      return window.localStorage;
    } catch (error) {
      return null;
    }
  };

  const storage = getStorage();

  const readTheme = () => {
    if (!storage) {
      return 'light';
    }

    try {
      return storage.getItem(STORAGE_KEY) === 'dark' ? 'dark' : 'light';
    } catch (error) {
      return 'light';
    }
  };

  const writeTheme = (theme) => {
    if (!storage) {
      return;
    }

    try {
      storage.setItem(STORAGE_KEY, theme);
    } catch (error) {
      // Ignore storage failures and keep the session-local toggle working.
    }
  };

  const updateButtons = (theme) => {
    const isDark = theme === 'dark';

    document.querySelectorAll(BUTTON_SELECTOR).forEach((button) => {
      button.setAttribute('aria-pressed', String(isDark));
      button.setAttribute('aria-label', LABELS[theme]);
      button.setAttribute('title', LABELS[theme]);

      const icon = button.querySelector(ICON_SELECTOR);

      if (icon) {
        icon.textContent = ICONS[theme];
      }
    });
  };

  const applyTheme = (theme) => {
    document.body.classList.toggle(DARK_CLASS, theme === 'dark');
    updateButtons(theme);
  };

  const init = () => {
    if (!document.querySelector('.reveal')) {
      return;
    }

    const buttons = Array.from(document.querySelectorAll(BUTTON_SELECTOR));

    if (buttons.length === 0) {
      return;
    }

    let currentTheme = readTheme();
    applyTheme(currentTheme);

    buttons.forEach((button) => {
      button.addEventListener('click', () => {
        currentTheme = document.body.classList.contains(DARK_CLASS) ? 'light' : 'dark';
        applyTheme(currentTheme);
        writeTheme(currentTheme);
      });
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();