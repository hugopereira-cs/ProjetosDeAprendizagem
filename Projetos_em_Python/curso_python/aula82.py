def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

# Usando a função lambda para obter mesmo resultado da função soma
print(executa(lambda x, y: x + y, 2, 3)) # Executa a função lambda com os valores 2 e 3


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# Recriando a função cria_multiplicador com a função lambda
duplica = executa(lambda m: lambda n: n * m, 2)

print(duplica(2))




# lambda é utilizada para simplificar um código, por isso os paâmetros com apenas uma letra são comuns.
# Sempre que um função lambda não fica simples, considere se realmente a função lambda é a melhor escolha.

# lambda também aceita *args
print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))



