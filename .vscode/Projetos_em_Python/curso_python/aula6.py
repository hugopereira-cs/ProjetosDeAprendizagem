# Conversão de tipo, coerção
# Type convertion, typecasting, coercion
# Tipos imutáveis e primitivos:
# str, in, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool('')) # Campo vazio => falso
print(bool(' ')) # Campo preenchido (mesmo que seja somente um espaço) => verdadeiro
print(str(11) + 'b')