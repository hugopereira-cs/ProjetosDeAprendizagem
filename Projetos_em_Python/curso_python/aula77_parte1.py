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

pessoa = {
    "nome": "Hugo", 
    "sobrenome": "Pereira"
}
# print(len(pessoa))
# print(pessoa.keys())# Mostra as chaves do dicionário
# print(list(pessoa.keys()))# Transforma as dict keys em lista
# print(tuple(pessoa.keys()))# Transforma as dict keys em tupla
# print(list(pessoa.values()))
# print(list(pessoa.items()))


# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa.setdefault("idade", None)# Define a chave idade com o valor None (ou qualquer outro valor)
print(pessoa["idade"])