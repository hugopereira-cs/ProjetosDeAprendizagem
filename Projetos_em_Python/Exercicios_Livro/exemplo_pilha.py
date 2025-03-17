def procura_chave(caixa_principal):
    pilha = caixa_principal.crie_uma_pilha_para_busca()
    while pilha is not None:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print('Achei a chave!')