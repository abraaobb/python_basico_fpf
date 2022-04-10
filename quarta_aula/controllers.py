from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

import utils
from main import Ui_Main
from models import Funcionario


class MainController(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_salvar.clicked.connect(self.salvar)
        self.lbl_mensagem.hide()
        self.popular_tabela()

    def salvar(self):
        funcionario = Funcionario()
        funcionario.nome = self.edt_nome.text()
        funcionario.sexo = self.cmb_sexo.currentText()
        funcionario.departamento = self.edt_departamento.text()
        funcionario.salario = float(self.edt_salario.text())
        funcionario.cadastrar()
        self.lbl_mensagem.setVisible(True)
        self.lbl_mensagem.setText('Cadastrado com sucesso!')
        utils.limpar_components(self.componentes)
        self.popular_tabela()
        self.limpar_mensagem()

    def limpar_mensagem(self):
        self.timer = QTimer(self)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(lambda: self.lbl_mensagem.hide())
        self.timer.start()

    def popular_tabela(self):
        items = Funcionario.listar()
        self.tbl_funcionarios.setRowCount(len(items))

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

            self.tbl_funcionarios.setItem(linha, 0, nome)
            self.tbl_funcionarios.setItem(linha, 1, sexo)
            self.tbl_funcionarios.setItem(linha, 2, salario)
            self.tbl_funcionarios.setItem(linha, 3, departamento)
