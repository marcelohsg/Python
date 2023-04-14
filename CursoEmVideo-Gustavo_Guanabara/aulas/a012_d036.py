# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa irá perguntar o valor da casa, o salário do comprador e em quantos anos ele irá pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado. 
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
prestacao = casa/(12*anos)
if prestacao <= (salario*0.3): 
    print(f'Para pegar uma casa no valor de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}. EMPRÉSTIMO CONSEDIDO!')
elif prestacao > (salario*0.3):
    print(f'Para pegar uma casa no valor de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}. EMPRÉSTIMO NEGADO!')