"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Hugo'
# noutra_variavel = nome
# nome = 'João'
# print(nome)
# print(noutra_variavel)

lista_a = ['Hugo', 'Maria']
# lista_b = lista_a # Isso diz que, tanto lista quanto lista b, apontam para 'Hugo' e 'Maria'
# Caso qualquer uma das listas seja modificada, a mudança também acontecerá na outra
# Para realmente copiar o conteúde de uma variável para outra, usa-se o seguinte método:
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'

print(lista_a)
print(lista_b)
