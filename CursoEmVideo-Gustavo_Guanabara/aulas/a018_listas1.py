'''teste = []
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
galera = [['João', 19], ['Ana', 35], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(f'galera[0] = {galera[0]}')
print(f'galera[0][0] = {galera[0][0]}')
print(f'galera[2][1] = {galera[2][1]}')
print('-'*30)
for pessoa in galera:
    print(pessoa)
print('-'*30)
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade!')

