# TODO: Criar um programa para adicionar funcionarios. Os funcionarios devem ter nome, sexo e esalaroio. O programa deve retornar a soma de salarios dos homens e a soma do salario das mulheres

funcionarios = list()
soma_masc = 0
soma_fem = 0
while True:
    print("""[1] - adicionar funcionarios
[2] - mostrar soma dos salarios""")
    op = int(input('digite uma opcao: '))
    if op == 1:
        funcionario = dict()
        funcionario['nome'] = input('Digite o nome: ')
        funcionario['sexo'] = input('Digite o sexo: ')
        funcionario['salario'] = float(input('Digite o salario: '))
        funcionarios.append(funcionario)
    elif op == 2:
        for f in funcionarios:
            if f.get('sexo') == 'masculino':
                soma_masc += f.get('salario', 0)
            else:
                soma_fem += f.get('salario', 0)
        break
    else:
        print('opcao invalida')

print(funcionarios)
print('salarios dos homens: R${}'.format(soma_masc))
print('salario das mulheres: R${}'.format(soma_fem))
