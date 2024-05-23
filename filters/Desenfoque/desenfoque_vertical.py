import cv2
import numpy as np

def apply_effect(image, multi):
    kernel_v = np.zeros((multi, multi), dtype=np.float64)
    kernel_v[:, int((multi - 1)/2)] = np.ones(multi)
    kernel_v /= multi
    return cv2.filter2D(image, -1, kernel_v)

def get_filter_data():
    return {
        "parameters": {
            "multi": {"min": 1, "max": 100, "init": 30, "interval": 1}
        }
    }
