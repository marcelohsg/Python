# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[m', end='')
    print(c, end=' ')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes.')
if tot == 2:
    print('O número é primo!')
else:
    print('O número NÃO é primo!')
