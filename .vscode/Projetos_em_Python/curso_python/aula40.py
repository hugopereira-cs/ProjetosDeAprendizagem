"""Calculadora com while"""


while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-*/): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos números digitados (ou ambos) é (são) inválido(s).')
        continue

    operadores_aceitos = '+-*/'

    if operador not in operadores_aceitos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite somente um operador.')
        continue

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = ', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = ', numero_1_float - numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} = ', numero_1_float * numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = ', numero_1_float / numero_2_float)
    else:
        print('A execução não deveria chegar aqui.')

    sair = input('Vc quer sair? [s]im ').lower().startswith('s')
    if sair is True:
        break