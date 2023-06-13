def aumentar(valor=0, taxa=0):
    res = valor + (valor * taxa/100)
    return res


def diminuir(valor=0, taxa=0):
    res = valor - (valor * taxa/100)
    return res


def dobro(valor=0):
    return valor*2


def metade(valor=0):
    return valor/2


def resumo(valor=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \tR${valor}')
    print(f'Dobro do preço: \tR${dobro(valor)}')
    print(f'Metade do preço: \tR${metade(valor)}')
    print(f'{taxaa}% de aumento: \tR${aumentar(valor, 10)}')
    print(f'{taxar}% de redução: \t\tR${diminuir(valor, 5)}')
    print('-'*30)
