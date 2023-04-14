# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5: reprovado!
# Média entre 5 e 6.9: Recuperação!
# Média 7 ou superior: Aprovado!
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
if media < 5:
    print(f'Sua média foi {media:.2f}. Aluno REPROVADO!')
elif media <= 6.9:
    print(f'Sua média foi {media:.2f}. Aluno RECUPERAÇÃO!')
else:
    print(f'Sua média foi {media:.2f}. Aluno APROVADO!')
