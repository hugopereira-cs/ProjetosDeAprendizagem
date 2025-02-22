# Operador lógico not
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')
if not senha:
    print('Você não digitou nada.')

senha2 = input('Senha: ')
if senha2 != '123456':
   print('Senha incorreta.')

print(not True)
print(not False)
print(not 0)
print(not 1)
