# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(a, b):
    print(f'A área do terreno é {a*b:.2f}m²')


largura = float(input('Qual a largura do terreno? '))
comprimento = float(input('Qual o comprimento do terreno? '))
area(largura, comprimento)
