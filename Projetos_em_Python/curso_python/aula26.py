"""
Formatação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF123456789)
.<número de dígitos>f
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^- centro
= - força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')#ABC fica à esquerda usando 10 casas
print(f'{variavel: <10}.')#ABC fica à direita usando 10 casas
print(f'{variavel: ^10}.')#ABC fica centralizado usando 10 casas
"""
Nos casos acima o que vem antes dos sinais é um espaço vazio,
mas poderia ser qualquer outro caracter como o 0 ou o $, por exemplo.
"""
print(f'{1000.4873648123746:0>+10,.1f}') # O sinal de + pede para o programa mostrar o sinal do número(seja esse número negativo ou positivo)
print(f'{-1000.4873648123746:0>+10,.1f}') # O sinal de + pede para o programa mostrar o sinal do número(seja esse número negativo ou positivo)
print(f'{-1000.4873648123746:0>-10,.1f}') # O sinal de -+ pede para o programa mostrar o sinal do número(somente se este número for negativo)
print(f'{1000.4873648123746:0=+10,.1f}') # O sinal de = faz com que o sinal venha antes dos zeros que completarão o número
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}') #Conversion flags veremos mais adiante
