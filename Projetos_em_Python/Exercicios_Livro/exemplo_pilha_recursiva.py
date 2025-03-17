def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)#recursão
        elif item.e_uma_chave():
            print('Achei a chave!')