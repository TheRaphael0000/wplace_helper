from PySide6.QtGui import QPixmap, QImage

import cv2
import numpy as np


def convert_cv_to_qpixmap(cv_image: np.ndarray) -> QPixmap:
    rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGRA2RGBA)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    q_image = QImage(
        rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGBA8888
    )
    return QPixmap.fromImage(q_image)
