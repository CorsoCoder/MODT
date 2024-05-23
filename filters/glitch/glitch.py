import cv2
import numpy as np

def apply_effect(image, glitch_intensity, glitch_frequency):
    rows, cols, _ = image.shape
    glitch_image = image.copy()

    for i in range(0, rows, glitch_frequency):
        shift = np.random.randint(-glitch_intensity, glitch_intensity)
        glitch_image[i] = np.roll(image[i], shift, axis=0)

    return glitch_image

def get_filter_data():
    return {
        "parameters": {
            "glitch_intensity": {"min": 1, "max": 50, "init": 10, "interval": 1},
            "glitch_frequency": {"min": 1, "max": 50, "init": 5, "interval": 1}
        }
    }
