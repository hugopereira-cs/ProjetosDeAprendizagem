"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis
"""
# print(list(range(10))) # Exibeuma lista de 0 a 9

import pprint # O modulo pprint é um print mais bem apresentado e com possibilidade de algumas customizações

def p(v): # Customiza a exibição do pprint
    pprint.pprint(v, sort_dicts=False, width=40)

# Criando e exibindo uma lista
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# Fazendo o mesmo do exemplo acima, mas usando list comprehension
# lista = [numero for numero in range(10)]
# print(lista)

# Um exemplo do que podemos fazer com list comprehension:
lista = [numero * 2 for numero in range(10)] # Dupplica cada número de 0 a 10 e salva cada resultado na lista
# print(lista)

# Mapeamento de dados em list comprehension - Transforma/modifica itens de uma lista para uma outra lista, que terá o mesmo tamanho da lista anterior.
produtos = [
    {"nome": "p1", "preco": 20, },
    {"nome": "p2", "preco": 10, },
    {"nome": "p3", "preco": 30, },
    {"nome": "p4", "preco": 40, },

]
# Cria um novo dicionário para alterar em 5% os preço dos produtos que custam mais do que 20 reais
# novos_produtos = [
#     {**produto, "preco": produto["preco"] * 1.05} # Desempacota o dict antigo para o novo e aumenta os preços em 5%...
#     if produto["preco"] > 20 else {**produto} # somente se o produto custar mais de 20 reais, caso contrário, desempacota o dict antigo, mantendo o preço antigo
#     for produto in produtos
#     ]

# print(*novos_produtos, sep="\n")


# Utilizando filtros
# lista = [n for n in range(10) if n < 5]
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] > 20 else {**produto}
    for produto in produtos
    if (produto["preco"] * 1.05) >= 20
]
p(novos_produtos)