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
    # Solicita uma letra ao usuário, em seguida conta + uma tentativa
    letra_escolhida = input('Escolha uma letra: ')
    numero_tentativas += 1
    
    # Verifica se o usuário realmente digitou somente uma letra
    if len(letra_escolhida) > 1:
        print('Digite apenas uma letra.')
        continue
    
    # Verifica se a letra escolhida pelo usuário está presente na palavra secreta,
    # caso isso ocorra, acrescenta a letra correta junto às outras acertadas previamente
    if letra_escolhida in palavra_secreta:
        letras_acertadas += letra_escolhida

    # Inicia a variável, em seguida adiciona um asterísco no lugar de cada letra 
    # que ainda não foi descoberta pelo usuário
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    # Imprime a palavra formada
    print('Palavra formada: ', palavra_formada)

    # Verifica se todas as letra foram descobertas, em caso positivo,
    # mostra, uma mensagem ao usuário, a palavra secreta e o número de tentativas
    # necessárias para o acerto da palavra
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas: ', numero_tentativas )
        
        # Pergunta ao usuário se ele quer sair, em caso positivo, encerra o jogo
        resposta = input('Digite [s]air para encerrar o jogo. ')
        if resposta == 's':
            break    
        letras_acertadas = ''
        numero_tentativas = 0


