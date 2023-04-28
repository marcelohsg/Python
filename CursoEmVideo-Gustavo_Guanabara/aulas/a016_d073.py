'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
times = ('Palmeiras', 'Inter', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
         'América-MG', 'Botafogo', 'Santos', 'Goiás', 'RB Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('-='*15)
print(f'a) Os cincos primeiros colocados são: {times[:6]}')
print('-='*15)
print(f'b) Os últimos quatro colocados são: {times[-4:]}')
print('-='*15)
print(f'c) Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'd) Posição do Flamengo: {times.index("Flamengo")+1}º posição!')
