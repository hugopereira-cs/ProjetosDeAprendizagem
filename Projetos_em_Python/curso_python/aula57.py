"""
Lista dentro de lista
(Poderia ser quaquer outro iterável dentro de outro)
"""

# salas = [
#     # 0        1   (índices dos valores dentro da lista)
#     ['Maria', 'Helena', ], # 0 (índice da lista)
#     # 0
#     ['Helaine', ], # 1
#     # 0       1       2          0  1   2   3   4
#     ['Hugo', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # 2
# ]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])


# Usando o for:
salas = [
    # 0        1   (índices dos valores dentro da lista)
    ['Maria', 'Helena', ], # 0 (índice da lista)
    # 0
    ['Helaine', ], # 1
    # 0       1       2          0  1   2   3   4
    ['Hugo', 'João', 'Eduarda', ], # 2
]

for sala in salas:
    print(sala)
    for aluno in sala:
        print(aluno)