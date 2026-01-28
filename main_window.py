#Pyside6 - responsible for generrating the window and everything inside
#OpenCV - open source computer vision used to generate images and the webcame to use the device camera
#MediaPipe - the brain behind the glasses filter an AI library that detects where the face is and allows the filter to be placed on the user's face
#Run Window- python main.py

#use library functions sys.exit
import sys  
#import to acess webcam and image processing
import cv2

#import style classes (from generated main window file)
from gen.gen_main_window import Ui_Filter_Me
#import qt timer to create a timer for webcam frames
from PySide6.QtCore import QTimer
#import qt image(to comvert frames to qt) and pixmap(to set qtframes to qlabel) to show images in labels
from PySide6.QtGui import QImage, QPixmap
#import qt main window (class that creates the window)
from PySide6.QtWidgets import QMainWindow

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

        # Start the webcam (camera 0 is the default camera)
        self.cap = cv2.VideoCapture(0)

        #create a timer to update frames
        self.timer = QTimer()
        # When the timer finishes, run the update_frame function
        self.timer.timeout.connect(self.update_frame)
         # Update every 30 milliseconds
        self.timer.start(30) 
    
    def update_frame(self):
        # Get a new image from the webcam
        ret, frame = self.cap.read()
        if ret:
            # Change the image from BGR (used by OpenCV) to RGB (used by Qt)
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Get the height, width, and number of color channels of the image
            h, w, ch = rgb_image.shape
            # Calculate how many bytes are in one line of the image
            bytes_per_line = ch * w
            # Make a QImage from the image data so Qt can use it
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            # Make a QPixmap from the QImage so we can show it in a label
            pixmap = QPixmap.fromImage(qt_image)
            # Show the image in the label on the window (change 'video_label' to your label's name)
            self.ui.webcam_Display.setPixmap(pixmap)