galera = []
dado = []
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade!')
        totmenor += 1
print(f'Temos {totmaior} maoiores de idade e {totmenor} menores de idade.')