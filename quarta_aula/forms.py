from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QPushButton, QTableWidget, QTableWidgetItem

import estilo
import utils
from models import Funcionario


class MainForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(estilo.qlabel)

        self.label_mensagem = QLabel()
        self.label_mensagem.hide()
        self.label_mensagem.setStyleSheet('color: green')

        self.label_nome = QLabel()
        self.label_nome.setText('Nome')

        self.line_edit_nome = QLineEdit()
        self.line_edit_nome.setFixedHeight(40)

        self.label_sexo = QLabel()
        self.label_sexo.setText('Sexo')

        self.combo_box_sexo = QComboBox()
        self.combo_box_sexo.addItems(['Masculino', 'Feminino'])
        self.combo_box_sexo.setFixedHeight(40)

        self.label_salario = QLabel()
        self.label_salario.setText('Salario')

        self.line_edit_salario = QLineEdit()
        self.line_edit_salario.setPlaceholderText('555.55')
        self.line_edit_salario.setFixedHeight(40)

        self.label_departamento = QLabel()
        self.label_departamento.setText('Departamento')

        self.line_edit_departamento = QLineEdit()
        self.line_edit_departamento.setFixedHeight(40)

        self.button_salvar = QPushButton()
        self.button_salvar.setText('Salvar')
        self.button_salvar.clicked.connect(self.salvar)

        self.table_funcionarios = QTableWidget()
        self.table_funcionarios.setColumnCount(4)
        self.table_funcionarios.setHorizontalHeaderLabels(['Nome', 'Sexo', 'Salario', 'Departamento'])
        self.table_funcionarios.setRowCount(0)

        space = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Expanding)

        layout = QVBoxLayout()
        layout.addWidget(self.label_mensagem)
        layout.addWidget(self.label_nome)
        layout.addWidget(self.line_edit_nome)
        layout.addWidget(self.label_sexo)
        layout.addWidget(self.combo_box_sexo)
        layout.addWidget(self.label_salario)
        layout.addWidget(self.line_edit_salario)
        layout.addWidget(self.label_departamento)
        layout.addWidget(self.line_edit_departamento)
        layout.addWidget(self.button_salvar)
        layout.addWidget(self.table_funcionarios)
        layout.addItem(space)

        self.componentes = QWidget()
        self.componentes.setLayout(layout)

        self.setCentralWidget(self.componentes)

        self.setWindowTitle('Meu primeiro formulário com PyQt5')
        self.setGeometry(20, 20, 800, 400)

        self.popular_tabela()

    def salvar(self):
        funcionario = Funcionario()
        funcionario.nome = self.line_edit_nome.text()
        funcionario.sexo = self.combo_box_sexo.currentText()
        funcionario.departamento = self.line_edit_departamento.text()
        funcionario.salario = float(self.line_edit_salario.text())
        funcionario.cadastrar()
        self.label_mensagem.setVisible(True)
        self.label_mensagem.setText('Cadastrado com sucesso!')
        utils.limpar_components(self.componentes)
        self.popular_tabela()
        self.limpar_mensagem()

    def limpar_mensagem(self):
        self.timer = QTimer(self)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(lambda: self.label_mensagem.hide())
        self.timer.start()

    def popular_tabela(self):
        items = Funcionario.listar()
        self.table_funcionarios.setRowCount(len(items))

        for linha, funcionario in enumerate(items):
            nome = QTableWidgetItem()
            nome.setText(funcionario.nome)

            sexo = QTableWidgetItem()
            sexo.setText(funcionario.sexo)

            sexo = QTableWidgetItem()
            sexo.setText(funcionario.sexo)

            salario = QTableWidgetItem()
            salario.setText(str(funcionario.salario))

            departamento = QTableWidgetItem()
            departamento.setText(funcionario.departamento)

            self.table_funcionarios.setItem(linha, 0, nome)
            self.table_funcionarios.setItem(linha, 1, sexo)
            self.table_funcionarios.setItem(linha, 2, salario)
            self.table_funcionarios.setItem(linha, 3, departamento)
