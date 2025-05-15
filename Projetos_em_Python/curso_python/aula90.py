# Generator expression, Iterables e Iterators em Python
# Iterable -> tem a responsabilidade de ter os valores
# Iterator -> tem a responsabilidade de saber qual é o próximo valor
# Se tem um método __iter__ no objeto, ele retornará um iterator; logo, ele é um iterable
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iterable.__iter__() # tem __iter__ e __next__ . iter(iterable) teria o mesmo efeito.
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# OBS.: O método next sempre atualiza o iterator ao ser chamado. Logo, não é possível solicitá-lo mais vezes do que o iterável suporta, nesse caso 3.

# Generators são funções que sabem pausar em determinada ocasião
# Todo generator é também um iterator, mas o iterator não é um generator

import sys # Para usar o getsizeof - mostra o tamanho da lista e do generator, em KBs
lista = [n for n in range(100)] # iterator slava todos os valores
generator = (n for n in range(100)) # Enquanto o generator não salva todos os valores na memória, entregando somente um valor por vez
print(sys.getsizeof(lista))
print(sys.getsizeof(generator)) # Logo, o generator economiza bastante espaço em memória em relação ao iterator
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# A grande vantagem das listas é que é possível acessar qualquer índice dela, já com o generator, isso não é possível