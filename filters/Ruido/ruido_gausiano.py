import numpy as np

def apply_effect(image, mean, std_dev):
    h, w, c = image.shape
    noise = np.random.normal(mean, std_dev, (h, w, c))
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image

def get_filter_data():
    return{ 
        "parameters": 
        {

        "mean": {"min": -100, "max": 100, "init": 0, "interval": 10},
        "std_dev": {"min": 1, "max": 10, "init": 5, "interval": 1}
    }   }

