# Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
x = randint(1, 10)
cont = 0
'''if a == x:
    print(f'O número escolhido foi {x}. VOCÊ GANHOU!')
else:
    print(f'O número escolhido foi {x}. VOCÊ PERDEU!')
print('== FIM ==')'''
a = ''
while a != x:
    a = int(input('Em qual número eu pensei? '))
    if a != x:
        cont += 1
        print('VOCÊ PERDEU!')
        if a < x:
            print('Mais... Tente outra vez!')
        else:
            print('Menos... Tente outra vez!')
print('VOCÊ GANHOU!')
print(f'Você tentou {cont} vezes até acertar.')
