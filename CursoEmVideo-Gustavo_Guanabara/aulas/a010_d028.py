# Escreva um programa que faça o computador "pensar" um número inteiro entre 0 e 5 e peça ao usuario tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuario venceu ou perdeu.
from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
a = int(input('Em que número eu pensei? '))
x = randint(1, 5)
if a == x:
    print(f'O número escolhido foi {x}. VOCÊ GANHOU!')
else:
    print(f'O número escolhido foi {x}. VOCÊ PERDEU!')
print('== FIM ==')
