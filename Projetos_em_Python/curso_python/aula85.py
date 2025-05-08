import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# Adicionando dois valores em uma lista
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y)) # Para adicionar dois valores em um único índice, é preciso tranformá-la em uma tupla, por isso os dois parênteses



# List comprehension com mais de um for
lista = [
    (x, y) # Para adicionar dois valores em um único índice, é preciso tranformá-la em uma tupla, por isso os dois parênteses

    for x in range(3)
    for y in range(3)
]

# Criando uma list comprehension dentro de um valor de uma list comprehension
lista = [
    [(x, letra) for letra in "Hugo"]
    for x in range(3)
    
]  
p(lista)