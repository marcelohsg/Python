'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 5:
        cont += 1
    lista.append(n)
    while True:
        r = input('Você quer continuar [S/N]? ').upper().strip()[0]
        if r in 'SN':
            break
        else:
            print('Opção inválida. Tente novamente!') 
    if r == 'N':
        print('Fim do programa!')
        break
print(f'O total de {len(lista)} números foram digitados.')
lista.sort(reverse=True)
print(f'Lista ordenada de forma decrescente {lista}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista!')
else:
    print(f'O valor 5 foi encontrado na lista {cont} vezes!')