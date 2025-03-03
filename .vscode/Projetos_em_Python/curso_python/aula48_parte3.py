"""
Listas em Python
Tipo list - mutável (diferentemente das str, os valores de list podem ser mudados)
Suporta vários valores de qualquer tipo, inclusive, poderia ter uma outra lista
dentro de uma lista
Conhecimentos reutilizaveis - índices e fatiamento
Métodos úteis: 
    append -> adiciona um ítem ao final
    insert -> adiona um ítem no índice escolhido
    pop -> remove do final ou do índice escolhido
    del -> apaga um índice
    clear -> limpa a lista
    extend -> estende a lista
    + -> concatena listas
Create Read Update   Delete
Criar, ler, alterar  apagar = lista[i] (CRUD) 
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Hugo')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear() # Limpa a lista completamente
lista.insert(0, 5) # insert recebe dois argumentos: o primeiro é o índice no
# qual você quer insirir um valor; e o segundo é o próprio valor a ser inserido na lista
#* Não adicionar ítens no início e no meio de uma lista grande, somente no fim.

print(lista)