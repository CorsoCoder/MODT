import cv2
import numpy as np

def apply_effect(image, shift_value):
    b_channel, g_channel, r_channel = cv2.split(image)

    zeros = np.zeros_like(b_channel)

    b_shifted = np.roll(b_channel, shift_value, axis=1)
    g_shifted = np.roll(g_channel, -shift_value, axis=1)
    r_shifted = np.roll(r_channel, shift_value // 2, axis=0)

    merged = cv2.merge([b_shifted, g_shifted, r_shifted])

    return merged

def get_filter_data():
    return {
        "parameters": {
            "shift_value": {"min": -50, "max": 50, "init": 5, "interval": 1}
        }
    }
