# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = {}
jogador['nome'] = str(input('Nome: '))
jogador['jogos'] = int(input('Quantidade de jogos: '))
if jogador['jogos'] != 0:
    totg = 0
    for cont in range (1, jogador['jogos']+1):
        gols = int(input(f'  Gol(s) marcado(s) na {cont}º partida: '))
        totg += gols  
jogador['Total de gols'] = totg
print('-='*30)
print(jogador)
for k, v in jogador.items():
    print(f'{k}: {v}')
