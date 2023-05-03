# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
listaPar = []
listaImpar = []
while True:
    n = int(input('Digite um valor: '))
    while True:
        r = input('Você quer continuar [S/N]? ').upper().strip()[0]
        if r in 'SN':
            break
        else:
            print('Opção inválida. Tente novamente!')
    lista.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    if r == 'N':
        break
print('-='*25)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')
