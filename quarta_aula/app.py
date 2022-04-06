import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from forms import MainForm

QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

app = QApplication(sys.argv)

main = MainForm()
main.show()

sys.exit(app.exec_())
