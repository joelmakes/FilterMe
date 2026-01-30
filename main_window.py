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
        #set stacked widget to page 24 (main filter page) ERROR doesnt show page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_23)  # or the correct page object


        # set window title using self ( self = window UI)
        self.setWindowTitle("FilterMe - Beta Edition")

        #create a way to access filters class from filters.py
        self.filters = Filters()

        #once rio button is clicked, run apply_grayscale_filter function from filters.py
        self.ui.button_rio.clicked.connect(self.apply_grayscale_filter)
        #once sketch button is clicked, run apply_sketch_filter function from filters.py
        self.ui.button_sketch.clicked.connect(self.apply_sketch_filter)

        # Connect take photo button to show preview page
        self.ui.button_take_photo.clicked.connect(self.show_preview_page)

        # Connect save and delete buttons on preview page to functions
        self.ui.pushButton_save.clicked.connect(self.save_preview_image)
        self.ui.pushButton_delete.clicked.connect(self.delete_preview_image)

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
            #get height, width, from picture frame
            h, w, _ = frame.shape
            if h > 0:
                #if height is greater than 0, set aspect ratio of current picture
                self.aspect_ratio = w / h
            else:
                #set default ratio if height is zero or less than 
                self.aspect_ratio = 16/9  # fallback
        else:
            #fall back if image couldnt be read set default ratio
            self.aspect_ratio = 16/9  
    
    #apply grayscale filter function
    def apply_grayscale_filter(self):
        self.current_filter = self.filters.apply_grayscale
    #apply sketch filter function
    def apply_sketch_filter(self):
        self.current_filter = self.filters.apply_sketch

    def update_frame(self):
        # Get a new image from the webcam
        ret, frame = self.cap.read()
        if ret:
                # Apply current filter if set
            if hasattr(self, 'current_filter') and self.current_filter:
                frame = self.current_filter(frame)
                # Convert the frame and Qlabel size to QPixmap 
            pixmap = self.frame_to_pixmap(frame, self.ui.QLabel_webcam_display.size())
            # set the converted pixmap to display on the QLabel
            self.ui.QLabel_webcam_display.setPixmap(pixmap)

    #change opencv frame to qt pixmap (taking in picture frame, QLabel size on qt designer)
    def frame_to_pixmap(self, frame, size=None):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        if size:
            pixmap = pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pixmap


    def show_preview_page(self):
        # Get the current frame
        ret, frame = self.cap.read()
        if not ret:
            return  # Optionally show an error message

        # Apply current filter if set
        if hasattr(self, 'current_filter') and self.current_filter:
            frame = self.current_filter(frame)

        # Store the frame for saving
        self.preview_frame = frame

        # Show the frame in the preview QLabel
        pixmap = self.frame_to_pixmap(frame, self.ui.QLabel_webcam_display_2.size())
        self.ui.QLabel_webcam_display_2.setPixmap(pixmap)

        # Switch to the preview page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_24)

    def save_preview_image(self):
        if not hasattr(self, 'preview_frame'):
            return
        
        frame = self.preview_frame
        user_name = self.ui.QLineEdit_insert_username.text().strip()

        if not user_name:
            user_name = "FilterMe_Photo"

        safe_name = "".join(c for c in user_name if c.isalnum() or c in (' ', '_', '-')).rstrip()
        filename = f"{safe_name}.png"
        pictures_dir = Path.home() / "Pictures"

        if not pictures_dir.exists():
            pictures_dir = Path.home()

        save_path = pictures_dir / filename
        cv2.imwrite(str(save_path), frame)
        print(f"Saved picture to: {save_path}")
        
        # clear the username label before returnin to home page
        self.ui.QLineEdit_insert_username.clear()
        # Switch back to home/camera page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_23)

    def delete_preview_image(self):
        self.preview_frame = None
        # clear the username label before returnin to home page
        self.ui.QLineEdit_insert_username.clear()
        # Switch back to home/camera page
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_23)

  

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
