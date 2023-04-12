# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.0 por cada km acima do limite.
vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print(
        f'MULTADO! Você excedeu a velocidade permitida. A multa irá custar R${multa:.2f}')
else:
    print('Você ultrapassou na velocidade permitida!')
