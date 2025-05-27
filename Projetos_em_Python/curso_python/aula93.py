# Try, except, else e finally
# a = 18
# b = 0
# c = a / b

try: # Tenta executar o código
    a = 18
    b = 0
    # print(b[0])
    print("Linha 1"[1000])
    c = a / b
    print("Linha 2")
except ZeroDivisionError: # trata o erro de divisão por zero
    print("Dividiu por zero")
except NameError: # trata o erro de nome não definido
    print("Nome b não está definido")
except (TypeError, IndexError) as error: # também é possível tratar mais de um erro na mesma linha. as error cria uma variável com a instãncia do erro
    # OBS.: Faz mais sentido tratar um erro de cada vez caso vc queira saber qual erro ecorreu.
    print("TypeError + IndexError")
    print("MSG:", error)
    print("Nome:", error.__class__.__name__) # Mostra especificamente a classe do erro ocorrido
except Exception: # Exception é a classe superior, tarta qualquer erro que possa ocorrer
    print("ERRO DESCONHECIDO.")


print("CONTINUAR")