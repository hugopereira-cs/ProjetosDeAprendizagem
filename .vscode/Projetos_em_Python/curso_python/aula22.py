# Operadores lógicos
# and (e), or (ou), not (não)
# and -> todas as condições precisam ser verdadeiras.
# se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que já vimos)
# 0 0.0 '' False
# Também existe o tipo None que é usado
# para representar um não valor

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# Avaliação de curto circuito
print(True or True)
print(True or False)
print(False or False)
print(0 or False or 0 or 'abc') # Retornará abc

senha = input('Senha; ') or 'Sem senha'
print(senha)

