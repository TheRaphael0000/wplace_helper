from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QFileDialog, QScrollArea, QGridLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from wplace_helper.lib import color_reduction, ensure_alpha_channel
from .utils import convert_cv_to_qpixmap
import cv2


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wplace Helper")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout_main = QGridLayout(self.central_widget)

        self.btn_browse = QPushButton("Browse image")
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

        self.layout_main.addWidget(self.btn_browse, 0, 0, 1, 2)

        self.layout_main.addWidget(QLabel("Original Image"), 1, 0)
        self.layout_main.addWidget(self.sa_1, 2, 0)

        self.layout_main.addWidget(QLabel("Palettise Image"), 1, 1)
        self.layout_main.addWidget(self.sa_2, 2, 1)

        self.layout_main.addWidget(self.btn_save, 3, 0, 1, 2)

        self.btn_browse.clicked.connect(self.on_button_click)

    def on_button_click(self):

        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Select Image File",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp)"
        )

        if not file_path:
            return

        pixmap = QPixmap(file_path)

        if pixmap.isNull():
            self.lbl_img_1.setText(
                "Could not load image. Please select a valid image file."
            )
            return

        self.lbl_img_1.setPixmap(pixmap)

        cv_img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        cv_img = ensure_alpha_channel(cv_img)
        cv_img = color_reduction(cv_img)

        pixmap2 = convert_cv_to_qpixmap(cv_img)

        if pixmap2.isNull():
            self.lbl_img_2.setText(
                "Could not load image. Please select a valid image file."
            )
            return

        self.lbl_img_2.setPixmap(pixmap2)
