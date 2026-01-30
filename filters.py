# apply image filters using OpenCV
import cv2
import numpy as np  # NumPy lets us easily create and work with arrays, which are like tables of numbers for images

class Filters():
    # This is the setup for the Filters class. It doesn't need to do anything special when starting.
    def __init__(self):
        pass

    # This function adds a "Rio de Janeiro" color effect to the image.
    def apply_rio_de_janeiro(self, frame):
        # Step 1: Make the image brighter and increase contrast so colors stand out more.
        frame = cv2.convertScaleAbs(frame, alpha=.8, beta=25)

        # Step 2: Make a gradient (smooth color change) from purple at the top to pink at the bottom.
        height, width = frame.shape[:2]  # Get the image size
        # These are the colors for the top and bottom of the gradient, written as BGR (Blue, Green, Red)
        top_color = np.array([128, 0, 128], dtype=np.uint8)   # Purple
        bottom_color = np.array([203, 192, 255], dtype=np.uint8) # Pink
        # Make a blank image (all zeros) the same size as the frame, to hold the gradient
        gradient = np.zeros((height, width, 3), dtype=np.uint8)
        # Fill each row of the gradient with a color that is a mix between purple and pink
        for y in range(height):
            ratio = y / height  # This goes from 0 at the top to 1 at the bottom
            color = (1 - ratio) * top_color + ratio * bottom_color  # Mix the two colors
            gradient[y, :] = color  # Set the whole row to this color

        # Step 3: Blend the original image and the gradient together.
        # 0.7 means the original image is stronger, 0.3 means the gradient is lighter.
        blended = cv2.addWeighted(frame, 0.7, gradient, 0.3, 0)

        # Add text label to the image
        text = "Rio De Janeiro"
        position = (200, 300)  # x, y coordinates
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255, 255, 255)  # White text in BGR
        thickness = 1
        cv2.putText(blended, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

        return blended

    # This function makes the image look like a pencil sketch.
    def apply_sketch(self, frame):
        # OpenCV's pencilSketch gives us two images: one in black and white, one in color.
        dst_gray, dst_color = cv2.pencilSketch(
            frame, sigma_s=3, sigma_r=0.11, shade_factor=0.09
        )
        # We use the black and white sketch, but change it to have 3 color channels so it works everywhere in our app.
        return cv2.cvtColor(dst_gray, cv2.COLOR_GRAY2BGR)