import numpy as np
from skimage.color import rgb2lab, deltaE_ciede2000

from wplace_helper.lib.utils import merge_alpha, split_alpha
import cv2


def color_reduction_lab(image_rgb, palette_rgb):
    image_lab = rgb2lab(image_rgb/255)
    palette_lab = rgb2lab(palette_rgb/255)

    image_lab_repeat = palette_lab.shape[0]
    image_lab_repeated = np.repeat(
        image_lab, image_lab_repeat, axis=1).reshape(-1, 3)

    palette_repeat = image_lab.shape[0] * image_lab.shape[1]
    palette_repeated = np.tile(palette_lab.T, palette_repeat).T

    distances = deltaE_ciede2000(image_lab_repeated, palette_repeated, channel_axis=1).reshape(
        image_lab.shape[0], image_lab.shape[1], palette_lab.shape[0])
    argmin = np.argmin(distances, axis=2)

    image_palettised = palette_rgb[argmin]

    return image_palettised


def color_reduction(image_bgra, palette):
    img_rgba = cv2.cvtColor(image_bgra, cv2.COLOR_BGRA2RGBA)
    palette = np.array(list(palette.keys()), dtype=np.uint8)

    img_rgb, img_alpha = split_alpha(img_rgba)
    img_rgb_reduced = color_reduction_lab(img_rgb, palette)
    img_rgba_reduced = merge_alpha(img_rgb_reduced, img_alpha)

    img = cv2.cvtColor(img_rgba_reduced, cv2.COLOR_RGBA2BGRA)

    return img
