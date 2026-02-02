# Pyside6 - responsible for generrating the window and everything inside
# OpenCV - generate images and the webcame to use the device camera
# OpenCV-Contrib - modules for OpenCV pencil sketch filter
# Run Window- python main.py

from pathlib import Path

import cv2
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel

from gen.gen_main_window import Ui_Filter_Me
from filters import Filters


class FilterMe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Filter_Me()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        self.setWindowTitle("FilterMe")

        self.filters = Filters()

        self.ui.button_rio.clicked.connect(self.apply_rio_de_janeiro)

        self.ui.button_sketch.clicked.connect(self.apply_sketch_filter)

        self.ui.button_reset.clicked.connect(self.reset_filter)

        self.ui.button_take_photo.clicked.connect(self.show_preview_page)

        self.ui.pushButton_save.clicked.connect(self.save_preview_image)

        self.ui.pushButton_delete.clicked.connect(self.delete_preview_image)

        self.cap = cv2.VideoCapture(0)

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_frame)

        self.timer.start(30)

        ret, frame = self.cap.read()
        if ret:
            h, w, _ = frame.shape
            if h > 0:
                # if height is greater than 0
                # set aspect ratio of current picture
                self.aspect_ratio = w / h
            else:
                # set default
                self.aspect_ratio = 16/9  # fallback
        else:
            # fall back if image couldnt be read set default ratio
            self.aspect_ratio = 16/9

    def apply_rio_de_janeiro(self):
        self.current_filter = self.filters.apply_rio_de_janeiro

    def apply_sketch_filter(self):
        self.current_filter = self.filters.apply_sketch

    def reset_filter(self):
        self.current_filter = None

    def update_frame(self):
        # Get a new image from the webcam
        ret, frame = self.cap.read()
        if ret:
            # Apply current filter if set
            if hasattr(self, 'current_filter') and self.current_filter:
                frame = self.current_filter(frame)

            # Convert the frame and Label size to QPixmap
            label_size = self.ui.QLabel_webcam_display.size()
            pixmap = self.frame_to_pixmap(frame, label_size)

            self.ui.QLabel_webcam_display.setPixmap(pixmap)

    # change opencv frame to qt pixmap
    def frame_to_pixmap(self, frame, size=None):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(
            rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888
        )
        pixmap = QPixmap.fromImage(qt_image)

        if size:
            # If a size is given, scale the pixmap
            # to fit while keeping the aspect ratio and smoothing the image
            pixmap = pixmap.scaled(
                size, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
        return pixmap  # Return the final pixmap to be displayed

    def show_preview_page(self):
        ret, frame = self.cap.read()

        if not ret:
            return

        # Apply current filter if set
        if hasattr(self, 'current_filter') and self.current_filter:
            frame = self.current_filter(frame)

        self.preview_frame = frame

        label_size = self.ui.QLabel_webcam_display_2.size()
        pixmap = self.frame_to_pixmap(frame, label_size)
        self.ui.QLabel_webcam_display_2.setPixmap(pixmap)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_prev)

    def save_preview_image(self):
        # Check if there is a preview frame to save
        if not hasattr(self, 'preview_frame'):
            return

        frame = self.preview_frame

        user_name = self.ui.QLineEdit_insert_username.text().strip()

        # If the user didn't enter a name, use a default name
        if not user_name:
            user_name = "FilterMe_Photo"

        # Make the filename safe:
        # only allow letters, numbers, spaces, underscores, and dashes
        safe_name = "".join(
            c for c in user_name
            if c.isalnum() or c in (' ', '_', '-')
        ).rstrip()
        filename = f"{safe_name}.png"

        pictures_dir = Path.home() / "Pictures"

        # If the Pictures folder doesn't exist, use the home folder instead
        if not pictures_dir.exists():
            pictures_dir = Path.home()

        save_path = pictures_dir / filename
        cv2.imwrite(str(save_path), frame)
        print(f"Saved picture to: {save_path}")

        self.ui.QLineEdit_insert_username.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

    def delete_preview_image(self):
        self.preview_frame = None
        self.ui.QLineEdit_insert_username.clear()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)


# Custom QLabel to maintain aspect ratio
class AspectRatioLabel(QLabel):
    def __init__(self, aspect_ratio=16/9, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aspect_ratio = aspect_ratio

    # This function is called whenever the label is resized
    def resizeEvent(self, event):
        w = self.width()
        h = int(w / self.aspect_ratio)

        # If the calculated height is too big, adjust width instead
        if h > self.height():
            h = self.height()
            w = int(h * self.aspect_ratio)

        super().resizeEvent(event)
