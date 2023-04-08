# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triâmgulo retãngulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt
co = int(input('Digite o cateto oposto: '))
ca = int (input('Digite o cateto adjacente: '))
h = sqrt((co**2)+(ca**2))
print(f'O comprimento da hipotenusa é {h}')