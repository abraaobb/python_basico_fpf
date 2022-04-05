class Pessoa:
    def __init__(self, nome=None, endereco=None):
        self.nome = nome
        self.endereco = endereco


class PessoaFisica:
    pass


class Juridica(Pessoa):
    def __init__(self, nome=None, endereco=None, cnpj=None):
        super().__init__(nome=nome, endereco=endereco)
        self.cnpj = cnpj


juridica = Juridica(nome='FPF Tech', endereco='distrito', cnpj='0000.00')
print(juridica.nome)