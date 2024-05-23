import cv2
import numpy as np

def apply_effect(image, kernel_size, anchor, iterations, border_type, border_value):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    return cv2.erode(gray, kernel, anchor=(-1, -1), iterations=iterations, borderType=border_type, borderValue=border_value)
def get_filter_data():
    return {
        "parameters": {
            "kernel_size": {"min": 2, "max": 50, "init": 5, "interval": 1},
            "anchor": {"min": -1, "max": -1, "init": -1, "interval": 1},
            "iterations": {"min": 1, "max": 10, "init": 1, "interval": 1},
            "border_type": {"min": 0, "max": 4, "init": 0, "interval": 1},
            "border_value": {"min": 0, "max": 255, "init": 0, "interval": 1},
        }
    }