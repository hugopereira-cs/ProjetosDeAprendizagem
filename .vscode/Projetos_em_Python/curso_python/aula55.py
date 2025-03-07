"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # Usado, geralmente, quando algum tipo de texto será exibido junto ao número
print(round(numero_3, 2))

# Em caso de números de ponto flutuante muito grandes podemos usar o modo decimal:
import decimal

numero_4 = decimal.Decimal(0.1)
numero_5 = decimal.Decimal(0.7)
numero_6 = numero_4 + numero_5
print(numero_6)
print(f'{numero_6:.2f}')
print(round(numero_6, 2))

# Caso passemos o valor float para a função decimal, podemos obter o resultado preciso, apenas passando os valores como str:
numero_7 = decimal.Decimal('0.1')
numero_8 = decimal.Decimal('0.7')
numero_9 = numero_7 + numero_8
print(numero_9)
print(f'{numero_9:.2f}')
print(round(numero_9, 2))