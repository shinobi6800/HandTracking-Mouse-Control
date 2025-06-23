# 🖐️ Hand Tracking Mouse Control with Python
#🐭

Control your mouse using your **index finger** in front of a webcam using Python, OpenCV, and MediaPipe.

---

## 📸 What It Does

- 🧠 Tracks your hand in real-time via webcam
- ☝️ Detects your **index finger tip**
- 🖱️ Moves your mouse cursor to follow your finger
- 🧪 Easily extendable to recognize gestures (clicks, scrolls, etc.)

---

## 💡 Features

- ⚡ Fast and responsive hand tracking
- 📦 Easy setup with `venv` + `pip`
- 🪟 Works on **X11**, **XWayland**, or with `ydotool` on Wayland
- 🧩 Modular and customizable code

---

## 🧰 Requirements

### 🐧 Linux (Arch / Hyprland / Wayland) Specific

- ✅ Python 3.10+ (recommended: use [`pyenv`](https://github.com/pyenv/pyenv))
- ✅ Webcam
- ✅ `XWayland` or Wayland with [`ydotool`](https://github.com/ReimuNotMoe/ydotool)

### 📦 Python Dependencies

```bash
pip install opencv-python mediapipe pyautogui
