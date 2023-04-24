# INTERROPENDO REPETIÇÕES WHILE
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break # Irá parar imediatamente o loop, impedindo que o número 999 seja somado.
    s += n
print(f'A soma vale {s}')
