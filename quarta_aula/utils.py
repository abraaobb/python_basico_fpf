from PyQt5.QtWidgets import QLineEdit, QComboBox


def limpar_components(widget):
    for index in range(widget.layout().count()):
        componente = widget.layout().itemAt(index).widget()
        if isinstance(componente, QLineEdit):
            componente.setText('')
        elif isinstance(componente, QComboBox):
            componente.setCurrentIndex(0)
