# Introdução às Generator functions em Python
# generator = (n for n in range (1000000))

# return -> para a execução da função e esta é encerrada
# Generator pausa a função, permitindo que ela seja retomada em algum momento
# Em funções generator, a palavra yield é usada para retornar algo
# Todo generator é um iterator
# def generator(n=0):
#     yield 1 # Pausar
#     # return "ACABOU" # Para a iteração, o que também é feito quando next é chamado em algo que não tem próxio valor; logo, return, neste caso, não é necessário
#     print("Continuando...")
#     yield 2 # Pausar
#     print("Mais uma vez...")
#     yield 3
#     print("Vou terminar")
#     return "ACABOU!!!"


# gen = generator(n=0)
# # print(next(gen)) # Retorna o valor em yield
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))

# # Fazendo isso dinamicamente
# for n in gen:
#     print(n)

# Outro exemplo

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return
        

gen = generator(n=5, maximum=12)
for n in gen:
    print(n)