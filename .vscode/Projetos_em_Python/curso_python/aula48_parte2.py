"""
Listas em Python
Tipo list - mutável (diferentemente das str, os valores de list podem ser mudados)
Suporta vários valores de qualquer tipo, inclusive, poderia ter uma outra lista
dentro de uma lista
Conhecimentos reutilizaveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar  apagar = lista[i] (CRUD) 
"""

lista = [10, 20, 30, 40]
numero = lista[2]
print(numero)

# Caso algo na lista seja alterado, essa alteração será feita em todo lugar em que esta lista for referenciada,
# ou seja, o valor antigo será substituído pelo novo
lista[2] = 300
print(lista)

del lista[2] # O índice será apagado, e por consequêcia, o índice 3, passará a ser o índice 2
# Caso tivesse mais elementos nessa lista após o índice deletado, todos eles também seriam movidos
# para um índice anterior 
print(lista)
print(lista[2])

# Dica: evitar mover valores em grandes lista, pois isto exigirá muito do processador, e deixará seu programa mais lento.
# O mais interessante se trantando de movimentos em listas é realizá-los no final dessas listas, fazendo com que poucos valores tenham que ser remanejados 

lista.append(50) # Adicionará o valor ao final da lista
lista.pop() # Remove o último elemento da lista
lista.append(60)
lista.append(70) # append pode ser utilizado quantas vezes for necessário
valor_removido = lista.pop() #Jogando o valor removido em uma variável, para exibí-lo
# Isso pode ser feito porque o pop retorna um valor, permitindo que várias ações sejam realizadas, inclusive jogá-lo em
# em uma variável como foi feito.
print(lista, 'Removido', valor_removido)
lista.pop(1) # É possível remover algum índice específico, basta passar o índice desejado 
#(em listas pequenas, como vimos, devemos evitar fazer isso em lista grandes)
print(lista)
