# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada: a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2em2 c) uma contagem personalizada
from time import sleep


def contador(i, f, p):
    if p == 0:
        p = 1
    print('-='*25)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(3)
    if i < f:
        for cont in range(i, f+1, p):
            print(cont, end=' ', flush=True)
            sleep(0.5)
    else:
        for cont in range(i, f-1, -p):
            print(cont, end=' ', flush=True)
            sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*25)
sleep(3)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
