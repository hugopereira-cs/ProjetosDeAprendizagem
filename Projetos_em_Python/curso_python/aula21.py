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

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# Avaliação de curto circuito
print(True and True and True)

print(True and 0 and True) # Ele considera o 0 como False, mas retornará 0 (e não False), a verificação será encerrada no 0.
print(True and False and True) # Retornará False (a execução será encerrada no False)


