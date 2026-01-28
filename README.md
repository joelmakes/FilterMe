# FilterMe - Real-time Webcam Filters

FilterMe is a PySide6 desktop app that applies real-time filters to your webcam using OpenCV and MediaPipe. It provides a simple Qt-based UI for launching and controlling the filter experience.

## Requirements
- Python 3.12 (tested on 3.12.10)
- Windows (tested), webcam device

## Setup
1. Clone the repository:
	```bash
	git clone <repository-url>
	cd FilterMe
	```

2. Create and activate a virtual environment:
	```bash
	python -m venv venv
	.\venv\Scripts\activate
	```

3. Install dependencies:
	```bash
	pip install -r requirements.txt
	```

## Run
Start the app:
```bash
python App.py
```

## Tech Stack
- PySide6 6.10.1 — Qt GUI and UI loading
- OpenCV 4.13.0.90 — Webcam capture and image processing
- MediaPipe 0.10.31 — Face/landmark detection for filter placement

## Development Notes
- UI file: `mainwindow.ui` (Qt Designer). The app loads this UI at runtime.
- Optional: regenerate a Python class from the UI using `pyside6-uic`:
  ```bash
  pyside6-uic mainwindow.ui -o gen\gen_mainwindow.py
  ```
- Entry point: `App.py` which initializes `QApplication` and shows the `FilterMe` window defined in `main_window.py`.

## Troubleshooting
- Ensure the virtual environment is activated before installing or running.
- If the UI fails to load, verify `mainwindow.ui` exists at the project root or update the path in `main_window.py`.
- For webcam issues, confirm another app isn’t using the camera and that OpenCV can access it.

## License
See LICENSE for details.