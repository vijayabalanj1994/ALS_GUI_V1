import sys
from PIL import Image

import numpy as np

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QImage ,QPixmap
from PySide6.QtCore import Qt

from MainWindow.UI.main_window import Ui_MainWindow

def pil2pixmap(im):
    im = im.convert("RGBA")
    data = im.tobytes("raw", "RGBA")
    qimage = QImage(data, im.width, im.height, QImage.Format_RGBA8888)
    return QPixmap.fromImage(qimage)

class HomeWindow(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.input_image_path =""
        self.pb_browse.clicked.connect(self.browse_image)

        self.pb_run.clicked.connect(self.run_model)

    @qtc.Slot()
    def browse_image(self):

        self.input_image_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select an Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.tif)"
        )

        print(self.input_image_path)

        if self.input_image_path:
            try:
                pil_image = Image.open(self.input_image_path)
                pixmap = pil2pixmap(pil_image)

                self.lb_input_image.setPixmap(
                    pixmap.scaled(
                        self.lb_input_image.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                )
            except Exception as e:
                self.lb_input_image.setText("Unable to load image.")

    def update_progress_bar(self, results:list):

        class_labels = ["control", "discordant", "concordant"]

        for label, value in zip(class_labels, results):
            bar = getattr(self, f"p_bar_{label}")
            bar.setValue(int(value))

        ranked = sorted(
            zip(class_labels, results),
            key=lambda x: x[1],
            reverse=True  # Highest confidence first
        )

        rank_colors = ["#4CAF50", "#FFA726", "#FFEB3B"]  # Green, Orange, Yellow

        for i, (label, _) in enumerate(ranked):
            bar = getattr(self, f"p_bar_{label}")
            color = rank_colors[i]
            bar.setStyleSheet(f"""
                QProgressBar {{
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    text-align: center;
                }}
                QProgressBar::chunk {{
                    background-color: {color};
                    width: 10px;
                }}
            """)

    @qtc.Slot()
    def run_model(self):
        if self.input_image_path:
            try:
                pil_image = Image.open(self.input_image_path)
                pixmap = pil2pixmap(pil_image)

                self.lb_CAM_image.setPixmap(
                    pixmap.scaled(
                        self.lb_CAM_image.size(),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                )

                self.update_progress_bar([5,70,25])
                
            except Exception as e:
                self.lb_CAM_image.setText("Unable to load image.")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = HomeWindow()
    window.show()
    sys.exit(app.exec())