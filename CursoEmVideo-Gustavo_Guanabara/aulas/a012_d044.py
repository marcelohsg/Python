# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições de pagamento:
# À vista dinheiro cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
valor = float(input('Valor do produto: R$'))
print('''Qual a forma de pagamento?
[1] À vista, dinheiro ou cheque: Desconto de 10%
[2] À vista no cartão: Desconto de 5%
[3] Em até 2x no cartão: Sem desconto
[4] 3x ou mais no cartão: Juros de 20%''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    print(f'O valor a ser pago será de R${(valor*0.9):.2f}')
elif opcao ==2:
    print(f'O valor a ser pago será de R${(valor*0.95):.2f}')
elif opcao == 3:
    print(f'O valor a ser pago será de R${valor}')
elif opcao == 4:
    print(f'O valor a ser pago será de R${(valor*1.2):.2f}')
else:
    print('Opção inválida!')
