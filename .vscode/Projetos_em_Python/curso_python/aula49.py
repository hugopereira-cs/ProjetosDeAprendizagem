"""
for in com listas
"""

lista = ['Maria', 'Helena', 'Hugo']
lista.append('Suelene')
lista.append('Alan')

i = 0
for nome in lista:
    print(i, nome, type(nome))
    i += 1

# lista = ['Maria', 'Helena', 'Hugo']
# lista.append('Suelene')
# lista.append('Alan')

# indices = range(len(lista))

# for indice in indices:
#     print(indice, lista[indice], type(lista[indice]))