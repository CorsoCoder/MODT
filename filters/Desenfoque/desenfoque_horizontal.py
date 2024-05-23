import cv2
import numpy as np
def apply_effect(image, kernel_size):
    kernel_h = np.zeros((kernel_size, kernel_size))
    kernel_h[int((kernel_size - 1)/2), :] = np.ones(kernel_size)
    kernel_h /= kernel_size
    return cv2.filter2D(image, -1, kernel_h)

def get_filter_data():
    return {
        "parameters": {
            "kernel_size": {"min": 1, "max": 101, "init": 3, "interval": 2}
        }
    }