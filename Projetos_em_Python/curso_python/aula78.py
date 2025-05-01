
# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados em matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagram de Venn
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set("Hugo") # Dessa forma, set irá iterar sobre o valor passado, e possivelmente as letras sairão de ordem.
# s1 = set() # set vazio
# s1 = {"Hugo", 1, 2, 3} # set com dados. Assim, a string "Hugo" terá sua ordem preservada, apesar dos outros valores não manterem sua ordem original
# print(s1)


# Sets são eficientes para remover valores duplicados de iteráveis.
# - eles não tem índices;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)
# Sets parecem dicionários porém, eles não possuem chave, somente valor.
# s1 = {1, 2, 3, 3, 3, 3, 3, 1} # Set remove valores duplicados
# l1 = [1, 2, 3, 3, 3, 3, 3, 1] # Lista com valores duplicados
# s1 = set(l1) # Converte a lista em um conjunto, o que irá eliminar valores duplicados
# l2 = list(s1) # Convertendo conjunto de volta a uma lista, só que agora sem valores dupliacdos

# s1 = {1, 2, 3}
# print(3 in s1)
# print(4 in s1)

# for numero in s1:
#     print (numero)



# Métodos úteis:
# add (adiciona um valor de cada vez)
# s1 = set()
# s1.add("Hugo")
# s1.add(1)

# update (pode adicionar vários valores por vez)
# s1.update(("Olá mundo",1, 2, 3 , 4)) # Mandando os valores dentro de uma tupla, evita-se que a str fique fora de ordem
# clear (limpa o set)
# s1.clear()

# discard (descarta o valor passado para o método)
# s1.discard("Olá mundo")


# print(s1)
# Operadores úteis:
# união | união (union) - Une
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2

print(s3)

# intersecção & (intersection) - Itens presentes em ambos
s4 = s1 & s2

print(s4)

# diferença - Itens presentes apenas no set da esquerda
s5 = s1 - s2

print(s5)

s6 = s2 - s1

print(s6)

# diferença simétrica ^ - Itens que não estão em ambos
s7 = s1 ^ s2

print(s7)
