"""
Função lambda em Python
A função lambda é uma função como qualquer outra em Python. Porém, são funções anônimas que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
"""

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort() # .sort pode ser usado para ordenar uma listas que coisas que o Python não consegue ordenar
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# Recebe os itens do dicionário "lista" e retorna a chave (key) "nome"
# def ordena(item):
#     return item["nome"]

# Recebe a key retornada pela função "ordena" e ordena o dicionário por nome.
# lista.sort(key=ordena)

# A função lambda tem a mesma utilidade, porém, com menos linhas de código

# lista.sort(key=lambda item: item["nome"]) #sort reorganiza a lista


def exibir(lista):
    for item in lista:
        print(item)
    print()

# Cria duas listas rasas, uma ordenada por nome, e outra por sobrenome
l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])


exibir(l1)
exibir(l2)
