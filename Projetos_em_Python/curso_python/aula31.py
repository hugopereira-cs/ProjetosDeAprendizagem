"""
Flag (Bandeira) - Maracr um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

v1 = 'a'
v2 = 'a'
v3 = 'A'
print(id(v1))# Mostra a identidade do valor v1 na memória
print(id(v2))# Como o conteúdo das variáveis é igual, 'a' no caso,
#ele mostrará a mesma identidade, mesmo sendo variáveis diferentes.
#Porém, se uma delas for mudada para um valor diferente,
#sua identidade irá mudar.
print(id(v3))
