# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('='*25)
print('O NÚMERO É PAR OU ÍMPAR?')
print('='*25)
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é ÍMPAR')
