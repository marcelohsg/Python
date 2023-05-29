# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(resp):
    from datetime import date
    ano = date.today().year
    idade = ano - resp
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# PROGRAMA PRINCIPAL
resp = int(input('Em que ano você nasceu? '))
print(voto(resp))