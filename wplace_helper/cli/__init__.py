import cv2
import argparse
from wplace_helper.lib import (
    color_reduction,
    img_info,
    color_split,
    ensure_alpha_channel,
    wplace_colors_map_rgb,
)
import pathlib
import os


def main():
    parser = argparse.ArgumentParser(
        prog='WPlace Helper',
        description='Split image by color',
        epilog='github.com/TheRaphael0000/wplace_helper'
    )
    parser.add_argument("filename", )
    parser.add_argument(
        "--no-reduction",
        action='store_true',
        help="Doesn't perform color reduction (a.k.a. Palettise). If you didn't palettise your image first you'll end up with a lot of images. Only use it if you know what you are doing."
    )

    args = parser.parse_args()

    path = args.filename

    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    img = ensure_alpha_channel(img)

    output_folder = pathlib.Path(path.split(".")[0])

    os.makedirs(output_folder, exist_ok=True)

    nb_non_transparent = img_info(img)
    nb_digits = len(str(nb_non_transparent))

    if not args.no_reduction:
        img = color_reduction(img, wplace_colors_map_rgb)
        filename = f"{nb_non_transparent}_pixels_palettised.png"
        cv2.imwrite(str(output_folder / filename), img)

    for (img_single_color, nb_pixels, color_label) in color_split(img):
        filename = f'{str(nb_pixels).zfill(nb_digits)}_pixels_{color_label.replace(" ", "_")}.png'
        cv2.imwrite(str(output_folder / filename), img_single_color)
