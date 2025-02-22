# if/ elif    / else
#se/ se não se/ se não
#elif e else são complementos do if
#elsif pode ser usado mais de uma vez
#else é sempre usado no último caso, sempre encerrando a sequência

entrada = input('Você que "entrar" ou "sair"? ')
if entrada =='entrar':
    print('Vocẽ entrou no sistema')
elif entrada =='sair':
    print('Você saiu do sistema')
else:
    print('Sua entrada não é válida')

print('fora dos BLOCOS')