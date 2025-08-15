from PySide6.QtWidgets import QApplication
from .main_window import MainWindow
import sys


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
