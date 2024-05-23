import cv2
import numpy as np

def apply_effect(image, shift_value_b, shift_value_g, shift_value_r, direction_b, direction_g, direction_r):
    
    b_channel, g_channel, r_channel = cv2.split(image)

    zeros = np.zeros_like(b_channel)

    axis_b = 1 if direction_b == 'horizontal' else 0
    axis_g = 1 if direction_g == 'horizontal' else 0
    axis_r = 1 if direction_r == 'horizontal' else 0

    b_shifted = np.roll(b_channel, shift_value_b, axis=axis_b)
    g_shifted = np.roll(g_channel, shift_value_g, axis=axis_g)
    r_shifted = np.roll(r_channel, shift_value_r, axis=axis_r)

    merged = cv2.merge([b_shifted, g_shifted, r_shifted])

    return merged

def get_filter_data():
    return {
        "parameters": {
            "shift_value_b": {"min": -50, "max": 50, "init": 5, "interval": 1},
            "shift_value_g": {"min": -50, "max": 50, "init": -5, "interval": 1},
            "shift_value_r": {"min": -50, "max": 50, "init": 2, "interval": 1},
            "direction_b": {"options": ["horizontal", "vertical"], "init": "horizontal"},
            "direction_g": {"options": ["horizontal", "vertical"], "init": "horizontal"},
            "direction_r": {"options": ["horizontal", "vertical"], "init": "vertical"}
        }
    }