#Estados a abranger
estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

#Estações a serem escolhidas
estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

#Variável para armazenar o conjunto final de estações
estacoes_finais = set()

#Escolhe a estação que cobre o maior número de estados não cobertos
while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados in estacoes.items():
        cobertos = estados_abranger & estados 
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    estados_abranger -= estados_cobertos
    estacoes_finais.add(melhor_estacao)

print(estacoes_finais)