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

    @staticmethod
    def listar():
        with open('db.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            funcionarios = list(map(Funcionario.transformar, linhas))
        return funcionarios

    @staticmethod
    def transformar(linha: str):
        colunas = linha.split(',')
        funcionario = Funcionario()
        funcionario.nome = colunas[0]
        funcionario.sexo = colunas[1]
        funcionario.salario = float(colunas[2])
        funcionario.departamento = colunas[3].replace('\n', '')
        return funcionario
