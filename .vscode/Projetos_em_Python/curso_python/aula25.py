"""
Interpolação básica de strings
s - string
d e i - int
f - float
 x e X - Hexadecimal (ABCDEF123456789)
"""

nome = 'Hugo'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))
print('O hexadecimal de %d é %04x' % (1500, 1500)) #Vai completar as casas, que estariam vazias, com 0 ou mais de um 0. Neste caso usará 4 casas.
print('O hexadecimal de %d é %08x' % (1500, 1500))#Mesmo exemplo anterior, porém, usando 8 casas.
