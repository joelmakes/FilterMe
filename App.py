import sys

from PySide6.QtWidgets import QApplication

from main_window import FilterMe

Version = "1.0.0"

if __name__ == "__main__":

    print("version:", Version)

    if sys.platform == "win32":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("FilterMe.App.1.0.0")

    app = QApplication(sys.argv)

    window = FilterMe()
    window.show()

    sys.exit(app.exec())
