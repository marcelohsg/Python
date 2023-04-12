# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print('ANALISADOR DE TRIÃNGULOS')
print('-='*20)
a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))
if a < b + c and b < a + c and c < b + a:
    print('Os valores digitados podem formar um triângulo!')
else:
    print('Os valores digitados NÃO podem formar um triângulo!')
