#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km foram rodados? '))
d = int(input('Quantos dias permaneceram com o carro? '))
print(f'O preço à pagar pelo aluguel será de R$ {(d*60)+(0.15*km):.2f}')