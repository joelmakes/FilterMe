# apply image filters using OpenCV
import cv2
#import pixel manipulation library
import numpy as np

class Filters():
    def __init__(self):
        pass

    def apply_grayscale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def apply_sepia(self, frame):
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia_frame = cv2.transform(frame, kernel)