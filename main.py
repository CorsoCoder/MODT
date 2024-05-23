import sys
import cv2
from PyQt5.QtWidgets import (
    QApplication, QComboBox, QMainWindow, QSizePolicy, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QSlider, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QIcon
from effects_settings import FILTERS

class PhotoEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MODT - Photo Editor")
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon("assets/calavera.gif"))
        self.image = None
        self.original_image = None
        self.active_filter = None
        self.active_category = None
        self.sliders = []
        self.comboboxes = []
        self.initUI()

    def initUI(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #000;
            }
            QWidget {
                background-color: #222;
                color: #fff;
            }
            QLabel {
                color: #fff;
            }
            QComboBox, QSlider, QPushButton {
                background-color: #333;
                color: #fff;
                border: 1px solid #666;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

        slider_style = """
            QSlider::groove:horizontal {
                height: 6px;
                background: #444;
                border: 1px solid #666;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #4CAF50;
                border: 1px solid #4CAF50;
                width: 12px;
                margin: -6px 0;
                border-radius: 6px;
            }
        """

        combobox_style = """
            QComboBox {
                max-width: 200px;
                padding: 3px;
                border: 1px solid #666;
                border-radius: 2px;
            }
            QComboBox::drop-down {
                width: 20px;
            }
            QComboBox::down-arrow {
                width: 10px;
                height: 10px;
            }
        """

        button_style = """
            QPushButton {
                padding: 8px 16px;
                border: 2px solid #4CAF50;
                border-radius: 25px;
                background-color: #4CAF50;
                color: #fff;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """

        self.filter_button_style = button_style 

        file_button_style = """
            QPushButton {
                padding: 8px 16px;
                border: 2px solid #008CBA;
                border-radius: 25px;
                background-color: #008CBA;
                color: #fff;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005f78;
            }
        """

        slider_label_style = """
            QLabel {
                color: #fff;
                font-weight: bold;
            }
        """

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        self.filter_buttons_layout = QVBoxLayout()
        main_layout.addLayout(self.filter_buttons_layout)

        self.category_combo = QComboBox(self)
        self.category_combo.addItems(FILTERS.keys())
        self.category_combo.currentTextChanged.connect(self.update_filter_buttons)
        self.filter_buttons_layout.addWidget(self.category_combo)

        self.filter_buttons_row_layout = QVBoxLayout()
        self.filter_buttons_layout.addLayout(self.filter_buttons_row_layout)

        right_layout = QVBoxLayout()
        right_layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_layout.addWidget(self.image_label)

        load_btn = QPushButton("Cargar Imagen", self)
        load_btn.clicked.connect(self.load_image)
        load_btn.setStyleSheet(file_button_style)
        right_layout.addWidget(load_btn)

        self.slider_layout = QVBoxLayout()
        self.slider_layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)
        right_layout.addLayout(self.slider_layout)

        save_btn = QPushButton("Guardar Imagen", self)
        save_btn.clicked.connect(self.save_image)
        save_btn.setStyleSheet(file_button_style)
        right_layout.addWidget(save_btn)

        combined_style = combobox_style + slider_style + slider_label_style 
        app.setStyleSheet(combined_style)

        main_layout.addLayout(right_layout)
        central_widget.setLayout(main_layout)

        self.update_filter_buttons()

    def update_filter_buttons(self):
        for i in reversed(range(self.filter_buttons_row_layout.count())):
            widget = self.filter_buttons_row_layout.itemAt(i).widget()
            widget.deleteLater()

        category = self.category_combo.currentText()
        if category in FILTERS:
            for filter_name in FILTERS[category].keys():
                btn = QPushButton(filter_name, self)
                btn.clicked.connect(lambda _, c=category, f=filter_name: self.apply_filter(c, f))
                btn.setStyleSheet(self.filter_button_style)
                self.filter_buttons_row_layout.addWidget(btn)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Cargar Imagen", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.image = self.original_image.copy()
            self.display_image(self.image)

    def display_image(self, img):
        widget_width = self.width()
        widget_height = self.height()

        max_width = int(widget_width * 0.7)
        max_height = int(widget_height * 0.7)

        img_height, img_width = img.shape[:2]

        aspect_ratio = img_width / img_height

        if img_width > max_width or img_height > max_height:
            if img_width / max_width > img_height / max_height:
                new_width = max_width
                new_height = int(max_width / aspect_ratio)
            else:
                new_height = max_height
                new_width = int(max_height * aspect_ratio)
        else:
            new_width = img_width
            new_height = img_height

        resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

        if len(resized_img.shape) == 2:
            q_img = QImage(resized_img.data, resized_img.shape[1], resized_img.shape[0], resized_img.strides[0], QImage.Format_Grayscale8)
        else:
            q_img = QImage(resized_img.data, resized_img.shape[1], resized_img.shape[0], resized_img.strides[0], QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(q_img)
        self.image_label.setPixmap(pixmap)

    def resizeEvent(self, event):
        if self.image is not None:
            self.display_image(self.image)
        super().resizeEvent(event)

    def apply_filter(self, category, filter_name):
        if self.original_image is None:
            self.show_message("Advertencia", "Primero carga una imagen.")
            return
        self.active_category = category
        self.active_filter = filter_name
        self.update_effect()

    def update_effect(self):
        if self.original_image is None:
            self.show_message("Advertencia", "Primero carga una imagen.")
            return
        if self.active_filter is not None:
            filter_info = FILTERS[self.active_category][self.active_filter]
            if "parameters" in filter_info and filter_info["parameters"]:
                self.update_sliders()
            else:
                self.image = filter_info["apply"](self.original_image)
                self.display_image(self.image)

    def save_image(self):
        if self.image is not None:
            file_path, _ = QFileDialog.getSaveFileName(self, "Guardar Imagen", "", "Images (*.png *.jpg *.jpeg *.bmp)")
            if file_path:
                cv2.imwrite(file_path, self.image)
                QMessageBox.information(self, "Éxito", "La imagen se ha guardado correctamente.")
        else:
            QMessageBox.warning(self, "Advertencia", "No hay ninguna imagen para guardar.")

    def update_sliders(self):
        if self.original_image is None:
            self.show_message("Advertencia", "Primero carga una imagen.")
            return

        self.clear_sliders()

        filter_info = FILTERS[self.active_category][self.active_filter]

        for param_name, param_info in filter_info["parameters"].items():
            if "options" in param_info:
                combobox = QComboBox(self)
                combobox.addItems(param_info["options"])
                combobox.setCurrentText(param_info["init"])
                combobox.currentTextChanged.connect(self.update_slider_value)
                combobox.setFixedHeight(25)
                combobox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                self.comboboxes.append((param_name, combobox))
                self.slider_layout.addWidget(QLabel(param_name))
                self.slider_layout.addWidget(combobox)
            else:
                slider = QSlider(Qt.Horizontal, minimum=int(param_info["min"]), maximum=int(param_info["max"]), value=int(param_info["init"]), singleStep

=int(param_info["interval"]))
                slider.valueChanged.connect(self.update_slider_value)
                slider.setFixedHeight(20)
                slider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                self.sliders.append((param_name, slider))
                self.slider_layout.addWidget(QLabel(param_name))
                self.slider_layout.addWidget(slider)
        
        self.image = filter_info["apply"](self.original_image, **self.get_slider_values())
        self.display_image(self.image)

    def show_message(self, title, message):
        QMessageBox.warning(self, title, message)

    def get_slider_values(self):
        values = {param_name: slider.value() for param_name, slider in self.sliders}
        values.update({param_name: combobox.currentText() for param_name, combobox in self.comboboxes})
        return values

    def update_slider_value(self):
        filter_info = FILTERS[self.active_category][self.active_filter]
        self.image = filter_info["apply"](self.original_image, **self.get_slider_values())
        self.display_image(self.image)

    def clear_sliders(self):
        for param_name, slider in self.sliders:
            slider.deleteLater()
        for param_name, combobox in self.comboboxes:
            combobox.deleteLater()
        for i in reversed(range(self.slider_layout.count())):
            item = self.slider_layout.itemAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.sliders = []
        self.comboboxes = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor_app = PhotoEditorApp()
    editor_app.show()
    sys.exit(app.exec_())
