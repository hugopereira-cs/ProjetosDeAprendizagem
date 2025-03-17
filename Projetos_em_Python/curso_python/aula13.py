nome = 'Hugo'
altura = 1.75
peso = 75
reais = 100050.55
imc = peso / (altura * altura) #poderia ser peso / altura ** 2 -. sem parenteses, já que a exponenciação teria prioridade sobre a divisão



#f-strings (formatação de strings)
linha_1 = f'{nome} tem {altura:.2f} de altura' #":.2f -> é para mostrar duas casa após a vírgula"

linha_2 = f'pesa {peso} quilos, e seu imc é'

linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)

linha_4 = f'{nome} tem {reais:,.2f} de reais' # ":,.2f -> é para separar um inteiro com vígula (comum em caso de o valor se referir a dinheiro), 
#depois mostrar duas casas após a vírgula"
print(linha_4)