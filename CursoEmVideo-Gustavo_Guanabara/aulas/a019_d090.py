# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*30)
print(f'- O nome é igual a {aluno["nome"]}')
print(f'- Média é igual a {aluno["media"]}')
if aluno['media'] < 7:
    print('- Situação é igual a recuperação!')
elif aluno['media'] < 4:
    print('- Situação é igual a reprovado!')
else:
    print('- Situação é igual a aprovado!')