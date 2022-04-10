from PyQt5.QtWidgets import QMainWindow

from main import Ui_Main


class MainController(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        