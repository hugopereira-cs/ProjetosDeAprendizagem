"""
Dicionários em Python (tipo dict)
Dicinários são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como "índice" que vimos na lista e podem se tipos imutáveis como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} - ou a classe dict para criar dicionários
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list
"""

pessoa = {
    "nome": "Hugo", 
    "sobrenome": "Pereira", 
    "idade": 18, 
    "altura": 1.8, 
    "endereços": [
        {"rua": "tal tal", "número": 123}, 
        {"rua": "outra rua", "número": 123}
    ]
}

# print(pessoa, type(pessoa))
print(pessoa["nome"])
print(pessoa["sobrenome"])

for chave in pessoa:
    print(chave, pessoa[chave])