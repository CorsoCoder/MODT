import cv2

def apply_effect(image, kernel_size):
    kernel_size = max(1, kernel_size)  
    kernel_size = kernel_size + (kernel_size % 2 == 0)  
    return cv2.medianBlur(image, kernel_size)

def get_filter_data():
    return {
        "parameters": {
            "kernel_size": {"min": 1, "max": 101, "init": 3, "interval": 2}
        }
    }
