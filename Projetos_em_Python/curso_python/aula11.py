"""
Precedência entre operadores aritméticos
1. (n + n)
2. **
3. * / // %
4. + -
"""

conta_1 = 1 + 1 ** 5 + 5 #era para o resultado ser 1024
conta_2 = (1 + 1) ** (5 + 5) #resultado foi o esperado (1024)
print(conta_1, conta_2)