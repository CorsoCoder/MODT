import cv2

def apply_effect(image, ksize_x, ksize_y):
    blurred_image = cv2.boxFilter(image, -1, (ksize_x, ksize_y))
    return blurred_image

def get_filter_data():
    return {
        "parameters": {
            "ksize_x": {"min": 3, "max": 15, "init": 5, "interval": 2},
            "ksize_y": {"min": 3, "max": 15, "init": 5, "interval": 2}
        }
    }
