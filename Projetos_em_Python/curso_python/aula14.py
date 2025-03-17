a = 'A'
b = 'B'
c = 1.1

formato = 'a={} b={} c={}'.format(a, b, c)

print(formato)

# Também funcionaria desse modo aqui:
string = 'a={} b={} c={}'
formato_2 = string.format(a, b, c)

print(formato_2)

# Formatando casas decimais:
string_2 = 'a={} b={} c={:.2f}'
formato_3 = string_2.format(a, b, c)

print(formato_3)