def regressiva(i):
    print('i')
    if i <= 1:#Caso-base
        return
    else:
        regressiva(i-1)#Caso-recursivo
