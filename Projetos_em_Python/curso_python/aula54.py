"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valorees de sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista
"""
import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Digite o que você deseja inserir à lista: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice a ser apagado: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um número inteiro.')
        except IndexError:
            print('Esse índice não exite na lista.')
        except Exception:
            print('Erro inesperado.')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('A lista está vazia.')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Você digitou uma opção inválida. Por favor, digite uma das opções válidas')
        