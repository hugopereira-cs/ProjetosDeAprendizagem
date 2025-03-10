"""
Desempacotamento em chamadas de métodos e funções
"""
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1   (índices dos valores dentro da lista)
    ['Maria', 'Helena', ], # 0 (índice da lista)
    # 0
    ['Helaine', ], # 1
    # 0       1       2          0  1   2   3   4
    ['Hugo', 'João', 'Eduarda', ],
]

# p, b, *_, ap, u = lista
# print(p, ap, u)

# for nome in lista:
#     print(nome, end=' ') # end= ' ' -> diz que é para terminar o nome com um espaço,
#     # e não com uma quebra de linha com é default.

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista) # Permite passar vários argumentos de uma vez
print(*string)
print(*tupla)
print(salas)
print('----------------------------------------') # Estou usando para separar os exemplos e deixá-los mais compreensíveis.
print(*salas, sep='\n') # O sep='\n faz com que a separação seja feita por lista, e ao final de uma lista, a linha seja quebrada.