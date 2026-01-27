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