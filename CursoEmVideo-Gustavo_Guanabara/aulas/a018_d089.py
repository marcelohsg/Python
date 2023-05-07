# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = []
lista = []
while True:
    nome = str(input('Nome: '))
    lista.append(nome)
    n1 = float(input('Nota 1: '))
    lista.append(n1)
    n2 = float(input('Nota 2: '))
    lista.append(n2)
    media = (n1+n2)/2
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    while True:
        resp = str(input('Você quer contituar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('Opção inválida. Tente novamente!')
    if resp == 'N':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for c in range(0, len(alunos)):
    print(f'{c:<4}{alunos[c][0]:<10}{alunos[c][3]:>8}')
print('-'*30)
while True:
    print('-'*30)
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))       
    if n == 999:
        print('FIM DE PROGRAMA!')
        break    
    print(f'Notas de {alunos[n][0]} são [{alunos[n][1]}, {alunos[n][2]}]')
print('<<<<< VOLTE SEMPRE >>>>>')
