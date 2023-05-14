# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
lista = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome: '))
    jogador['jogos'] = int(input('Quantidade de jogos: '))
    if jogador['jogos'] != 0:
        totg = 0
        for cont in range (1, jogador['jogos']+1):
            gols = int(input(f'  Gol(s) marcado(s) na {cont}º partida: '))
            totg += gols  
    jogador['Total de gols'] = totg
    lista.append(jogador.copy())
    jogador.clear()
    while True:
        option = input('Você quer continuar [S/N]? ').strip().upper()[0]
        if option in 'SN':
            break
        else:
            print('Opção inválida. Escolha "S" para SIM ou "N" para NÃO!')
    if option == 'N':
        break
print(lista)