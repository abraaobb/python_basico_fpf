import random

# TODO: Dada uma lista de valores inteiros criar um programa para somar os valores pares e valores impares

numbers = list()
pares = 0
impares = 0

for i in range(20):
    numbers.append(random.randrange(0, 101, 1))

for i in numbers:
    if i % 2 == 0:
        pares += i
    else:
        impares += i

print('os numeros: {}'.format(numbers))
print('total: {}'.format(sum(numbers)))
print('a soma dos pares: {}'.format(pares))
print('a soma dos impares: {}'.format(impares))
