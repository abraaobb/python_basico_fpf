# arquivo = open('texto.txt', 'w+')
# arquivo.write('Meu primeiro arquivosss')
# arquivo.close()

arquivo = open('texto.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
