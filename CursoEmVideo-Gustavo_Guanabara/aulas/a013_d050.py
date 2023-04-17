# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
print('=-'*15)
print('Digite seis números inteiros')
print('=-'*15)
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        cont = cont + 1
        soma = soma + num
print(f'A soma dos {cont} valores pares é igual a {soma}.')
    