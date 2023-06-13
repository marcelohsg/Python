# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

valor = float(input('Digite um valor: R$'))
met = moeda.metade(valor)
dobrar = moeda.dobro(valor)
print(f'A metade de {valor} é {met}')
print(f'O dobro de {valor} é {dobrar}')
print(f'Aumentando em 10%, temos {moeda.aumentar(valor)}')
