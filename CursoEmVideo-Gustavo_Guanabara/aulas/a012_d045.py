# Crie um programa que faça o computador jogar jokênpo com você.
from random import choice
lista = ['pedra', 'papel', 'tesoura']
comp = choice(lista)
print('=-'*16)
print('JOGO: PEDRA, PAPEL E TESOURA')
print('=-'*16)
print('''Qual é sua escolha?
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
opcao = int(input('Opção: '))
if opcao == 1:
    print('Você escolheu: Pedra')
    if comp == 'pedra':
        print('O computador escolheu: Pedra')
        print('Resultado: EMPATE!')
    elif comp == 'papel':
        print('O computador escolheu: Papel')
        print('Resultado: Papel ganha Pedra. Você PERDEU!')
    elif comp == 'tesoura':
        print('O computador escolheu: Tesoura')
        print('Resultado: Pedra ganha de Tesoura. Você GANHOU')
elif opcao == 2:
    print('Você escolheu: Papel')
    if comp == 'papel':
        print('O computador escolheu: Papel')
        print('Resultado: EMPATE!')
    elif comp == 'tesoura':
        print('O computador escolheu: tesoura')
        print('Resultado: Tesoura ganha Papel. Você PERDEU!')
    elif comp == 'pedra':
        print('O computador escolheu: Pedra')
        print('Resultado: Papel ganha de pedra. Você GANHOU')
elif opcao == 3:
    print('Você escolheu: Tesoura')
    if comp == 'tesoura':
        print('O computador escolheu: Tesoura')
        print('Resultado: EMPATE!')
    elif comp == 'pedra':
        print('O computador escolheu: Pedra')
        print('Resultado: Pedra ganha Tesoura. Você PERDEU!')
    elif comp == 'papel':
        print('O computador escolheu: Papel')
        print('Resultado: Tesoura ganha de Papel. Você GANHOU')
else:
    print('Opção inválida!!')
