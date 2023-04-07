# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
real = int(input('Quantos reais você tem R$ '))
dollar = float(input('Digite o valor do cambio do dolar hoje: r$ '))
print(f'Com R$ {real} você pode comprar $ {real/dollar:.2f}')

