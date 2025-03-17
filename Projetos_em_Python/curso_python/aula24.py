# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 
# H u g o 
#-4-3-2-1

"""nome = 'Hugo'
print(nome[2])
print(nome[-3])

print('go' in nome)
print('pe' in nome)
print(10 * '-')
print('go' not in nome)
print('pe' not in nome)
"""
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')