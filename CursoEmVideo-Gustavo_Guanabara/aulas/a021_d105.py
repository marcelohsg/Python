# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: – Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)
def notas(*n, sit=False):
    dic = {}
    dic['Total'] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = (sum(n)/len(n))
    if sit == True:
        if dic['Média'] >= 7:
            dic['Situação'] = 'Boa'
        elif dic['Média'] >= 5:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Ruim'
    return dic


# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
