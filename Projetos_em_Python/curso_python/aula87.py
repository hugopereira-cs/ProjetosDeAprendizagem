# isinstance - para saber se o objeto é de determinado tipo
lista = [ "a", 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {"nome": "Hugo"}]

for item in lista:
    if isinstance(item, set): # Verifica se o item é um set
        print("SET")
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str): # Se o item for str, imprime o item com letra maiúscula, sem modificar a lista
        print("STR")        
        print(item.upper())

    elif isinstance(item, (int, float)): # Se o item for int ou float, o item será mostrado  e será multiplicado por 2, com o resultado também sendo mostrado
        print("NUM")        
        print(item, item * 2)
    else:
        print("OUTRO")
        print(item)




#Obs.: Tentar sempre criar uma lista com um único tipo de valor
