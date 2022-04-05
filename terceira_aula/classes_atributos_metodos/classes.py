from datetime import date, datetime


class Funcionario:
    def __init__(self, nome=None, sexo=None, salario=None, data_aniversario=None):
        self.nome = nome
        self.sexo = sexo
        self.salario = salario
        self.data_aniversario = data_aniversario

    def cadastrar(self):
        pass

    def listar(self):
        pass

    @property
    def idade(self):
        agora = datetime.now().date()
        diff = agora - self.data_aniversario
        return int(diff.days / 365)


f1 = Funcionario(nome='Abraão', sexo='M', salario=1000, data_aniversario=date(1995, 10, 7))
print(f'{f1.nome} - {f1.data_aniversario}')
print(f1.idade)
