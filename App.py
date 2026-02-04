import sys

from PySide6.QtWidgets import QApplication

from main_window import FilterMe

Version = "1.0.0"

if __name__ == "__main__":

    print("version:", Version)

    app = QApplication(sys.argv)

    window = FilterMe()
    window.show()

    sys.exit(app.exec())
