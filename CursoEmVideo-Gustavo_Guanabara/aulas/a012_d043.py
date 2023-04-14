# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
nome = input('Digite seu nome: ') 
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso/(altura**2)
if imc < 18.5:
    print(f'Olá, {nome}. Seu IMC é {imc:.2f}, você está ABAIXO DO PESO!')
elif imc < 25:
    print(f'Olá, {nome}. Seu IMC é {imc:.2f}, você está no PESO IDEAL.')
elif imc <= 30:
    print(f'Olá, {nome}. Seu IMC é {imc:.2f}, você está com SOBREPESO.')
elif imc <= 40:
    print(f'Olá, {nome}. Seu IMC é {imc:.2f}, você está com OBESIDADE.')
else:
    print(f'Olá, {nome}. Seu IMC é {imc:.2f}, você tem OBESIDADE MÓRBIDA.')