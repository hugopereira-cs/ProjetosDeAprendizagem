nome = 'Hugo'
altura = 1.75
peso = 75
imc = peso / (altura * altura) #poderia ser peso / altura ** 2 -. sem parenteses, já que a exponenciação teria prioridade sobre a divisão

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos, e seu imc é', imc)