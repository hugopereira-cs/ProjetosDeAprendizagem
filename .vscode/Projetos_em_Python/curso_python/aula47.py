"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário
digitar apenas uma letra.
Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na 
palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra; se a letra não
estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário."""

import os
palavra_secreta = 'hugo'
letras_acertadas = ''
numero_tentativas = 0
resposta = ''

while True:
    letra_escolhida = input('Escolha uma letra: ')
    numero_tentativas += 1
    
    if len(letra_escolhida) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_escolhida in palavra_secreta:
        letras_acertadas += letra_escolhida

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas: ', numero_tentativas )
        resposta = input('Digite [s]air para encerrar o jogo. ')
        if resposta == 's':
            break    
        letras_acertadas = ''
        numero_tentativas = 0


