import cv2
import numpy as np

def apply_effect(image, kernel_size):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilated = cv2.dilate(gray, kernel, iterations=1)

    return cv2.cvtColor(dilated, cv2.COLOR_GRAY2BGR)

def get_filter_data():
    return {
        "parameters": {
            "kernel_size": {"min": 2, "max": 50, "init": 5, "interval": 1},
        }
    }