def calculadora(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return 'erro na expressão'


while True:
    expression = input('digite a expressao e pressione enter pra calcular: ')
    print(calculadora(expression))
