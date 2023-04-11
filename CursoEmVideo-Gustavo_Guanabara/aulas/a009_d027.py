# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome  separadamente
# Ex: Ana Maria de Souza
# primeiro: Ana
# último: Souza
nome = input('Digite seu nome completo: ').strip()
analise = nome.rfind(' ')
print(f'Primeiro: {nome.split()[0]}')
print(f'Último: {nome[ analise + 1:]}')
