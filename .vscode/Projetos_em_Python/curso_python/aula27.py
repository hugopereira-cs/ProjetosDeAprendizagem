"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: A função len retorna a quantidade de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel)
print(variavel[4])#Mostra o caractere da posição que foi pedida
print(variavel[4:7])#Mostra os caracteres de uma posição até outra
print(variavel[4:8])#O segundo número indica que é pra mostrar o último carctere antes dele.
print(variavel[4:])#Colocando os : e omitindo o final, ele mostrará até o final da string
#começando da posição que foi solicitada.
print(variavel[0:5])
print(variavel[:5])#Omitindo o início, será mostrada a string do início até a posição solicitada

print(len(variavel))

print(variavel[0:9:1])#O último número é o passo, ele indica o número de posições a serem puladas para mostrar a string
#nesse caso, o passo será normal, de 1 em 1.
print(variavel[0:9:2])#De 2 em 2
print(variavel[0:9:3])#De 3 em 3
print(variavel[::-1])#De 1 em 1, porém, na ordem ,ivertida. Omitindo início e fim
print(variavel[-1:-10:-1])#A mesma coisa do exemplo acima, mas passando início e fim