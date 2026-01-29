#Pyside6 - responsible for generrating the window and everything inside
#OpenCV - open source computer vision used to generate images and the webcame to use the device camera
#MediaPipe - the brain behind the glasses filter an AI library that detects where the face is and allows the filter to be placed on the user's face
#Run Window- python main.py

#import to acess webcam and image processing
import cv2
#manage file paths for pictures
from pathlib import Path

#import style classes (from generated main window file)
from gen.gen_main_window import Ui_Filter_Me
#import qt timer to create a timer for webcam frames
from PySide6.QtCore import QTimer, Qt
#import qt image(to comvert frames to qt) and pixmap(to set qtframes to qlabel) to show images in labels
from PySide6.QtGui import QImage, QPixmap
#import qt main window (class that creates the window)
from PySide6.QtWidgets import QMainWindow, QLabel
#import filter functionality from filters.py
from filters import Filters

#inherit from Qmaninwindow to customezie, and add functionality
class FilterMe(QMainWindow):

    #defnie the constructor as self
    def __init__(self):
        # Call the QmainWindow constructor
        super().__init__()
            
        # Store class ui to -> imported UI file from py file
        self.ui = Ui_Filter_Me()
        #setup the UI using self
        self.ui.setupUi(self)

        # set window title using self ( self = window UI)
        self.setWindowTitle("FilterMe - Beta Edition")

        #create a way to access filters class from filters.py
        self.filters = Filters()

        #once rio button is clicked, run apply_grayscale_filter function from filters.py
        self.ui.button_rio.clicked.connect(self.apply_grayscale_filter)
        #once sequoia button is clicked, run apply_sequoia_filter function from filters.py
        self.ui.button_sketch.clicked.connect(self.apply_sequoia_filter)

        self.ui.button_take_picture.clicked.connect(self.take_picture)

        # Start the webcam (camera 0 is the default camera)
        self.cap = cv2.VideoCapture(0)

        #create a timer to update frames
        self.timer = QTimer()
        # When the timer finishes, run the update_frame function
        self.timer.timeout.connect(self.update_frame)
        # Update every 30 milliseconds (about 33fps)
        self.timer.start(30)

        # Get camera aspect ratio
        ret, frame = self.cap.read()
        if ret:
            h, w, _ = frame.shape
            if h > 0:
                self.aspect_ratio = w / h
            else:
                self.aspect_ratio = 16/9  # fallback
        else:
            self.aspect_ratio = 16/9  # fallback
    
      #apply grayscale filter function
    def apply_grayscale_filter(self):
        self.current_filter = self.filters.apply_grayscale

    def apply_sequoia_filter(self):
        self.current_filter = self.filters.apply_sepia

    def update_frame(self):
        # Get a new image from the webcam
        ret, frame = self.cap.read()
        if ret:
                # Apply current filter if set
            if hasattr(self, 'current_filter') and self.current_filter:
                frame = self.current_filter(frame)
            # Convert BGR to RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qt_image)
            # Scale pixmap to fit label while keeping aspect ratio
            scaled_pixmap = pixmap.scaled(self.ui.QLabel_webcam_display.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ui.QLabel_webcam_display.setPixmap(scaled_pixmap)
    
    def take_picture(self):
    # Get the current frame
        ret, frame = self.cap.read()
        if not ret:
            return  # Optionally show an error message

        # Get the user name from the text input
        user_name = self.ui.lineEdit_user_name.text().strip()
        if not user_name:
            user_name = "user"

        # Sanitize filename
        safe_name = "".join(c for c in user_name if c.isalnum() or c in (' ', '_', '-')).rstrip()
        filename = f"{safe_name}.png"

        # Get Pictures directory or fallback to home
        pictures_dir = Path.home() / "Pictures"
        if not pictures_dir.exists():
            pictures_dir = Path.home()
        save_path = pictures_dir / filename

        # Save the image
        cv2.imwrite(str(save_path), frame)

        # Optionally, show a message or open the folder
        print(f"Saved picture to: {save_path}")

  

# Custom QLabel to maintain aspect ratio
class AspectRatioLabel(QLabel):
    def __init__(self, aspect_ratio=16/9, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aspect_ratio = aspect_ratio

    def resizeEvent(self, event):
        w = self.width()
        h = int(w / self.aspect_ratio)
        if h > self.height():
            h = self.height()
            w = int(h * self.aspect_ratio)
        super().resizeEvent(event)
