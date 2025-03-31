"""
Closure e funções que retornam outras funções.
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!' # Só retornará essa linha, caso já tenha acesso a esses dois parâmetros.
    return saudar # Ao não colocar os parêntes, a função está sendo adiada 

falar_bom_dia = criar_saudacao('Bom dia')
fala_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Hugo']:
    print(falar_bom_dia(nome)) # Colocando os parêntese aqui, indicamos que agora sim, a função pode ser executada
    print(fala_boa_noite(nome))