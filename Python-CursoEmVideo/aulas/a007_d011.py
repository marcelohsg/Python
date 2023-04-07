# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Digite a largura da parede (m): '))
a = float(input('Digite a altura da parede (m): '))

print(f'Sua área é de {l*a} m²')
print(f'A quantidade de tinta necessária para pintá-la será de {(l*a)/2} litros')