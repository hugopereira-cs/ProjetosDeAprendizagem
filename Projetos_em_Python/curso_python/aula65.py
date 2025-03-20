"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def imprimir(a, b, c): # a, b, são parâmetros
#     print(a, b, c)

# imprimir(1, 2, 3) # Valores das variáveis a, b, c. Estes valores são chamados de argumentos.
# imprimir(4, 5, 6) # A cada vez que vc chamar a função, pode fazer isso usando parâmetros diferentes.

def saudacao(nome='Sem nome'): # Pode-se dar valor ao parâmetro já na criação da função. Ela receberá o valor que está na chamada; caso não tenha valor na chamada, ela terá o valor passado na criação (neste caso "Sem nome").
    print(f'Olá, {nome}!')


saudacao('Hugo')
saudacao('Maria')
saudacao('Helena')
saudacao()
