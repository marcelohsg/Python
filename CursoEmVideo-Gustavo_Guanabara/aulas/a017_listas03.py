a = [2, 3, 4, 7]
# b = a isso significa que irá criar uma ligação entre as duas listas, logo, se alterar 'b' tbm se altera 'a'.
b = a[:] # Faz uma cópia, logo, se alterar 'b', não altera 'a'.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')