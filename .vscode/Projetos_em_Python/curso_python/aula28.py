"""
Execício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idades forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba "descupe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:#Só entrará nesse bloco caso as duas condições sejam verdadeiras (caso nada for digitado em uma ou em ambas,
    #o bloco não será executado, e a execuçaõ pulará para o bloco else)
    print(f'Seu nome é {nome}')
    print(f'Seu nome  invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')