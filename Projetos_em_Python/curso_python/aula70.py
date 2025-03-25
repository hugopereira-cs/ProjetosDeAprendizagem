"""
Retorno de valores das funções (return)
Exitem dois tipos de funções:
Funções que somente executam ações, como é o caso da função print.
Funções que específicas para retornarem valores.
Obs.: return encerra a função.
"""

# A seguinte função retorna um None Type (retorna nada)
# def soma(x, y):
#     print(x + y)

# soma1 = soma(2, 2)
# soma2 = soma(3, 3)

# Caso queira acrescentar, por exemplo, somar soma 1 com soma 2, deve-se definir o retorno da função soma.
def soma(x, y):
    return(x + y)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1 + soma2)

print('--------------------------')

# Até é possível ter dois return dentro de umafunção, desde que seja possível executar apenas um deles:
def adicao(x, y):
    if x > 10: # Dessa maneira, só é possível cair em um desses return
        return 10 
    return x + y

adicao1 = adicao(2, 2)
adicao2 = adicao(3, 3)
print(adicao1 + adicao2)
