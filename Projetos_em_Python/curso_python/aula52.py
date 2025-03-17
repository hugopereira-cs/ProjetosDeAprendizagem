"""
Tipo tupla (tuples) -> Uma lista imutável
"""
# A tupla é mais eficiente que uma lista, então, se você não deseja alterar uma lista,
# é recomendável criar uma tupla ao invéz de uma lista. 
nomes = ('Maria', 'João', 'Hugo') # Usa-se parênteses, ao invéz de colchetes, para criar uma tupla
# Obs.: Se nada for colocado, deixando os nomes soltos, separados por vígula, também cria-se uma tupla

# Também é possível converter uma tupla em uma lista, ou uma lista em uma tupla:
nomes = list(nomes) # Convertendo uma tuple em uma lista

print(nomes[-1])
print(nomes)

nomes = tuple(nomes) #Convertendo uma lista em uma tupla
print(nomes)