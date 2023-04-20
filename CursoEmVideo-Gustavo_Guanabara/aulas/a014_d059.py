# Crie um programa que leia dois valores e mostre um menu como o ao lado da tela: Seu programa deverá realizar a operação solicitada em cada caso [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos números\n [5] Sair do programa')
    escolha = int(input('>>>>>>> Qual é sua escolha? '))
    if escolha == 1:
        print(f'O resultado de {n1} + {n2} = {n1+n2}')
    elif escolha == 2:
        print(f'O resultado de {n1} x {n2} = {n1*n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O {n1} é MAIOR que {n2}!')
        elif n1 < n2:
            print(f'O {n2} é MAIOR que {n1}!')
        else:
            print('Os números são iguais!')
    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('FIM DO PROGRAMA')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-' * 15)
