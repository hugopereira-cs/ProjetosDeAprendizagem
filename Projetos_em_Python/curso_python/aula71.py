"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
*args é utilizado para passarmos uma quantidade ilimitada de argumentos não nomeados.
A função sum tem a mesma funcionalidade da função passada com *args, porém faz isso tudo com uma só linha de código.
"""
# Lembre-te de desempacotamento:
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


def soma(x, y):
    return x + y

soma1 = soma(2, 2)
print(soma1)

def soma(*args): # *args empacota numeros, tranformando-os em uma tupla
    total = 0
    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10 # Aqui os numeros estão sendo transformados em tupla novamente
# outra_soma = soma(*numeros) # Usando o* antes de numeros, eles serão desempacotados, e estarão prontos para serem utilizados pela função.
# print(outra_soma)


print(sum((1, 2, 3, 4, 5, 6, 7, 78, 10))) # Ela precisa ser passada como uma tupla (por isso os dois parânteses)
print(sum(numeros)) # Utilizando a função sum, e passando a variável numeros, não é necessário fazer o desempacotamento (utilizar o *).