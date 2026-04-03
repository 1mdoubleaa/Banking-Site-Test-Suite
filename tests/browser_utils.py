# browser_utils.py
# Detects and launches the first available browser on the machine.
# Priority: Chrome > Brave > Opera > Edge > Firefox
# Uses Selenium's built-in driver manager (Selenium 4.6+), no webdriver-manager needed.

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

BROWSER_PATHS = {
    "chrome": [
        "C:/Program Files/Google/Chrome/Application/chrome.exe",
        "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    ],
    "brave": [
        "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe",
        "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe",
    ],
    "opera": [
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Opera\opera.exe"),
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Opera GX\opera.exe"),
        "C:/Program Files/Opera/opera.exe",
    ],
    "edge": [
        "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
        "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    ],
    "firefox": [
        "C:/Program Files/Mozilla Firefox/firefox.exe",
        "C:/Program Files (x86)/Mozilla Firefox/firefox.exe",
    ],
}


def _find_binary(browser):
    """Return the first existing path for a browser, or None."""
    for path in BROWSER_PATHS[browser]:
        if os.path.exists(path):
            return path
    return None


def get_driver():
    """Return a WebDriver for the first installed browser found."""
    errors = []

    # Chrome — Selenium's built-in manager handles chromedriver automatically
    if _find_binary("chrome"):
        try:
            return webdriver.Chrome()
        except Exception as e:
            errors.append(f"Chrome: {e}")

    # Brave (Chromium-based — uses ChromeDriver with custom binary)
    brave_path = _find_binary("brave")
    if brave_path:
        try:
            options = ChromeOptions()
            options.binary_location = brave_path
            return webdriver.Chrome(options=options)
        except Exception as e:
            errors.append(f"Brave: {e}")

    # Opera (Chromium-based — uses ChromeDriver with custom binary)
    opera_path = _find_binary("opera")
    if opera_path:
        try:
            options = ChromeOptions()
            options.binary_location = opera_path
            return webdriver.Chrome(options=options)
        except Exception as e:
            errors.append(f"Opera: {e}")

    # Edge
    if _find_binary("edge"):
        try:
            return webdriver.Edge()
        except Exception as e:
            errors.append(f"Edge: {e}")

    # Firefox
    if _find_binary("firefox"):
        try:
            return webdriver.Firefox()
        except Exception as e:
            errors.append(f"Firefox: {e}")

    error_details = "\n  ".join(errors) if errors else "No browser binaries found."
    raise RuntimeError(
        f"Could not launch any browser. Details:\n  {error_details}"
    )
