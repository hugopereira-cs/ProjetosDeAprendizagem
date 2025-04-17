#Inicializando o grafo e representandoo os pesos das arestas
grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2
# print(grafo['inicio'].keys())
# print(grafo['inicio']['a'])
# print(grafo['inicio']['b'])

grafo['a'] = {}
grafo['a']['fim'] = 1

grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5

grafo['fim'] = {}

#Tabela de custos
infinito = float('inf')
custos = {}
custos['a'] = 6
custos['b'] = 2
custos['fim'] = infinito

#Tabela hash para os pais
pais = {}
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['fim'] = None

#Array para registrar os vértices processados
processados = []

#Definindo a função para achar custo mais baixo
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float('inf')
    nodo_custo_mais_baixo = None
    for nodo in custos:
        if custos[nodo] < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custos[nodo]
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo= custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)
