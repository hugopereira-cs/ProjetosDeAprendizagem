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

lista_a = [1, 2, 3]
lista_b = [4, 5 ,6]
lista_c = lista_a + lista_b
print(lista_c)
lista_a.extend(lista_b) # Este método retorna um não-valor, pois ele interfere diretamente no 
# objeto onde ele foi chamado; como neste caso, onde ele extende os valores da lista a com os
# valore da lista b
# lista_d = lista_a.extend(lista_b) # Isso retornará um não-valor
print(lista_a)