# 2B 1S  🍦🎵

**2B 1S** is a lightweight, responsive desktop audio player built using Python, Tkinter, and Pygame. It features a fully customized, ultra-smooth background rendering system that tracks window resizing instantly without native OS event lag.

## ✨ Features
* **Zero-Lag UI Scaling:** Bypasses standard OS window loop limitations to provide true real-time background image updating while stretching or dragging the window frame.
* **Dual-Stage Image Rendering:** Dynamically trades off between performance-friendly bilinear scaling during adjustments and high-quality Lanczos antialiasing once sizing completes.
* **Non-Blocking Audio Engine:** Powered by the Pygame mixer module to ensure independent sound stream controls that never freeze the user interface.
* **High Contrast Overlays:** Designed with an integrated geometric interface plate to guarantee accessibility and button readability over any background image assets.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3 and the required media processing libraries installed:
```bash
pip install pygame pillow
```

### Required Assets
Place the following files in the root folder of your project script:
* `choclate ice scerma.jpg` — Your default application background graphic.
* `Lovers Theme.mp3` — The application's default audio track file.

### Execution
Run the script directly via your terminal:
```bash
python main.py
```

## 🛠️ How It Works
Standard Tkinter windows freeze up background image scaling when a user holds down their cursor on a window border. **2B 1S** circumvents this by initiating an asynchronous 15ms task polling loop using `root.after()`. This enforces strict layout calculations and active display repaints (`root.update_idletasks()`) to maintain a seamless user experience.

