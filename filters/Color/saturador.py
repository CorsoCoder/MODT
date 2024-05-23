import cv2
import numpy as np

def apply_effect(image, color, saturation_scale, brightness_boost):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv_image)

    color_ranges = {
        'red': [(0, 10), (160, 180)],
        'green': [(35, 85)],
        'blue': [(100, 140)],
        'yellow': [(25, 35)],
        'cyan': [(85, 100)],
        'magenta': [(140, 160)]
    }

    masks = []
    for (lower, upper) in color_ranges[color]:
        mask = cv2.inRange(h, lower, upper)
        masks.append(mask)

    color_mask = cv2.bitwise_or(*masks) if len(masks) > 1 else masks[0]

    s = cv2.add(s, (saturation_scale * (color_mask // 255)).astype(np.uint8))
    v = cv2.add(v, (brightness_boost * (color_mask // 255)).astype(np.uint8))

    s = np.clip(s, 0, 255)
    v = np.clip(v, 0, 255)

    enhanced_hsv_image = cv2.merge([h, s, v])

    enhanced_image = cv2.cvtColor(enhanced_hsv_image, cv2.COLOR_HSV2BGR)

    return enhanced_image

def get_filter_data():
    return {
        "parameters": {
            "color": {"options": ["red", "green", "blue", "yellow", "cyan", "magenta"], "init": "red"},
            "saturation_scale": {"min": 0, "max": 100, "init": 50, "interval": 1},
            "brightness_boost": {"min": 0, "max": 100, "init": 50, "interval": 1}
        }
    }