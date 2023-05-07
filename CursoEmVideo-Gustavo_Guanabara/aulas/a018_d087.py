'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPar = maior = somar3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        somar3 += matriz[l][2] 
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma de todos os valores pares da matriaz é {somaPar}.')
print(f'A soma dos valores da terceira coluna é {somar3}.')
maior = matriz[1][0]
if matriz[1][c] > maior:
    maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')