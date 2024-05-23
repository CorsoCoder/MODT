import cv2

def apply_effect(image, kernel_size, sigma):
    kernel_size = kernel_size + (kernel_size % 2 == 0)
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

def get_filter_data():
    return {
        "parameters": {
            "kernel_size": {"min": 1, "max": 31, "init": 15, "interval": 2},
            "sigma": {"min": 1, "max": 10, "init": 5, "interval": 1}
        }
    }
    