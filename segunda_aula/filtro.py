lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def par(num) -> bool:
    return num % 2 == 0


novos = filter(par, lista)
print(list(novos))
