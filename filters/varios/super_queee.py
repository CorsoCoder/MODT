import cv2
import numpy as np

def apply_effect(image, blur_radius, morphology_iterations, pyramid_levels):
    blurred_image = cv2.boxFilter(image, -1, (blur_radius, blur_radius))

    kernel = np.ones((5,5),np.uint8)
    morphology_image = cv2.morphologyEx(blurred_image, cv2.MORPH_GRADIENT, kernel, iterations=morphology_iterations)

    pyr_down_image = cv2.pyrDown(morphology_image, dstsize=(image.shape[1]//2, image.shape[0]//2))
    pyr_up_image = cv2.pyrUp(pyr_down_image, dstsize=(image.shape[1], image.shape[0]))

    return pyr_up_image

def get_filter_data():
    return {
        "parameters": {
            "blur_radius": {"min": 1, "max": 10, "init": 5, "interval": 1},
            "morphology_iterations": {"min": 1, "max": 5, "init": 2, "interval": 1},
            "pyramid_levels": {"min": 1, "max": 5, "init": 3, "interval": 1}
        }
    }