# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.5 por km para viagem até 200km e R$0.45 para viagens mais longas.
dist = float(input('Qual a distância da sua viagem: '))
if dist <= 200:
    valor = dist * 0.5
    print(f'O preço da passagem será de R${valor:.2f}')
else:
    print(f'O preço da passagem será de R${(dist*0.45):.2f}')
