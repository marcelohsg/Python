# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe seu sexo [M/F]: ').upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida. Digite "M" para Masculino ou "F" para Feminino!')
    else:
        print(f'Sexo {sexo} registrado com sucesso!')

