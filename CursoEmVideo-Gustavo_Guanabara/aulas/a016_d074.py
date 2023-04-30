# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
'''FORMA TRADICIONAL!
cont = n1 = n2 = n3 = n4 = n5 = maior = menor = 0
while cont <= 5:
    computador = randint(1,20)
    if cont == 1:
        n1 = computador
        maior = menor = computador
    else:
        if computador > maior:
            maior = computador
        if computador < menor:
            menor = computador        
    if cont == 2:
        n2 = computador
    if cont == 3:
        n3 = computador
    if cont == 4:
        n4 = computador
    if cont == 5:
        n5 = computador   
    cont += 1
listagem = (n1, n2, n3, n4, n5)
print(f'Números gerados: {listagem}')
print(f'O MAIOR número gerado foi {maior}.')
print(f'O MENOR número gerado foi {menor}.')'''
num = (randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20))
print('Os valores soteados foram: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(num)}.')
print(f'O menor número sorteado foi {min(num)}.')
