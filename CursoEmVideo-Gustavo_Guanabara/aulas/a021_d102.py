# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

num = int(input('Você quer o fatorial de qual número? '))
while True:
    resp = input('Será mostrado o processo de cálculo do fatorial [S/N]? ').strip().upper()[0]
    if resp in 'SN':
        break
    else: 
        print('Opção inválida. Responda "S" para SIM ou "N" para NÃO!')
if resp == "S":
    x = True
if resp == "N":
    x = False
print(fatorial(num, show=x))
