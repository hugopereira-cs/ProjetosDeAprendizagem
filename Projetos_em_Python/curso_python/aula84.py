"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas a partir de iteráveis
"""
# print(list(range(10))) # Exibeuma lista de 0 a 9

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
print(lista)