import numpy as np
from .wplace_colors import wplace_colors_map_bgr


def img_to_unique_colors_imgs(img):
    img_2d = img.reshape(img.shape[0] * img.shape[1], img.shape[2])
    unique_colors = np.unique(img_2d, axis=0)

    for unique_color in unique_colors:
        unique_color_plain = tuple(unique_color[:-1])
        if unique_color[-1] <= 0:
            continue

        mask = (img == unique_color).all(axis=-1)

        nb_pixels = np.sum(mask)

        img_single_color = np.zeros_like(img)
        img_single_color[mask] = img[mask]

        try:
            color_label = wplace_colors_map_bgr[unique_color_plain]
        except:
            # should not happen in the standard pipeline
            print(unique_color, "is not a WPlace color!")
            unique_color_plain_str = map(str, unique_color_plain)
            color_label = f"{'_'.join(unique_color_plain_str)}"

        yield (img_single_color, nb_pixels, color_label)
