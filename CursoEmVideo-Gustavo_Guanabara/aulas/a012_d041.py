# A confederação nascinal de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com sua idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil!
# Até 19 anos: Júnior!
# Até 25 anos: Sênior!
# Acima: Master!
from datetime import date
ano = date.today().year
nome = input('Nome Completo: ')
nasc = int(input('Data de nascimento: '))
idade = ano - nasc
if idade <= 9:
    print(
        f'O(A) atleta, {nome}, tem {idade} anos e pertence a categoria MIRIN.')
elif idade <= 14:
    print(
        f'O(A) atleta, {nome}, tem {idade} anos e pertence a categoria INFANTIL.')
elif idade <= 19:
    print(
        f'O(A) atleta, {nome}, tem {idade} anos e pertence a categoria JÚNIOR.')
elif idade <= 25:
    print(
        f'O(A) atleta, {nome}, tem {idade} anos e pertence a categoria SÊNIOR.')
else:
    print(
        f'O(A) atleta, {nome}, tem {idade} anos e pertence a categoria MASTER.')
