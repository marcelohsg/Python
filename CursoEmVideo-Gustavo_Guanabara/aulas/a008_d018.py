# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite o valor de um ângulo qualquer: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print(f'O seno de {a} graus é {sen:.2f}')
print(f'O cosseno de {a} graus é {cos:.2f}')
print(f'A tangente de {a} graus é {tg:.2f}')