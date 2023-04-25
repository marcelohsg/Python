# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
print('=-'*15)
print('Vamos jogar PAR ou ÍMPAR')
print('=-'*15)
from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar [P/I]? ').upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print("Você PERDEU!")
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')