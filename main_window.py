#Todo in this file make a mainwindow class that will control all the logic. 
# TODO: Imports

#Pyside6 - responsible for generrating the window and everything inside
#OpenCV - open source computer vision used to generate images and the webcame to use the device camera
#MediaPipe - the brain behind the glasses filter an AI library that detects where the face is and allows the filter to be placed on the user's face
#Run Window- python main.py

#talk to desktop system
#import qt parts
from gen.gen_mainwindow import Ui_Filter_Me
from PySide6.QtWidgets import QMainWindow
#load up QT
from PySide6.QtUiTools import QUiLoader
#choose QT File
from PySide6.QtCore import QFile

#select main window to display
class FilterMe(QMainWindow):
    def __init__(self):
        super().__init__()
            
        # 2. Attach the UI to this class
        # This makes all your buttons and labels accessible via self.ui
        self.ui = Ui_Filter_Me()
        self.ui.setupUi(self)
        # 3. Final Window Setup - setting tab name
        self.setWindowTitle("FilterMe - Beta Edition")