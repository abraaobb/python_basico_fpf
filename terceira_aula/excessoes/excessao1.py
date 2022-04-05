# try:
#     numero = int(input('Digite um numero: '))
#     print(numero)
# except ValueError as ex:
#     print(f'Deu ruim {ex}')

def somar(a, b):
    if a > 10:
        raise Exception('O valor de A é maior')
    return a + b


try:
    resultado = somar(20, 30)
    print(resultado)
except Exception as error:
    print(error)
