# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'.
cidade = input('Digite o nome da cidade: ')
cidade = cidade.lower().strip()
analise = 'santo' in cidade
print(f'A cidade começa com "santo" = {analise}')
