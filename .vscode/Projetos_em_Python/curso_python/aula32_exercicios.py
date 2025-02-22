"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro. 
"""
#numero = input('Digite um número inteiro: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'O {numero_int} é um número par.')
#     else:
#         print(f'O {numero_int} é um némero ímpar.')
# else:
#     print('O número que vc digitou não é um inteiro.')

#Também poderia ser feito com try e except
# try:
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'O {numero_int} é um número par.')
#     else:
#         print(f'O {numero_int} é um némero ímpar.')
# except:
#     print('O número que vc digitou não é um inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, 
baseando-se no horário descrito exiba a saudação apropriada.
Ex.: Bom dia 0-11, Boa tarde 12-17, boa noite 18-23.
"""
# hora = input('Digite a hora em números inteiros: ')

# try:
#     hora_int = int(hora)
    
#     if hora_int >= 0 and hora_int <= 11:
#         print('Bom dia!')
#     elif hora_int >= 12 and hora_int <= 17:
#         print('Boa tarde!')
#     elif hora_int >= 18 and hora_int <= 23:
#         print('Boa noite!')
#     else:
#         print('Você digitou uma hora inválida.')
# except:
#     print('Por favor, digite apenas números inteiros.')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto", se tiver entre 5 e 6 letras escreva "Seu nome é normal".
Maior que 6 escreva "Seu nome é muito grande".
"""

# primeiro_nome = input('Digite seu primeiro nome: ')

# if primeiro_nome != '':
#     primeiro_nome_tamanho = len(primeiro_nome)
#     if primeiro_nome_tamanho > 0 and primeiro_nome_tamanho <= 4:
#         print('Seu nome é curto.')
#     elif primeiro_nome_tamanho > 4 and primeiro_nome_tamanho <= 6:
#         print('Seu nome é normal.')
#     else:
#         print('Seu nome é muito grande.')
# else:
#     print('Vc não digitou seu nome.')

#Outra forma de fazer:
name = input('Digite seu primeiro nome: ')

short_name = len(name) <= 4
average_name = len(name) > 4 and len(name) <= 6
long_name = len(name) > 6

if name.isalpha():
    if short_name:
        print('Seu nome é curto.')
    elif average_name:
        print('Seu nome é normal.')
    elif long_name:
        print('Seu nome é muito grande.')
else:
    print('Vc não digitou seu nome.')