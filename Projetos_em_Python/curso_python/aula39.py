"""
Iterando strings com while
"""
#       01234567891011
nome = 'Hugo Pereira'#strings são iteráveis
#      121110987654321


indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

    # if nome[indice] == ' ':
    #     print(' ')
    #     continue
novo_nome += '*'
print(novo_nome)

print('Acabou!')