"""
Listas em Python
Tipo list - mutável (diferentemente das str, os valores de list podem ser mudados)
Suporta vários valores de qualquer tipo, inclusive, poderia ter uma outra lista
dentro de uma lista
Conhecimentos reutilizaveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""


#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)

# print(bool([])) falsy (conjunto vazio = falsy - falso)
#prin(lista, type(lista))

#       0     1      2              3    4
#      -5    -4     -3             -2   -1
lista = [123, True, 'Hugo Pereira', 1.2, []]
print(lista[2], type(lista[2]))
# Apesar de ser diferente de string, várias coisas que funcionam com str, também funcionam com list
print(lista[2].upper())

lista[2] = 'Maria'
print(lista[-3]) # Nesse exemplo -3 e 2 são o mesmo índice
print(lista[-3], type(lista[-3]))