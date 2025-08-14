import numpy as np
from .wplace_colors import wplace_colors_map_bgr


def color_reduction(img):
    palette = np.array(list(wplace_colors_map_bgr.keys()), dtype=np.uint8)

    height, width, _ = img.shape
    bgr = img[:, :, :3]
    alpha = img[:, :, 3]

    pixels = bgr.reshape(-1, 3).astype(np.float32)

    palette_broadcastable = palette.astype(np.float32)[np.newaxis, :, :]
    distances_sq = np.sum(
        (pixels[:, np.newaxis, :] - palette_broadcastable) ** 2, axis=2)
    closest_color_indices = np.argmin(distances_sq, axis=1)
    reduced_pixels = palette[closest_color_indices]
    reduced_bgr = reduced_pixels.reshape(height, width, 3)
    reduced_img = np.dstack((reduced_bgr, alpha))

    return reduced_img
