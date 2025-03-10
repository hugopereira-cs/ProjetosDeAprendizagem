"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
# print('Valor' if True else 'outro valor')
# print('Valor' if False else 'outro valor')

# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'outro valor'
# print(variavel)

digito = 9 # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito # A opereção de cima invertida, mas com o mesmo resultado.
print(novo_digito)