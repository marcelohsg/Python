# Crie um programa que leia um nome de uma pessoa e diga se ela tem 'silva' no nome.
nome = input('Digite seu nome completo: ')
nome = nome.strip().lower()
analise = 'silva' in nome
print(f'Seu nome possui "Silva": {analise}')