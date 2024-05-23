from filters import *

FILTERS = {}

from filters.Color import escala_grises
from filters.Color import inidie
from filters.Color import matiz
from filters.Color import saturador
from filters.Desenfoque import bilateral
from filters.Desenfoque import box
from filters.Desenfoque import desenfoque_gausiano
from filters.Desenfoque import desenfoque_horizontal
from filters.Desenfoque import desenfoque_vertical
from filters.Desenfoque import mediana
from filters.espejo import espejo
from filters.glitch import glitch
from filters.glitch import shift
from filters.glitch import shift_pro
from filters.pixel import pixelar
from filters.pixel import pixelar_pro
from filters.Ruido import ruido_gausiano
from filters.varios import dilatar
from filters.varios import dilatar_pro
from filters.varios import erode
from filters.varios import super_queee

FILTERS = {
    "Color": {
        "escala_grises": {
            "apply": escala_grises.apply_effect,
        },
        "inidie": {
            "apply": inidie.apply_effect,
            "parameters": {
                "blur_kernel_size": {'min': 3, 'max': 15, 'init': 5, 'interval': 2},
                "canny_threshold1": {'min': 50, 'max': 150, 'init': 100, 'interval': 10},
                "canny_threshold2": {'min': 100, 'max': 250, 'init': 200, 'interval': 10},
                "color_adjustment": {'min': 0.5, 'max': 2.0, 'init': 1.5, 'interval': 0.1},
                "noise_level": {'min': 10, 'max': 30, 'init': 20, 'interval': 5},
            }
        },
        "matiz": {
            "apply": matiz.apply_effect,
            "parameters": {
                "hue_shift": {'min': -180, 'max': 180, 'init': 0, 'interval': 1},
            }
        },
        "saturador": {
            "apply": saturador.apply_effect,
            "parameters": {
                "color": {'options': ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta'], 'init': 'red'},
                "saturation_scale": {'min': 0, 'max': 100, 'init': 50, 'interval': 1},
                "brightness_boost": {'min': 0, 'max': 100, 'init': 50, 'interval': 1},
            }
        },
    },
    "Desenfoque": {
        "bilateral": {
            "apply": bilateral.apply_effect,
            "parameters": {
                "d": {'min': 1, 'max': 10, 'init': 3, 'interval': 1},
                "sigmaColor": {'min': 1, 'max': 100, 'init': 20, 'interval': 1},
                "sigmaSpace": {'min': 1, 'max': 100, 'init': 15, 'interval': 1},
            }
        },
        "box": {
            "apply": box.apply_effect,
            "parameters": {
                "ksize_x": {'min': 3, 'max': 15, 'init': 5, 'interval': 2},
                "ksize_y": {'min': 3, 'max': 15, 'init': 5, 'interval': 2},
            }
        },
        "desenfoque_gausiano": {
            "apply": desenfoque_gausiano.apply_effect,
            "parameters": {
                "kernel_size": {'min': 1, 'max': 31, 'init': 15, 'interval': 2},
                "sigma": {'min': 1, 'max': 10, 'init': 5, 'interval': 1},
            }
        },
        "desenfoque_horizontal": {
            "apply": desenfoque_horizontal.apply_effect,
            "parameters": {
                "kernel_size": {'min': 1, 'max': 101, 'init': 3, 'interval': 2},
            }
        },
        "desenfoque_vertical": {
            "apply": desenfoque_vertical.apply_effect,
            "parameters": {
                "multi": {'min': 1, 'max': 100, 'init': 30, 'interval': 1},
            }
        },
        "mediana": {
            "apply": mediana.apply_effect,
            "parameters": {
                "kernel_size": {'min': 1, 'max': 101, 'init': 3, 'interval': 2},
            }
        },
    },
    "espejo": {
        "espejo": {
            "apply": espejo.apply_effect,
            "parameters": {
                "angle": {'min': -45, 'max': 45, 'init': 0, 'interval': 1},
                "direction": {'options': ['Horizontal', 'Vertical'], 'init': 'Horizontal'},
                "flip_type": {'options': ['Full', 'Partial'], 'init': 'Full'},
                "split_ratio": {'min': 1, 'max': 9, 'init': 5, 'interval': 1},
            }
        },
    },
    "glitch": {
        "glitch": {
            "apply": glitch.apply_effect,
            "parameters": {
                "glitch_intensity": {'min': 1, 'max': 50, 'init': 10, 'interval': 1},
                "glitch_frequency": {'min': 1, 'max': 50, 'init': 5, 'interval': 1},
            }
        },
        "shift": {
            "apply": shift.apply_effect,
            "parameters": {
                "shift_value": {'min': -50, 'max': 50, 'init': 5, 'interval': 1},
            }
        },
        "shift_pro": {
            "apply": shift_pro.apply_effect,
            "parameters": {
                "shift_value_b": {'min': -50, 'max': 50, 'init': 5, 'interval': 1},
                "shift_value_g": {'min': -50, 'max': 50, 'init': -5, 'interval': 1},
                "shift_value_r": {'min': -50, 'max': 50, 'init': 2, 'interval': 1},
                "direction_b": {'options': ['horizontal', 'vertical'], 'init': 'horizontal'},
                "direction_g": {'options': ['horizontal', 'vertical'], 'init': 'horizontal'},
                "direction_r": {'options': ['horizontal', 'vertical'], 'init': 'vertical'},
            }
        },
    },
    "pixel": {
        "pixelar": {
            "apply": pixelar.apply_effect,
            "parameters": {
                "block_size": {'min': 2, 'max': 50, 'init': 5, 'interval': 1},
            }
        },
        "pixelar_pro": {
            "apply": pixelar_pro.apply_effect,
            "parameters": {
                "block_size": {'min': 2, 'max': 50, 'init': 5, 'interval': 1},
                "method": {'options': ['mean', 'median', 'mode'], 'init': 'mean'},
                "intensity": {'min': 0.1, 'max': 2.0, 'init': 1.0, 'interval': 0.1},
                "block_shape": {'options': ['square', 'rectangular'], 'init': 'square'},
            }
        },
    },
    "Ruido": {
        "ruido_gausiano": {
            "apply": ruido_gausiano.apply_effect,
            "parameters": {
                "mean": {'min': -100, 'max': 100, 'init': 0, 'interval': 10},
                "std_dev": {'min': 1, 'max': 10, 'init': 5, 'interval': 1},
            }
        },
    },
    "varios": {
        "dilatar": {
            "apply": dilatar.apply_effect,
            "parameters": {
                "kernel_size": {'min': 2, 'max': 50, 'init': 5, 'interval': 1},
            }
        },
        "dilatar_pro": {
            "apply": dilatar_pro.apply_effect,
            "parameters": {
                "kernel_size": {'min': 2, 'max': 50, 'init': 5, 'interval': 1},
                "anchor": {'min': -1, 'max': -1, 'init': -1, 'interval': 1},
                "iterations": {'min': 1, 'max': 10, 'init': 1, 'interval': 1},
                "border_value": {'min': 0, 'max': 255, 'init': 0, 'interval': 1},
            }
        },
        "erode": {
            "apply": erode.apply_effect,
            "parameters": {
                "kernel_size": {'min': 2, 'max': 50, 'init': 5, 'interval': 1},
                "anchor": {'min': -1, 'max': -1, 'init': -1, 'interval': 1},
                "iterations": {'min': 1, 'max': 10, 'init': 1, 'interval': 1},
                "border_type": {'min': 0, 'max': 4, 'init': 0, 'interval': 1},
                "border_value": {'min': 0, 'max': 255, 'init': 0, 'interval': 1},
            }
        },
        "super_queee": {
            "apply": super_queee.apply_effect,
            "parameters": {
                "blur_radius": {'min': 1, 'max': 10, 'init': 5, 'interval': 1},
                "morphology_iterations": {'min': 1, 'max': 5, 'init': 2, 'interval': 1},
                "pyramid_levels": {'min': 1, 'max': 5, 'init': 3, 'interval': 1},
            }
        },
    },
}
