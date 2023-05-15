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
print('-='*30)
print(f'{"cod":<4} {"nome":<20} {"gols":<20} total')
print('-'*55)
for k, v in enumerate(lista):
    print(f'{k:<4} {v["nome"]:<20} {v["Total de gols"]:<20} {v["jogos"]}')
resp = ''
while True:
    print('-'*55)
    while True:
        resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if resp < len(lista) or resp == 999:
            break
        else:
            print('Jogador NÃO encontrado. Tente novamente!')
    if resp == 999:
        print('-'*55)
        print('PROGRAMA FINALIZADO!')
        print('  <<<< VOLTE SEMPRE >>>>')
        break    
    print(f'  -- LEVANTAMENTO DO JOGADOR {lista[resp]["nome"]}')
    print(f'     Realizou {lista[resp]["Total de gols"]} gols em {lista[resp]["jogos"]} jogos')
    print(f'     Média de {lista[resp]["Total de gols"]/lista[resp]["jogos"]:.2f} gols por jogo')
    
