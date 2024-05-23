import cv2 as cv

def apply_effect(image, d=3, sigmaColor=20, sigmaSpace=15):
    return cv.bilateralFilter(image, d, sigmaColor, sigmaSpace)

def get_filter_data():
    return {
        "parameters": {
            "d": {"min": 1, "max": 10, "init": 3, "interval": 1},
            "sigmaColor": {"min": 1, "max": 100, "init": 20, "interval": 1},
            "sigmaSpace": {"min": 1, "max": 100, "init": 15, "interval": 1}
        }
    }
