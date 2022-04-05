# 1 - Cadastrar funcionario
# 2 - Total de salarios dos homens
# 3 - Total de salarios das mulheres
# 4 - Listar todos os funcionarios
# 5 - Total de salarios por departamento
#     -> Exibir todos os departamentos
#     -> Escolher um departamento
#     -> Total de salario de departamento por Treinador é 9000
# 0 - sair

def get_all_employees():
    f = open("employee.txt", "r")
    db = list()
    for x in f:
        t = x.replace('\n', '')
        t = t.split(',')
        db.append(t)
    f.close()
    return db


def list_employee():
    employees = get_all_employees()
    for e in employees:
        print('-' * 20)
        print("""Nome: {} {}
Sexo: {}
Departamento: {}
Salario: R${}""".format(e[0], e[1], e[2], e[4], e[3]))


def get_departments():
    employees = get_all_employees()
    departments = list()
    for e in employees:
        if e[4] not in departments:
            departments.append(e[4])
    departments.sort()
    return departments


def get_department():
    departments = get_departments()
    for i, d in enumerate(departments):
        print('{} - {}'.format(i, d))
    op = int(input('digite o numero do departamento: '))
    return departments[op]


def add_employee():
    a = open("employee.txt", "a")
    employee = list()
    employee.append(input('Digite o nome: '))
    employee.append(input('Digite o sobrenome: '))
    employee.append(get_gender())
    employee.append(input('Digite o salario: R$'))
    employee.append(input('Digite o departamento: '))
    e = ','.join(employee)
    e = '\n{}'.format(e)
    a.write(e)
    a.close()


def get_gender():
    while True:
        gender = input('M - Masculino\nF - Feminino\nDigite o sexo: ').lower()
        if gender == 'm':
            gender = 'Male'
            return gender
        elif gender == 'f':
            gender = 'Female'
            return gender
        else:
            print('sexo inválido!')


def sum_salary_gender2(gender):
    employees = get_all_employees()
    salary = list()
    for e in employees:
        if e[2] == gender:
            salary.append(float(e[3]))
    msg = 'o total do salario pelo sexo {} é R${}'.format(gender, format(salary, '.2f'))
    print(msg)


def sum_salary_gender(gender):
    employees = get_all_employees()
    salary = sum([float(s[3]) for s in employees if s[2] == gender])
    msg = 'o total do salario pelo sexo {} é R${}'.format(gender, format(salary, '.2f'))
    print(msg)


def sum_salary_department():
    department = get_department()
    employees = get_all_employees()
    salary = sum(float(s[3]) for s in employees if s[4] == department)
    msg = 'o total de salario do departamento {} é R${}'.format(department, format(salary, '.2f'))
    print(msg)


def menu():
    print("""1 - Cadastrar um funcionario
2 - Total de salario dos homens
3 - Total de salario das mulheres
4 - Listar todos os funcionarios
5 - Total de salario por departamento
6 - Encerrar o programa""")
    op = int(input('digite uma opção: '))
    return op


def run():
    while True:
        op = menu()
        if op == 1:
            add_employee()
        elif op == 2:
            sum_salary_gender('Male')
        elif op == 3:
            sum_salary_gender('Female')
        elif op == 4:
            list_employee()
        elif op == 5:
            sum_salary_department()
        elif op == 6:
            break
        else:
            print('opção inválida')


run()
