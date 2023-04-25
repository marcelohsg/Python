'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
contIdade = contHomem = contMulher = 0
while True:
    print('=-'*15)
    print('CADASTRE UMA PESSOA')
    print('=-'*15)
    idade = int(input('Idade: '))
    sexo = continuar = ' '
    while sexo not in 'MF':        
        sexo = input('Sexo [M/F]: ').upper().strip()[0]        
    while continuar not in 'SN':
        print('=-'*15)
        continuar = input('Você quer continuar [S/N]? ').upper().strip()[0]  
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contHomem += 1
    if sexo == 'F':
        if idade < 20:
            contMulher += 1
    if continuar == 'N':
        print('Fim programa!')
        print('=-'*15)
        break
print(f'A) Pessoas com mais de 18 anos: {contIdade}')
print(f'B) Homens cadastrados: {contHomem}')
print(f'C) Mulheres com menos de 20 anos: {contMulher}')
