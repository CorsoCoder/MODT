

import cv2
import numpy as np

def apply_effect(image, block_size):
    # Calculate the number of blocks needed in each dimension
    num_blocks_x = int(image.shape[1] / block_size)
    num_blocks_y = int(image.shape[0] / block_size)

    # Create a new image with the desired pixelation
    pixelated_image = np.zeros((num_blocks_y * block_size, num_blocks_x * block_size, 3), dtype=np.uint8)

    # Loop through each block and copy the corresponding pixels from the original image
    for y in range(num_blocks_y):
        for x in range(num_blocks_x):
            start_x = x * block_size
            end_x = (x + 1) * block_size
            start_y = y * block_size
            end_y = (y + 1) * block_size
            block = image[start_y:end_y, start_x:end_x]
            pixelated_image[start_y:end_y, start_x:end_x] = block.mean(axis=(0, 1))

    return pixelated_image
def get_filter_data():
    return {
        "parameters": {
            "block_size": {"min": 2, "max": 50, "init": 5, "interval": 1},        }
    }
