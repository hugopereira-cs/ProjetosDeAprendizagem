"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    name = input('Digite seu nome: ')
    print(f'Seu nome é {name}')

    if (name.casefold()) == 'sair':
        break

print('Acabou!')
