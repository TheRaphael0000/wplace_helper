from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QFileDialog, QScrollArea, QGridLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from wplace_helper.lib import (
    color_reduction,
    ensure_alpha_channel,
    wplace_colors_map_rgb,
    color_split,
)
from .utils import convert_cv_to_qpixmap
import cv2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wplace Helper")

        self.setMinimumSize(600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout_main = QGridLayout(self.central_widget)

        self.btn_open = QPushButton("Open image")
        self.btn_save = QPushButton("Save")

        self.lbl_img_1 = QLabel()
        self.lbl_img_1.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.sa_1 = QScrollArea()
        self.sa_1.setWidgetResizable(True)
        self.sa_1.setWidget(self.lbl_img_1)

        self.lbl_img_2 = QLabel()
        self.lbl_img_2.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.sa_2 = QScrollArea()
        self.sa_2.setWidgetResizable(True)
        self.sa_2.setWidget(self.lbl_img_2)

        self.layout_main.addWidget(QLabel("Original Image"), 0, 0)
        self.layout_main.addWidget(self.btn_open, 0, 1)
        self.layout_main.addWidget(QLabel("Palettise Image"), 0, 2)
        self.layout_main.addWidget(self.btn_save, 0, 3)

        self.layout_main.addWidget(self.sa_1, 1, 0, 1, 2)
        self.layout_main.addWidget(self.sa_2, 1, 2, 1, 2)

        self.btn_open.clicked.connect(self.on_btn_open_click)
        self.btn_save.clicked.connect(self.on_btn_save_click)

        self.cv_original_img = None
        self.cv_palettise_img = None
        self.cv_single_color_imgs = []

    def on_btn_save_click(self):
        file_dialog = QFileDialog()
        dir_path = file_dialog.getExistingDirectory(
            self,
            "Select save directory"
        )
        print(dir_path)

    def on_btn_open_click(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Select image file",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_path:
            return

        self.cv_original_img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        self.cv_original_img = ensure_alpha_channel(self.cv_original_img)

        self.set_cv_img_to_label(self.cv_original_img, self.lbl_img_1)

        print("color reduc")
        self.cv_palettise_img = color_reduction(
            self.cv_original_img, wplace_colors_map_rgb)
        self.set_cv_img_to_label(self.cv_palettise_img, self.lbl_img_2)

        print("img to")
        for (img_single_color, nb_pixels, color_label) in color_split(self.cv_palettise_img):
            self.cv_single_color_imgs.append(img_single_color)
        print("done")

    def set_cv_img_to_label(self, cv_img, lbl: QLabel):
        print("set image 2 label")
        pixmap = convert_cv_to_qpixmap(cv_img)
        if pixmap.isNull():
            lbl.setText(
                "Could not load image. Please select a valid image file."
            )
            return
        lbl.setPixmap(pixmap)
