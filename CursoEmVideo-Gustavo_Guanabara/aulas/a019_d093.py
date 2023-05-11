# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
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
