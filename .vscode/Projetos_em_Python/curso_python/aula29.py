"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar (obs.: a sintaxe do código precisa estar correta)
O if não evita erros, ele simplesmente checa a lógica sem exceção.
Enquanto o try/except só tenta executar  e, caso dê algum tipo de erro, ele pula para o except
"""

#print(1234)
#print(456)
#int('a')

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número.')


# if numero_str.isdigit():#A função .isdigit retorna True ou False, ela analisa se o digito é um número 
# #ela retornará False também em casos de números com ponto. 
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número.')
