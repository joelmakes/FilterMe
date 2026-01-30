# apply image filters using OpenCV
import cv2

class Filters():
    #set class constructor
    def __init__(self):
        pass

    #set grayscale filter function
    def apply_grayscale(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    def apply_sketch(self, frame):
            # pencilSketch returns two images: grayscale and color
            dst_gray, dst_color = cv2.pencilSketch(
                frame, sigma_s=3, sigma_r=0.11, shade_factor=0.09
            )
            # Return the grayscale sketch as a 3-channel image for consistency
            return cv2.cvtColor(dst_gray, cv2.COLOR_GRAY2BGR)