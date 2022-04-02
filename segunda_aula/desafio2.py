# 1 - Cadastrar funcionario
# 2 - Total de salario dos homens
# 3 - Total de salario das mulheres
# 4 - Listar todos
# 0 - Sair

def cadastrar_funcionario():
    funcionario = dict()
    funcionario['nome'] = input('digite o nome: ')
    funcionario['sexo'] = input('m - masculino\nf - feminino\ndigite uma das opções: ')
    funcionario['salario'] = float(input('digte o salario: '))
    return funcionario


def total_salario(sexo: str, args: list):
    funcionario = filter(lambda funcionario: funcionario['sexo'] == sexo, args)
    salarios = map(lambda funcionario: funcionario['salario'], funcionario)
    return sum(salarios)


def listar_todos(args: list):
    for a in args:
        print('Nome: {}'.format(a['nome']))
        print('Sexo: {}'.format(a['sexo']))
        print('Salário: R${}'.format(a['salario']))
        print('-' * 20)


def imprimir_salarios(funcionarios: list, mensagem: str, sexo: str):
    soma = total_salario(sexo=sexo, args=funcionarios)
    print('o total do salarios d{}: R${}'.format(mensagem, soma))


def menu():
    print("""1 - Cadastrar funcionario
2 - Total de salario dos homens
3 - Total de salario das mulheres
4 - Listar todos
0 - Sair""")
    opcao = int(input('digite uma das opções acima: '))
    return opcao


def run():
    funcionarios = list()
    while True:
        op = menu()
        if op == 1:
            funcionario = cadastrar_funcionario()
            funcionarios.append(funcionario)
        elif op == 2:
            imprimir_salarios(funcionarios=funcionarios, mensagem='os homens', sexo='m')
        elif op == 3:
            imprimir_salarios(funcionarios=funcionarios, mensagem='as mulheres', sexo='f')
        elif op == 4:
            listar_todos(funcionarios)
        elif op == 0:
            print('encerrado programa')
            break
        else:
            print('opcao inválida tente novamente')


run()
