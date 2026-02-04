
# FilterMe - Real-time Webcam Filters

FilterMe is a PySide6 desktop app that applies real-time filters to your webcam using OpenCV. It features a modern Qt-based UI for launching, previewing, and saving filtered webcam images.

## Requirements
- Python 3.12 (tested on 3.12.10)
- Windows (tested), webcam device
- All dependencies in requirements.txt:
  - PySide6==6.10.1
  - opencv-contrib-python==4.13.0.90

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

## Features
- Real-time webcam feed with filter preview
- Two built-in filters: "Rio De Janeiro" (color gradient + text) and "Sketch" (pencil sketch effect)
- Save filtered images to user-selectable locations (FilterMe Pictures, Pictures, Documents, Desktop, or custom long path)
- Username input for personalized filenames
- Modern, responsive UI built with Qt Designer

## Tech Stack
- PySide6 6.10.1 — Qt GUI and UI loading
- OpenCV 4.13.0.90 — Webcam capture and image processing

## Development Notes
- UI file: `Form/main_window.ui` (edit in Qt Designer)
- Generated Python UI: `gen/gen_main_window.py` (regenerate with `pyside6-uic Form/main_window.ui -o gen/gen_main_window.py`)
- Main logic: `main_window.py` (FilterMe class)
- Entry point: `App.py` (starts the application)
- Filters: `filters.py` (Rio De Janeiro and Sketch)

## Troubleshooting
- Ensure the virtual environment is activated before installing or running.
- If the UI fails to load, verify `Form/main_window.ui` exists or regenerate `gen/gen_main_window.py`.
- For webcam issues, confirm another app isn’t using the camera and that OpenCV can access it.

## License
See LICENSE for details.