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

p1 = {
    "nome": "Hugo",
    "sobrenome": "Pereira",
}
# print(p1["nome"])# Mostra o conteúdo da chave nome. Caso não exista, gerará um erro.
# print(p1.get("nome", "Não existe"))# Mostra o conteúdo da chave nome. Caso não exista, mostrará "Não existe"

# nome = p1.pop("nome")# Passa o valor da chave "nome" para a variável nome, mas elimina a chave do dicionário
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()# Remove a última chave do dicionário
# print(ultima_chave)
# print(p1)

#O método update atualiza e/ou cria novas chaves e valores de um dicionário
#Existem 3 formas de implementar o método update:
#Primeira forma:
# p1.update({
#     "nome": "novo valor",
#     "idade": 30,
# })

#Segunda forma:
# p1.update(nome="novo valor", idade=30)

#terceira forma:
tupla = (("nome", "novo valor"), ("idade", 30))# Com uma tupla
# lista = [["nome", "novo valor"], ["idade", 30]]# Com lista
p1.update(tupla)# Ou p1.update(lista) para usar com uma lista
print(p1)
