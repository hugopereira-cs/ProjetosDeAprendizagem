# Generator expression, Iterables e Iterators em Python
# Iterable -> tem a responsabilidade de ter os valores
# Iterator -> tem a responsabilidade de saber qual é o próximo valor
# Se tem um método __iter__ no objeto, ele retornará um iterator; logo, ele é um iterable
iterable = ["Eu", "Tenho", "__iter__"]
iterator = iterable.__iter__() # tem __iter__ e __next__ . iter(iterable) teria o mesmo efeito.
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))
# OBS.: O método next sempre atualiza o iterator ao ser chamado. Logo, não é possível solicitá-lo mais vezes do que o iterável suporta, nesse caso 3.