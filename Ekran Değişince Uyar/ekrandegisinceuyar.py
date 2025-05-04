#!/usr/bin/env python3
"""
Screen‑watch utility.

Continuously captures a secondary (left‑hand) 1080p monitor and looks for a
specific template image (e.g., a “Converting…” badge).  When the template can
no longer be found with ≥ 0.8 similarity, the script plays a WAV alert 30 times
and exits.

Tested on Windows 10/11 with winsound; no external audio libraries required.
"""

from pathlib import Path
import time
import winsound

import cv2
import mss
import numpy as np

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

TEMPLATE_PATH = Path("template.png")   # Grayscale PNG of the element to detect
SOUND_PATH    = Path("Beep.wav")       # WAV file to play as the alert
MATCH_THRESHOLD = 0.8                  # 0‒1, higher = stricter

# Capture region for the left‑hand 1080p monitor placed at x = −1920
MONITOR = {"left": -1920, "top": 0, "width": 1920, "height": 1080}

# --------------------------------------------------------------------------- #
# Initialise
# --------------------------------------------------------------------------- #

# Load template on startup
template = cv2.imread(str(TEMPLATE_PATH), cv2.IMREAD_GRAYSCALE)
if template is None:
    raise FileNotFoundError(f"Template not found: {TEMPLATE_PATH.resolve()}")

sct = mss.mss()
print("Watching screen…  (Ctrl‑C to abort)")

# --------------------------------------------------------------------------- #
# Main loop
# --------------------------------------------------------------------------- #

while True:
    # Capture screenshot and convert to grayscale
    frame = np.array(sct.grab(MONITOR))
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)

    # Template matching (normalised cross‑correlation)
    _, max_val, _, _ = cv2.minMaxLoc(
        cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    )
    print(f"Match score: {max_val:.3f}")

    # If template has vanished, trigger the alert
    if max_val < MATCH_THRESHOLD:
        print("Template disappeared → playing alert sound.")
        for _ in range(30):
            winsound.PlaySound(
                str(SOUND_PATH),
                winsound.SND_FILENAME | winsound.SND_NODEFAULT
            )
            time.sleep(0.1)  # short gap between beeps
        break

    time.sleep(5)  # check again after 5 s
