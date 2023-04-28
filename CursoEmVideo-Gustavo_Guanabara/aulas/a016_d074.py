# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
cont = n1 = n2 = n3 = n4 = n5 = 0
while cont <= 5:
    computador = randint(1,20)
    if cont == 1:
        n1 = computador
    elif cont == 2:
        n2 = computador
    elif cont == 3:
        n3 = computador
    elif cont == 4:
        n4 = computador
    elif cont == 5:
        n5 = computador
    cont += 1
listagem = (n1, n2, n3, n4, n5)

