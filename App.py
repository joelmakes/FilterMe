import os
import sys

from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from main_window import FilterMe

Version = "1.0.0"


def resource_path(relative_path):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, relative_path)

if __name__ == "__main__":

    print("version:", Version)

    if sys.platform == "win32":
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("FilterMe.App.1.0.0")

    app = QApplication(sys.argv)

    # Show splash
    splash = QSplashScreen(QPixmap(resource_path("assets/splash.png")))
    splash.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
    splash.show()
    app.processEvents()

    # Startup work (this is where FilterMe opens the camera, etc.)
    window = FilterMe()

    splash.finish(window)
    window.show()

    sys.exit(app.exec())
