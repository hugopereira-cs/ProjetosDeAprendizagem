"""
https://docs.python.org/pt-br/3/library/stdtypes.html#other-built-in-types
Imutáveis que vimos: str, in, float, bool
"""

string = 'Hugo Pereira'#Não dá para mudar essa string nesta variável.
# outra_variavel = f'{string[:3]}ABC{string[4:]}'#Assim é possível mudar, em outra variável.
# print(string)
# print(outra_variavel)
# print(string.z)#Retorna uma cópia da string com o seu primeiro 
#caractere em maiúsculo e o restante em minúsculo.
print(string.zfill(100))#Completa a string com zeros à esquerda até a string completar
#a quantidade de caracteres passada (neste caso 100).