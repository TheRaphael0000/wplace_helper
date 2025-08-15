import cv2
import argparse
from .split_by_color import img_to_unique_colors_imgs
from .color_reduction import color_reduction
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
        help="Doesn't perform color reduction (a.k.a. Palettise)."
        "If you didn't palettise your image first you'll end up with a lot of images."
        "Only use it if you know what you are doing."
    )

    args = parser.parse_args()

    path = args.filename

    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    output_folder = pathlib.Path(path.split(".")[0])

    os.makedirs(output_folder, exist_ok=True)

    if not args.no_reduction:
        img = color_reduction(img)
        cv2.imwrite(str(output_folder / "_color_reduced.png"), img)

    for (img_single_color, nb_pixels, color_label) in img_to_unique_colors_imgs(img):
        filename = f'{nb_pixels}_pixels-{color_label.replace(" ", "_")}.png'
        output_path = output_folder / filename
        cv2.imwrite(str(output_path), img_single_color)


if __name__ == "__main__":
    main()
