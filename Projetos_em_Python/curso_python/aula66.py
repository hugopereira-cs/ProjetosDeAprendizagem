"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} z={3}', '|', 'x + y + z=,', x + y + z) # Mostra os valores de x e y e o resultado da operação

soma(1, 2, 3)
soma(2, 1, 3) # Os argumentos devem ser passados na ordem dos parâmetros que eles devem ocupar
# Para não precisar se preocupar com a ordem:
soma(y=2, z=3, x=1)
soma(1, y=2, z=3) # A partir do momento que você nomeia um argumento, todos os que vem depois também precisarão ser nomeados
# Obs.: Não é recomendável passar parâmetros nomeados e não nomeados na mesma função, a menos que seja necessário.