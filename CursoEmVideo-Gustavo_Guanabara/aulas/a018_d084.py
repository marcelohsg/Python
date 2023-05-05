'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoas = []
pessoa = []
maiorPeso = menorPeso = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = pessoa[1]
    else:
        if pessoa[1] > maiorPeso:
            maiorPeso = pessoa[1]
        elif pessoa[1] < menorPeso:
            menorPeso = pessoa[1]        
    pessoas.append(pessoa[:])
    pessoa.clear()
    while True:
        resp = input('Você quer continuar [S/N]? ').strip().upper()[0]
        if resp in "NS":
            break
    if resp == 'N':
        break
if len(pessoas) == 1:
    print(f'Ao total foi cadastrada apenas {len(pessoas)} pessoa!')
else:
    print(f'Ao total foram cadastradas {len(pessoas)} pessoas!')
print(f'O maior peso foi de {maiorPeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorPeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')
print()
    