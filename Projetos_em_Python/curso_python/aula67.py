"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter
valores padrão. Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None): # Passando None como valor padrão para z...
    if z is not None: # ...isso permite que, ao receber qualquer valor que não seja None, esse valor será utilizado. Caso z fosse definido como 0, isso não seria possível.
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)

# O uso do None como valor padrão é recomendável para casos onde temos um parâmetro, em uma determinada função, que pode ou não ser enviado.