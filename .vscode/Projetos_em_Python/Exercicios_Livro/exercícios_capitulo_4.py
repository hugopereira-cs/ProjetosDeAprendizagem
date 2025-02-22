"""
Escreva o código para a função soma, vista anteriormente.
"""
# def soma(lista):
#     if lista == []:
#         return 0
#     return lista [0] + soma(lista[1:])

"""
Escreva uma função recursiva que conte o número de itens em uma lista
"""
# def conta(lista):
#     if lista == []:
#         return 0
#     return 1 + conta(lista[1:])

"""
Encontre o valor mais alto em uma lista.
"""
def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max