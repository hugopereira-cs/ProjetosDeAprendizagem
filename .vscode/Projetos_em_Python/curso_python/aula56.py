"""
split e join com list e str
split -> divide uma string
join -> une uma string
"""
# frase = 'Olha só que, coisa interessante'
# lista_frase = frase.split() # Caso nenhum parâmetro seja passado para o split, ele separará a frase nos espaços.
# print(lista_frase)
# Caso queira separar de outra forma, basta passar onde você quer que a quebra seja feita,
# Por exemplo, na vírgula:
# lista_frase2 = frase.split(',')
# print(lista_frase2)
 # O que for passado para o split, não será mostrado.
# Por exemplo, se só passarmos a vírgula, o espaço após ele será mostrado.
# Para que o espaço após a vígula não seja mostrado, basta passar a vírgula seguida por um espaço.

# Outras formas de retirar os espaços é usar os métodos strip, rstrip e lstrip.
# strip -> corta os espaços do começo e do fim.
# rstrip -> corta os espaços da direita.
# lstrip -> corta os espaços da esquerda.

# for i, frase in enumerate(lista_frase2):
#     print(lista_frase2[i].strip())

# Não é recomendável você alterar valores mutáveis como feito acima.
# O correto a fazer é:
frase = '   Olha só que, coisa interessante    '
lista_frase_crua = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())

print(lista_frase)
print(lista_frase_crua)
# Assim você preserva os valores originais das variáveis

# Unindo a frase:
frases_unidas = '-'.join(lista_frase) # O primeiro valor passado (-) é o que irá unir a as frases,
# o segundo, que é passado para o método join, é o conteúdo que você quer unir (lista_frase)
print(frases_unidas)