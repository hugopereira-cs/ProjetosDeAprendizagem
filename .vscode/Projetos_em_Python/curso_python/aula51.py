"""
Introdução ao desempacotamento
"""
# A quantidade de variáveis deve ser igua à quantidade de valores 
# nomes = ['Maria', 'João', 'Hugo']
# nome1, nome2, nome3 = nomes
# print(nome3)

# Em caso de só precisar desempacotar 1 valor, será necessário empacotar o resto da lista.
# Isso é feito com um * que antecede o nome da variável em que o restante da lista será colocada.
# nome1, *_ = ['Maria', 'João', 'Hugo']
# print(nome1, _)

# Em Python há uma convenção que diz que, em caso de criação de uma variável que não será usada,
# usa-se um _ como nome para esta variável. Isso indica para outro desenvolvedor que, a variável está alí porém,
# ela não será usada.

# Em caso de você precisar do nome2:
# _, nome2, *_ = ['Maria', 'João', 'Hugo']
# print(nome2)

# Agora, caso precise apenas do nome3:
_, _, nome3, *_ = ['Maria', 'João', 'Hugo'] # Basta adicionar _ para cada nome que antecede o nome desejado.
print(nome3)