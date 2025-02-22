"""
1-CONSTANTE = "Variáveis" que não vão mudar
Existe uma convenção que diz que devemos usar sempre letras maiúscula
para criar uma variável que não mudará no código
2-Não colocar muitas condições no mesmo if.
3- Quanto mais afastado da margem o seu  código está (blocos de códigos dentro de outros blocos de códigos),
 mais complexo ele é; e isso não é considerada uma boa prática
"""

velocidade = 61 #Velocidade atual do carro
local_carro = 101 #Local em que o carro está na estrada

RADAR_1 = 60 #Velocidade máxima do radar 1
LOCAL_1 = 100 #Local onde o radar 1 está
RANGE_1 = 1 #A distância onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RANGE_1) and \
    local_carro <= (LOCAL_1 + RANGE_1)#Barra invertida indica que o código continuará na linha seguinte
carro_multado_radar_1 = carro_passou_radar_1 and velocidade > RADAR_1

if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1.')

if carro_multado_radar_1:
    print('Carro multado em radar 1.')