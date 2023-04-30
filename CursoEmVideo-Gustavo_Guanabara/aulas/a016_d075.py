'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
valores = int(input('Digite um número: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite o último valor: '))
print(f'Tupla: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
    