# dir, hasattr e getattr em Python
# dir -> Na área DEBUG CONSOLE, utilizando, por exemplo, dir(string), ele irá mostrar os métodos presentes naquela string
# hasattr -> checa se um determinado objeto tem um determinado nome (método) dentro
string = "Hugo"

# print(string)

# if hasattr(string, "upper"): # Se a string tem o método upper, printa que ele existe e a string com letras maiúsculas. OBS.: o nome do método prexisa ser passado como string
#     print("Existe upper")
#     print(string.upper())

# Outro modo de fazer:
metodo = "upper"

if hasattr(string, metodo):
    print(f"Existe {metodo}")
    print(getattr(string, metodo)())
else:
    print("Não existe o método", metodo)