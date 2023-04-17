# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
maior = 0
menor = 0
for c in range(1,8):
    ano = int(input(f'Ano de nascimento da {c}º pessoa: '))
    if (2023 - ano) >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já atigiram a maior idade!')
print(f'{menor} pessoas ainda não atingiram a maior idade!')

