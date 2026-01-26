#display ONLY

#Pyside6 - responsible for generrating the window and everything inside
#OpenCV - open source computer vision used to generate images and the webcame to use the device camera
#MediaPipe - the brain behind the glasses filter an AI library that detects where the face is and allows the filter to be placed on the user's face
#Run Window- python main.py

# python/pyside = pep8
# Qt designer = C

#talk to desktop system
import sys
#import qt parts
from PySide6.QtWidgets import QApplication
# import the main window class that defines FilterMe from main_window.py
from main_window import FilterMe

#check if file is the main conducter
if __name__ == "__main__":
    # Create the application object
    app = QApplication(sys.argv)
    
    # Create and show your window
    window = FilterMe()
    window.show()
    
    # Start the event loop (this keeps the window open until user hits closes)
    sys.exit(app.exec())