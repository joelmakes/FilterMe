import os
import sys

from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from main_window import FilterMe

Version = "1.0.0"
_INSTANCE_MUTEX = None


def resource_path(relative_path):
    base = getattr(sys, "_MEIPASS", os.path.abspath("."))
    return os.path.join(base, relative_path)


def focus_existing_window():
    """Restore and foreground the running Filter Me window on Windows."""
    if sys.platform != "win32":
        return

    import ctypes

    user32 = ctypes.WinDLL("user32", use_last_error=True)
    hwnd = user32.FindWindowW(None, "Filter Me")
    if hwnd:
        SW_RESTORE = 9
        user32.ShowWindow(hwnd, SW_RESTORE)
        user32.SetForegroundWindow(hwnd)


def acquire_single_instance_lock():
    """Allow only one running instance on Windows using a named mutex."""
    global _INSTANCE_MUTEX

    if sys.platform != "win32":
        return True

    import ctypes
    from ctypes import wintypes

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.CreateMutexW.argtypes = [
        wintypes.LPVOID,
        wintypes.BOOL,
        wintypes.LPCWSTR,
    ]
    kernel32.CreateMutexW.restype = wintypes.HANDLE

    mutex_name = "FilterMe.SingleInstance.1_0_0"
    mutex = kernel32.CreateMutexW(None, False, mutex_name)
    if not mutex:
        return False

    ERROR_ALREADY_EXISTS = 183
    if ctypes.get_last_error() == ERROR_ALREADY_EXISTS:
        focus_existing_window()
        kernel32.CloseHandle(mutex)
        return False

    _INSTANCE_MUTEX = mutex
    return True

if __name__ == "__main__":

    print("version:", Version)

    if not acquire_single_instance_lock():
        sys.exit(1)

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
