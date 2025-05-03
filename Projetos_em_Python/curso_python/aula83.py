# Empacotamento e desempacotamento
# a, b = 1, 2
# a, b = b, a # Invertendo os valores das variávis
# print(a, b)

# Empacotamento e desempacotamento de dicionários

# pessoa = {
#     "nome": "Hugo",
#     "sobrenome": "Pereira",
# }
# a, b = pessoa # Quando nenhum método é passado, ele mostrá as keys
# print(a, b)
# print()

# c, d = pessoa.values()
# print(c, d)
# print()

# # e, f = pessoa.items() # Gerará tuplas com as chaves e valores
# (a1, a2), (b1, b2) = pessoa.items() # Desempacotamento interno baseando-se nos itens contidos no dicionário
# print(a1, a2)
# print(b1, b2)
# # Isso é o mesmo que:
# for chave, valor in pessoa.items():
#     print(chave, valor)


pessoa = {
    "nome": "Hugo",
    "sobrenome": "Pereira",
}

dados_pessoa = {
    "idade": 16,
    "altura": 1.6,
}

# Extrai os conteúdos dos dois dicinários acima e os coloca em um terceiro dicionário
pessoa_completa = {**pessoa, **dados_pessoa} # Dois ** para realizar a extração. Também é possível passar novos valores para esse dicionário, para isso, é só não utilizar os asteríscos.
# print(pessoa_completa)


# args e kwargas
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS:", args) # Mostra os argumentos não nomeados

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(1,2, nome="Joana", qlq=123)

# Desempacotar uma chamada de função passando os argumentos
# mostro_argumentos_nomeados(**pessoa_completa)

# Um outro exemplo de desempacotamento
configuracoes = {
    "arg1": 1,
    "arg2": 2,
    "arg3": 3,
    "arg4": 4,
}
mostro_argumentos_nomeados(**configuracoes)