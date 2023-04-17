# Refaça o desafio 009, mostrando a tabuada de um número que o usuario escolher, só que agora utilizando um laço for.
num = int(input('Você quer a tabuada de qual número? '))
for c in range(0, 11):
    print(f'{c} x {num} = {c*num}')
print('FIM!!')
