'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
total = contProduto = cont = 0
while True:
    nome = input('Nome do produto: ').strip()
    valor = float(input('Preço: R$'))
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar [S/N]? ').strip().upper()[0]
    total += valor
    if valor >= 1000:
        contProduto += 1
    cont += 1
    if cont == 1:
        produto = nome
        menor = valor
    else:
        if valor < menor:
            menor = valor
            produto = nome
    if resposta == 'N':
        break
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'Quantidade de produtos que custam mais de R$1000: {contProduto}')
print(f'O produto mais barato é {produto} com o preço de R${menor:.2f}')
