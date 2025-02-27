"""
COMO FUNCIONA O FOR POR TRÁS DOS PANOS
Iterável -> str, range etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entrege o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Hugo') #.__iter__()
# print (texto)
# """
# Quando é usado a funão iter (ou .__iter__) pode-se usar a função next para entregar o próximo valor
# """
# print(next(texto))#.__next__()
# print(next(texto))#.__next__()
# print(next(texto))##.__next__()
# print(next(texto))#.__next__()
# #Se passar o número máximo de valores, um erro será levantado. Por exemplo,
# #  caso tivesse 5 linhas solicitando  a função next em uma variável de somente 4 valore


#for letra in texto:
texto = 'Hugo' # iterável
iterador = iter(texto) # iterator(iterador)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

"""
Assim é o funcionamento do for, reconhece quem é o iterável, que nesse caso é texto,
em seguida solicita, para o iterável, o objeto iterador dele;a seguir, ele solicita o next até que o erro StopIterator seja 
acionado(quando o limite de valores for excedido), iss irá sinalizar para o for que ele deve interromper a iteração.
"""

for letra in texto: # O código acima representa o funcionamento deste for por trás dos panos.
    print(letra)