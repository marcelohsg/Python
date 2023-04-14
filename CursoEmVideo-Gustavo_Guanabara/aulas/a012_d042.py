# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero, Isósceles ou Escaleno
print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))
if a < b + c and b < a + c and c < b + a:
    print('Os valores digitados podem formar um triângulo!')
    if a == b and a == c and c == b:
        print('O triângulo é EQUILÁTERO!')
    elif a != b and a != c and c != b:
        print('O triângulo é ESCALENO!')
    else:
        print('O triângulo é ISÓSCELES')
else:
    print('Os valores digitados NÃO podem formar um triângulo!')
