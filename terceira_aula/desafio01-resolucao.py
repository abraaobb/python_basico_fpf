funcionarios = []


def transformar(linha: str):
    colunas = linha.split(',')
    funcionario = dict()
    funcionario['nome'] = colunas[0]
    funcionario['sexo'] = colunas[2]
    funcionario['salario'] = float(colunas[3])
    funcionario['departamento'] = colunas[4]
    return funcionario


def carregar_funcionarios():
    global funcionarios
    with open('funcionarios.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        funcionarios = list(map(transformar, linhas))


def totalizar(**parametros):
    if 'sexo' in parametros.keys():
        filtrados = filter(lambda funcionario: funcionario['sexo'] == parametros['sexo'], funcionarios)
    elif 'departamento' in parametros.keys():
        filtrados = filter(lambda funcionario: funcionario['departamento'] == parametros['departamento'], funcionarios)
    total = sum(map(lambda funcionario: funcionario['salario'], filtrados))
    return total

def exibir_departamentos():
    departamentos = list(set(map(lambda funcionario: funcionario['departamento'], funcionarios)))
    print('lista dos departamentos')
    print('\,'.join(departamentos))

def exibir_menu():
    print('1 - Adicionar funcionario')
    print('2 - Somar salario dos homens')
    print('3 - Somar salario das mulheres')
    print('4 - Listar todos')
    print('0 - Sair do programa')
    print('-' * 20)


def main():
    carregar_funcionarios()
    while True:
        exibir_menu()
        opcao = int(input('Escolha sua opcao: '))

        if opcao == 0:
            break
        elif opcao == 1:
            funcionarios.append(cadastrar_funcionario())
        elif opcao == 2:
            total = totalizar(sexo='Masculino')
            print(f'Soma do salário dos homens {total}')
        elif opcao == 3:
            total = totalizar(sexo='Feminino')
            print(f'Soma do salário das mulheres {total}')
        elif opcao == 4:
            print(', '.join(map(lambda funcionario: funcionario['nome'], funcionarios)))
        else:
            print('opcao inválida')


main()
