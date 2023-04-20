# Crie um programa que leia dois valores e mostre um menu como o ao lado da tela: Seu programa deverá realizar a operação solicitada em cada caso [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = ''
while escolha != 5:
    print(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos números\n [5] Sair do programa')
    escolha = int(input('>>>>>>> Qual é sua escolha? '))
print('FIM DO PROGRAMA')