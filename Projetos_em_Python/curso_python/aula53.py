"""
Enumerate -> enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Hugo']
lista.append('João')

# lista_enumerada = enumerate(lista)
# print(next(lista_enumerada)) # Mostra o próximo índice da lista enumerada (que neste caso é o 0)

# Também é possível mostrar a lista enumerada e os índices usando o for:
# for item in lista_enumerada:
#     print(item)

# Após usar esse iterator (lista_enumerada) no for acima, essa lista será esvaziada, ou seja, não dará para usar novamente
# Uma maneira de utilizar esse enumerate mais de uma vez é não jogá-lo em uma variável:
# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):
#     print(item)
# for item in enumerate(lista):  
#     print(item)
# for item in enumerate(lista):
#     print(item)

# Caso o objetivo seja somente usar com um print:
# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)

# É possível separar os valores dentro da tupla (no caso, índice e nome):
for indice, nome in enumerate(lista):
    print(indice, nome)