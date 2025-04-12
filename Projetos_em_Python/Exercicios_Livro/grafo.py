from collections import deque
fila_de_pesquisa = deque()
grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []
fila_de_pesquisa += grafo['voce']
def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        print(f'Verificando {pessoa}...')
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f'{pessoa} é um vendedor de manga!')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)

    print('Nenhum vendedor de manga encontrado.')
    return False
    
pesquisa('voce')