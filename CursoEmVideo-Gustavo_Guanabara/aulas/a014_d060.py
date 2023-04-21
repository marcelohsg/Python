# Faça um programa que leia um número qualquer e mostre o seu fatorial
'''from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
fatorial = factorial(num)
num2 = num*(num-1)*(num-2)
print(fatorial)'''
num = int(input('Digite um número para calcular seu fatorial: '))
cont = num
f = 1
print(f'O fatorial de {num}! = ', end = '')
while cont>0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f)