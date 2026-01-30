# apply image filters using OpenCV
import cv2
#import pixel manipulation library
import numpy as np

class Filters():
    #set class constructor
    def __init__(self):
        pass

    #set grayscale filter function
    def apply_grayscale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #set sepia filter function by applying a color transformation matrix (edits pixel colors to set RGB values)
    def apply_sepia(self, frame):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia_frame = cv2.transform(frame, kernel)
        return sepia_frame