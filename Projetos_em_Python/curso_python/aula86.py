import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# Dictionary Comprehension e Set Comprehension
produto = {
    "nome": "Caneta Azul",
    "preco": 2.5,
    "categoria": "Escritório",
}

dc = {
    chave: valor.upper() # Transforma os valores em letras maiúsculas...
    if isinstance(valor, str) else valor # ... caso o valor seja um str, caso contrário, mantém o valor original
    for chave, valor in produto.items()
    if chave == "categoria" # Só a chave "categoria" será adicionada (filtro) 
}
p(dc)
# Criando um dicionário a partir de valores de uma lista que se parece com um dicionário
lista = [
    ("a", "valor a"),
    ("b", "valor b"),
    ("c", "valor c"),
]
dc = {
    chave: valor 
    for chave, valor in lista
}
# Também é possível fazer o mesmo por meio da função
print(dict(lista))
# Ou
p(dict(lista))

# Set comprehension
s1 = {i for i in range (10)} # Gerando um set com 10 valores
p(s1)
# Outra maneira:
print(set(range(10)))
# Ou
p(set(range(10)))

