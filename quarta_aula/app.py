import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from controllers import MainController

QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

app = QApplication(sys.argv)

main = MainController()
main.showMaximized()

sys.exit(app.exec_())
