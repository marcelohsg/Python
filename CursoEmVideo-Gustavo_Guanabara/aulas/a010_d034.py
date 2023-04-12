# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$1.250, calcule um aumento de 10%. Para salários inferiores ou iguais é de 15%.
salario = float(input('Digite seu salário: R$ '))
if salario > 1250:
    print(f'Seu novo salário será de R$ {(salario*1.1):.2f}')
else:
    print(f'Seu novo salário será de R${(salario*1.15):.2f}')
