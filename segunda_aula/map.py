frutas = [
    {'nome': 'maçã', 'is_vermelha': True},
    {'nome': 'pessego', 'is_vermelha': False},
    {'nome': 'laranja', 'is_vermelha': False},
    {'nome': 'morango', 'is_vermelha': True},
    {'nome': 'cereja', 'is_vermelha': True},
]


# teste = lambda argumento: argumento == 10
# print(teste(11))

def is_vermelha(condicao):
    return condicao


print(frutas)

frutas_vermelhas = filter(lambda param: param['is_vermelha'], frutas)
valores = map(lambda param: param['nome'], frutas_vermelhas)
print(list(valores))
