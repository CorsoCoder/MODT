import cv2
import numpy as np

def apply_effect(image, block_size, method='mean', intensity=1.0, block_shape='square'):
    num_blocks_x = int(image.shape[1] / block_size)
    num_blocks_y = int(image.shape[0] / block_size)

    pixelated_image = np.zeros_like(image)

    for y in range(num_blocks_y):
        for x in range(num_blocks_x):
            start_x = x * block_size
            end_x = (x + 1) * block_size
            start_y = y * block_size
            end_y = (y + 1) * block_size
            block = image[start_y:end_y, start_x:end_x]
            if method == 'mean':
                pixel_value = block.mean(axis=(0, 1))
            elif method == 'median':
                pixel_value = np.median(block, axis=(0, 1))
            elif method == 'mode':
                pixel_value = np.squeeze(cv2.calcHist([block], [0], None, [256], [0, 256])).argmax()
            else:
                raise ValueError("Invalid pixelation method")
            pixelated_image[start_y:end_y, start_x:end_x] = pixel_value

    pixelated_image = (pixelated_image * intensity).astype(np.uint8)

    return pixelated_image

def get_filter_data():
    return {
        "parameters": {
            "block_size": {"min": 2, "max": 50, "init": 5, "interval": 1},
            "method": {"options": ["mean", "median", "mode"], "init": "mean"},
            "intensity": {"min": 0.1, "max": 2.0, "init": 1.0, "interval": 0.1},
            "block_shape": {"options": ["square", "rectangular"], "init": "square"}
        }
    }
