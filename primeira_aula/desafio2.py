# TODO: Dada uma palavra criar um programa para retornar a quantidade de vogais e quantidade de consoantes

text = input('digite a palavra: ')
vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxz'
quant_vogais = 0
quant_consoantes = 0
for t in text.lower():
    if t in vogais:
        quant_vogais += 1
    elif t in consoantes:
        quant_consoantes += 1

print(text)
print('quantidade de vogais: {}'.format(quant_vogais))
print('quantidade de consoantes: {}'.format(quant_consoantes))
