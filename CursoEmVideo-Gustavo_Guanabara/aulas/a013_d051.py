# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('=-'*15)
print('    10 TERMOS DE UMA P.A.')
print('=-'*15)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = n1 + (10 - 1) *r
for c in range(n1, decimo + r, r):
    print(c, end=' -> ')
print('ACABOU!')
