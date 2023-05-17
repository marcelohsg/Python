# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*valores):
    cont = maior = 0
    print('-='*25)
    print('Analisando os valores passados...')
    for num in valores:
        print(f'{num}', end=' ', flush=True)
        sleep(.5)
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 7, 21, 8, 9, 15)
maior(2,8,7,1)
maior(3,7)
maior(7)
maior()
