class Funcionario:
    def __init__(self, nome=None, sexo=None, salario=None, departamento=None):
        self.nome = nome
        self.sexo = sexo
        self.salario = salario
        self.departamento = departamento

    def cadastrar(self):
        linha = f'{self.nome},{self.sexo},{self.salario},{self.departamento}\n'
        with open('db.txt', 'a') as arquivo:
            arquivo.write(linha)
