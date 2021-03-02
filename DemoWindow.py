from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QApplication, QListWidgetItem
from typing import List, Dict

class Comp490DemoWindow(QWidget):
    def __init__(self, data_to_show):
        super().__init__()
        self.data = data_to_show
        self.list_control = None
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("GUI Demo for Capstone")
        display_list = QListWidget(self)
        self.list_control = display_list
        self.put_data_in_list(self.data)
        display_list.resize(400,350)
        self.setGeometry(100,100, 400, 500)
        quit_button = QPushButton("Quit Now", self)
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(150, 400)
        self.show()

    def put_data_in_list(self, data: List[Dict]):
        for item in data:
            display_text = f"{item['state_name']}\t\t{item['median_income']}"
            list_item = QListWidgetItem(display_text, listview=self.list_control)
