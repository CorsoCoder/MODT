import cv2
import numpy as np

def apply_effect(image, blur_kernel_size, canny_threshold1, canny_threshold2, color_adjustment, noise_level):
    
    if blur_kernel_size % 2 == 0:
        blur_kernel_size += 1

    blurred = cv2.GaussianBlur(image, (blur_kernel_size, blur_kernel_size), 0)

    edges = cv2.Canny(blurred, canny_threshold1, canny_threshold2)

    edges_3ch = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    indie_image = np.clip(color_adjustment * blurred - (1 - color_adjustment) * edges_3ch, 0, 255).astype(np.uint8)

    noise = np.random.normal(0, noise_level, image.shape).astype(np.uint8)
    indie_image = np.clip(indie_image + noise, 0, 255)

    return indie_image

def get_filter_data():
    return {
        "parameters": {
            "blur_kernel_size": {"min": 3, "max": 15, "init": 5, "interval": 2},
            "canny_threshold1": {"min": 50, "max": 150, "init": 100, "interval": 10},
            "canny_threshold2": {"min": 100, "max": 250, "init": 200, "interval": 10},
            "color_adjustment": {"min": 0.5, "max": 2.0, "init": 1.5, "interval": 0.1},
            "noise_level": {"min": 10, "max": 30, "init": 20, "interval": 5}
        }
    }
