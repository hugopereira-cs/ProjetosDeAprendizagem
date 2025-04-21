# Manipulando chaves e valore em dicinários
pessoa = {}

##
##

# Utilizando chave dinâmica
chave = "nome_completo" 
pessoa[chave] = "Hugo"

pessoa["sobrenome"] = "Pereira"


print(pessoa[chave], pessoa["sobrenome"])

# print(pessoa["nome1"]) #Gerará um erro de chave, pois a chave "nome1" não existe.

pessoa[chave] = "Maria" # Sobreescreve a chave

del pessoa["sobrenome"] # Deleta a chave "sobrenome"
print(pessoa[chave])
# print(pessoa["sobrenome"]) # Produzirá um erro de chave (uma excessão que interromperá a execução)

# Para evitar que esse erro de chave ocorra:
if pessoa.get("sobrenome") is None: # Por padrão, esta função já retorna None
    print("Não existe")
else:
    print(pessoa["sobrenome"])