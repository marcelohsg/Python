# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = total = soma = maior = menor = 0
continuar = ''
while continuar != "N":
    num = int(input('Digite um valor: '))
    total += 1
    soma += num 
    if total == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num   
    continuar = input('Você ainda quer continuar [s/n]? ').upper().strip()[0]
print(f'Você digitou {total} números e a média foi {soma/total}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')

