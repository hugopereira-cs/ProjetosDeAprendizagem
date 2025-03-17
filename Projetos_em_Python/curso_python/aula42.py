frase = 'O Python é uma linguagem de programação ' \
'multiparadigma. ' \
'Python foi criado por Guido va Rossum.'

i = 0

quantidade_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    quantidade_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if quantidade_apareceu_mais_vezes < quantidade_atual:
        quantidade_apareceu_mais_vezes = quantidade_atual
        letra_apareceu_mais_vezes = letra_atual
    
    
    print(letra_atual, quantidade_atual)
    i += 1

print('Aletra que apareceu mais vezes foi a letra '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{quantidade_apareceu_mais_vezes}x.')