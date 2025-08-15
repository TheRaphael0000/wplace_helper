import numpy as np
import cv2


def img_info(img):
    alpha_channel = img[:, :, 3]
    non_transparent_mask = alpha_channel > 0
    nb_non_transparent = np.sum(non_transparent_mask)
    return nb_non_transparent


def ensure_alpha_channel(image: np.ndarray) -> np.ndarray:
    if image.shape[2] == 4:
        return image
    elif image.shape[2] == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    elif image.shape[2] == 1:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2BGRA)
    else:
        raise ValueError("Unsupported number of channels in the image.")


def split_alpha(img):
    return img[:, :, :3], img[:, :, 3]


def merge_alpha(img_colors, img_alpha):
    return np.dstack((img_colors, img_alpha))
