# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# A média de idade do grupo:
# Qual o nome do homem mais velho:
# Quantas mulheres tem menos de 20 anos:
somaidade = 0
mediaIdade = 0
maioridadehomem = 0
nomevelho = ''
cont = 0
for c in range(1, 5):
    print(f'----- {c}º PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        cont = cont + 1 
mediaIdade = somaidade/4    
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'No grupo so existe {cont} mulher com menos de 20 anos.')

