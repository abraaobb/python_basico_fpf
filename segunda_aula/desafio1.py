frutas = ['maça', 'laranja', 'pessego', 'uva', 'mamao']
regra = ['maça', 'uva', 'pera']


def filtrar_frutas(fruta):
    return fruta in regra


resultado = filter(filtrar_frutas, frutas)
print(list(resultado))

res2 = filter(lambda frutas: frutas in regra, frutas)

print(list(res2))