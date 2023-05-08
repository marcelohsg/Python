pessoas = {'nome': 'Marcelo', 'sexo': 'M', 'idade': 30}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print('-='*30)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-='*30)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('-='*30)
for k in pessoas.keys():
    print(k)
print('-='*30)
for v in pessoas.values():
    print(v)
print('-='*30)
for k, v in pessoas.items():
    print(f'{k} = {v}')
