"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palvra global faz uma variável do escopo externo ser a mesma no escopo interno.
"""

x = 1 # Valor global de x

def escopo(): # Definindo função escopo
    x = 10

    def outra_funcao():
        y = 2
        
        print(x, y)

    outra_funcao()
    print(x)


print(x) # x ainda vale 1, pois ele foi alterado na função escopo, e ela não foi executada ainda
escopo()
print(x) # Função escopo executada, agora x vale 10
