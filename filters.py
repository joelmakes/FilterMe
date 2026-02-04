import numpy as np

import cv2


class Filters():
    def __init__(self):
        pass

    def apply_rio_de_janeiro(self, frame):
        frame = cv2.convertScaleAbs(frame, alpha=.8, beta=25)

        height, width = frame.shape[:2]

        top_color = np.array([128, 0, 128], dtype=np.uint8)
        bottom_color = np.array([203, 192, 255], dtype=np.uint8)
        gradient = np.zeros((height, width, 3), dtype=np.uint8)

        # Fill each row of the gradient with a color
        # that is a mix between purple and pink
        for y in range(height):
            ratio = y / height
            color = (1 - ratio) * top_color + ratio * bottom_color
            gradient[y, :] = color

        blended = cv2.addWeighted(frame, 0.7, gradient, 0.3, 0)

        text = "Rio De Janeiro"
        position = (200, 300)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255, 255, 255)
        thickness = 1

        # This function draws the text onto the image at the given position
        cv2.putText(
            blended, text, position, font, font_scale, color,
            thickness, cv2.LINE_AA
        )

        return blended

    def apply_sketch(self, frame):
        dst_gray, dst_color = cv2.pencilSketch(
            frame, sigma_s=3, sigma_r=0.11, shade_factor=0.09
        )
        return cv2.cvtColor(dst_gray, cv2.COLOR_GRAY2BGR)
