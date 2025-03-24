"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

x = 1 # Valor global de x

def escopo(): # Definindo função escopo
    x = 10 # Valor local de x. x pode ser usado por essa função e por outras dentro desta, como outra_funcao, por exemplo.

    def outra_funcao(): # definindo a função local outra_funcao
        y = 2 # Valor local de y. y só pode ser utilizado por esta função ou por alguma que esteja dentro desta.
        print(x, y) # Mostra o valor de x (pega o valor mais próximo a ela, neste caso é 10) e y (que foi definido dentro dela)

    outra_funcao() # outra_funcao é uma função local, portanto, deve ser chamada dentro da função onde está localizada (escopo).
    print(x) # x tem valor 10 dentro da função escopo.


print(x) # Fora da função escopo x tem valor 1
escopo() # Mostra a função escopo, que define um novo valor para x (10) e, define a função outra_funcao, e a executa
print(x) # Fora da função escopo x tem valor 1

# Transformando uma variável local em global:

# x = 1 # Valor global de x

# def escopo(): # Definindo função escopo
#     global x # Definindo o x deste escopo (10) como global (má prática de programação, não é recomendável)
#     x = 10

#     def outra_funcao():
#         y = 2
        
#         print(x, y)

#     outra_funcao()
#     print(x)


# print(x) # x ainda vale 1, pois ele foi alterado na função escopo, e ela não foi executada ainda
# escopo()
# print(x) # Função escopo executada, agora x vale 10