# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total



multiplicacao = multiplica(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(multiplicacao)