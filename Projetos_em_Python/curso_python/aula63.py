"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitosdo CPF
MAIS O PRIMEIRO DÍGITO
multiplicando cada um dos valores por uma
contagem regressiva começando de 11.

Ex.: 746.824.890-70 (746824890)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7
   77 40  54 64 14 24 40 36 0  14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
301 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
Caso contrário:
    resultado é o valor da conta

O primeiro dígito do CPF é 0
"""

# cpf = '85970587060'
# dez_digitos = cpf[:10]
# contador_regressivo = 11
# resultado_digito_2 = 0

# for digito in dez_digitos:
#     resultado_digito_2 += (int(digito) * contador_regressivo)
#     contador_regressivo -= 1
# digito_2 = (resultado_digito_2 * 10) % 11
# digito_2 = digito_2 if digito_2 <= 9 else 0

# print(digito_2)

# Gerando os dois dígitos:
# cpf_enviado_usuario = '63861515008'.replace('.', '').replace('-', '').replace(' ', '')
import re # re significa regular expression
import sys

entrada = input('CPF: ')
cpf_enviado_usuario = re.sub(r'[^0-9]','', entrada) # O primeiro parâmetro a ser passado deve ser o que será substituído (neste caso, tudo que não for número).
# Em seguida, pelo quê substituir. Por último, onde aplicar esta função.

entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += (int(digito)) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += (int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


# Verificando se o cpf é válido:
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido.')
else:
    print(f'{cpf_enviado_usuario} é inválido.')