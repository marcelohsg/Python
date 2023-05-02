# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
maior = menor = 0
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont] 
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('=-'*25)
print(f'Você digitou os valores {valores}')
print(f'O maior valor lido foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor lido foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
 