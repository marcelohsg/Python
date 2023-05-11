# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
from time import sleep
trabalhador = {}
trabalhador['nome'] = input('Nome: ')
ano = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - ano
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] == 0:
    print('-='*30)
    for k, v in trabalhador.items():
        print(f'    - {k} tem o valor {v}')
        sleep(1)
else:
    trabalhador['contratação'] = int(input('Ano de Contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)
    print('-='*30)
    for k, v in trabalhador.items():
        print(f'    - {k} tem valor {v}')
        sleep(1)