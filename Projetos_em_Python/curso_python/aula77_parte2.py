"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
por - apaga um ítem com a chave especificada (del)
popitem - apaga o último ítem adicionado
update - atualiza um dicionário com outro
"""

d1 = {
    "c1":1,
    "c2": 2,
    "l1": [0, 1, 2],
}
# d2 = d1 # Ao fazer isso, vc está apontando que d2 aponta para o mesmo local de memória que d1.

# d2["c1"] = 1000 # Ao alterar d2, d1 também será alterada.
# print(d1)
# print(d2)

# Para evitar esse problema:
# d2 = d1.copy() # Copia o dicionário d1 para dentro de d2, sendo um novo dicionário

# d2["c1"] = 1000 # Dessa forma, ao modificar d2, d1 não será afetado
# print(d1)
# print(d2)
# OBS.: copy só faz copias rasas (só copia valores imutáveis). Ele fará um link de valores mutáveis para outro dicionário; logo, se algum valor de, por exemplo uma lista, for alterado em um dicionário, essa valor também será alteradono outro.

# Para solucionar esse problema podemos usar o método deepcopy (cópia profunda)
import copy

d2 = copy.deepcopy(d1)

d2["c1"] = 1000
d2["l1"][1] = 999999

print(d1)
print(d2)

