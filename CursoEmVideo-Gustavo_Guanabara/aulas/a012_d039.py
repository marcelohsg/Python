# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
if idade < 16:
    print(
        f' Idade: {idade} anos.\n Status: Ainda irá se alistar!\n Ano(s) faltante(s): {18-idade} ano(s)')
elif idade <= 18:
    print(
        f' Idade: {idade} anos.\n Status: Já pode se alistar!\n Ano faltante: {18-idade} ano(s)')
else:
    print(
        f' Idade: {idade} anos.\n Status: Já passou de se alistar!\n Ano(s) excedente(s): {idade-18} ano(s)')
