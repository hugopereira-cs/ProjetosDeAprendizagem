"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(10)#Quando só é passado um valor, esse valor é o stop (onde o range termirá - 
#Obs.: em Python ele sempre termirá em um número antes do limite estabelecido pelo range, neste caso no 9)
#Como não foi indicado o start, o range iniciará no 0.
print(numeros[5])
for numero in numeros:
    print(numero)

numeros = range(5, 10)#Dois números representam o ínicio e o fim do range (no caso, de 5 a 9)
#Como o step não foi passado, a contagem será feita de 1 em 1.

for numero in numeros:
    print(numero)

numeros = range(5, 10, 2)#O terceiro número é o step, ele indica como seŕa feita a contagem, neste caso, de 2 em 2.

for numero in numeros:
    print(numero)

numeros = range(0, -10, -1)

for numero in numeros:
    print(numero)