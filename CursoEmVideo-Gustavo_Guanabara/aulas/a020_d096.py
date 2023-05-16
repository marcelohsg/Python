# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(a, b):
    print(f'A área de um terreno {a:.0f}x{b:.0f} é de {a*b:.2f}m².')

print('=-'*15)
print('CONTROLE DE TERRENO')
print('=-'*15)
largura = float(input('Qual a largura do terreno (m)? '))
comprimento = float(input('Qual o comprimento do terreno (m)? '))
area(largura, comprimento)
