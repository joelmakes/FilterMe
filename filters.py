# apply image filters using OpenCV
import cv2

import numpy as np


class Filters():
    #set class constructor
    def __init__(self):
        pass
    
    #apply rio de janeiro filter function
    def apply_rio_de_janeiro(self, frame):
        # Step 1: Brightness & Contrast
        frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=10)

        # Step 2: Create gradient overlay
        height, width = frame.shape[:2]
        top_color = np.array([128, 0, 128], dtype=np.uint8)   # Purple (BGR)
        bottom_color = np.array([203, 192, 255], dtype=np.uint8) # Pink (BGR)
        gradient = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            ratio = y / height
            color = (1 - ratio) * top_color + ratio * bottom_color
            gradient[y, :] = color

        # Step 3: Linear blending
        blended = cv2.addWeighted(frame, 0.7, gradient, 0.3, 0)

        return blended
    
    #Use opencv pencilSketch for sketch effect from openccv contrib module
    def apply_sketch(self, frame):
           # pencilSketch returns two images: grayscale and color
           dst_gray, dst_color = cv2.pencilSketch(
               frame, sigma_s=3, sigma_r=0.11, shade_factor=0.09
           )
           # Return the grayscale sketch as a 3-channel image for consistency
           return cv2.cvtColor(dst_gray, cv2.COLOR_GRAY2BGR)
    
    # def apply_sketch(self, frame):
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     blur = cv2.medianBlur(gray, 5)
    #     sketch = cv2.adaptiveThreshold(
    #         blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
    #         cv2.THRESH_BINARY, 9, 9
    #     )
    #     return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)