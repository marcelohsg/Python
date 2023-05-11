# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
grupo = []
temporario = {}
totidade = 0
mulheres = []
maiorIdade = []
while True:
    temporario['nome'] = input('Nome: ')
    while True:
        temporario['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if temporario['sexo'] in 'MF':
            break
        else:
            print('Opção inválida. Tente novamente!')
    temporario['idade'] = int(input('Idade: '))
    totidade += temporario['idade']
    opção = input('Você deseja continuar [S/N]? ').strip().upper()[0]
    print('-='*30)
    grupo.append(temporario.copy())
    if temporario['sexo'] == 'F':
        mulheres.append(temporario.copy())
    if temporario['idade'] >= 18:
        maiorIdade.append(temporario.copy())
    if opção == 'N':
        break
print(f'  - Ao total foram cadastradas {len(grupo)} pessoas')
idadeMedia = totidade/len(grupo)
print(f'  - A idade média foi de {idadeMedia} anos')
print(f'  - As mulheres cadastradas foram: ', end='')
for mulher in mulheres:
    print(f'{mulher["nome"]}', end=' ')
print(f'\n  - Pessoas com maior idade foram: ', end='')
for maior in maiorIdade:
    print(f'{maior["nome"]}', end=' ')
