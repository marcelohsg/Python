# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas a letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúscilas é {nome.lower()}')
n1 = len(nome)
n2 = nome.count(' ')
nome2 = n1-n2
print(f'Seu nome tem ao todo {nome2} letras')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')
