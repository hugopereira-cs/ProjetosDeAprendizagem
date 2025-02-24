# senha_salva = '12345'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('O laço acima pode ter repetições infinitas.') #while é usado para casos onde não sabemos 
#o número exato de repetições.

#Já para os casos em que sabemos a quantidade exata de repetições que teremos, usamos o for.

frase = 'Python'
novo_texto =''
for letra in frase:#Nesse caso o python já identifica que letra, nessa situação está funcionando como um índice
    novo_texto += f'*{letra}'
    print(letra)#Mas poderia ser qualquer outro nome de variável 
print(novo_texto + '*')
