import cv2
import numpy as np
import os
import pathlib
from .wplace_colors import wplace_colors_map


def img_to_unique_colors_imgs(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    img_2d = img.reshape(img.shape[0] * img.shape[1], img.shape[2])
    unique_colors = np.unique(img_2d, axis=0)

    # ensure we dont have an non-palettised image
    assert len(unique_colors) <= 64

    output_folder = pathlib.Path(path.split(".")[0])
    os.makedirs(output_folder, exist_ok=True)

    for unique_color in unique_colors:
        if unique_color[-1] <= 0:
            continue

        mask = (img == unique_color).all(axis=-1)

        nb_pixels = np.sum(mask)

        img_single_color = np.zeros_like(img)
        img_single_color[mask] = img[mask]

        try:
            # BGR to RGB
            color_label = wplace_colors_map[(
                unique_color[2], unique_color[1], unique_color[0])]
        except:
            print(unique_color, "is not a WPlace color!")
            unique_color_str = unique_color.astype(str)
            # BGR to RGB
            color_label = f"{unique_color_str[2]}_{unique_color_str[1]}_{unique_color_str[0]}"

        output_path = output_folder / \
            f'{color_label.replace(" ", "_")}-{nb_pixels}pixels.png'

        cv2.imwrite(str(output_path), img_single_color)
