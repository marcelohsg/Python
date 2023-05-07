# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
mega = []
temp = []
print('-'*40)
print('JOGO DA MEGA SENA')
print('-'*40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*4, end='')
print(f' SORTEANDO {jogos} JOGOS ', end='')
print(f'-='*4)
for c in range(0, jogos):
    for cont in range(0, 6):
        num = randint(1, 60)
        while num in temp:
            num = randint(1, 60)
            break
        temp.append(num)
        temp.sort()
    mega.append(temp[:])
    temp.clear()
for c in range(1, jogos+1):
    print(f'Jogo {c}: {mega[c - 1]}')
print('-='*5, end='')
print(' < BOA SORTE > ', end='')
print('-='*5)
