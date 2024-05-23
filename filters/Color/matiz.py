import cv2
import numpy as np

def apply_effect(image, hue_shift):

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    hsv_image[:, :, 0] = (hsv_image[:, :, 0] + hue_shift) % 180

    modified_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    
    return modified_image

def get_filter_data():

    return {
        "parameters": {
            "hue_shift": {"min": -180, "max": 180, "init": 0, "interval": 1}
        }
    }
