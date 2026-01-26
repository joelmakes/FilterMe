#Todo in this file make a mainwindow class that will control all the logic. 
# TODO: Imports

#Pyside6 - responsible for generrating the window and everything inside
#OpenCV - open source computer vision used to generate images and the webcame to use the device camera
#MediaPipe - the brain behind the glasses filter an AI library that detects where the face is and allows the filter to be placed on the user's face
#Run Window- python main.py

#talk to desktop system
#import qt parts
from PySide6.QtWidgets import QMainWindow
#load up QT
from PySide6.QtUiTools import QUiLoader
#choose QT File
from PySide6.QtCore import QFile

#select main window to display
class FilterMe(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Load the UI file you created in Designer
        #TODO: Better way of loading this, can you import from gen folder? 
        loader = QUiLoader()
        ui_file = QFile("MainWindow.ui")
        
        #throw error if file could not be open "name could have been different"
        if not ui_file.open(QFile.ReadOnly):
            print(f"Error: Could not open {ui_file.fileName()}")
            return
            
        # 2. Attach the UI to this class
        # This makes all your buttons and labels accessible via self.ui
        self.ui = loader.load(ui_file, self)
        #close file after reading all qt elements to avoid clutter
        ui_file.close()

        # 3. Final Window Setup - setting tab name
        self.ui.setWindowTitle("FilterMe - Beta Edition")