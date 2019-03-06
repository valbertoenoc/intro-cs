from random import choice

def computador_escolhe_jogada(n, m):

    melhor_jogada = m
    remover = m
    while remover > 0:
        if (n - remover) % (m + 1) == 0 == 0:
            melhor_jogada = remover
            break
        remover -= 1

    if remover == 0:
        melhor_jogada = min(n, m)

    if melhor_jogada == 1:
        print('O Computador tirou uma peça.')
    else:
        print('O Computador tirou {} peças.'.format(melhor_jogada))

    return melhor_jogada


def usuario_escolhe_jogada(n, m):    
    peca = min(n, m)
    while peca < n or peca > 0:
        peca = int(input('Quantas peças você vai tirar? '))
        
        if peca > m or peca <= 0 or peca > n:
            print('\nOops! Jogada inválida! Tente de novo.\n')
        else:
            break
    
    if peca == 1:
        print('Você tirou uma peça.')
    else:
        print('Você tirou {} peças.'.format(peca))
    
    return peca


def partida():
    n = m = -1
    while n < 0 or m < 0:
        n = int(input('Quantas peças? '))
        m = int(input('Limite de peças por jogada? '))

    jogadores = ['Computador', 'Voce']
    pontos = {
        jogadores[0]: 0,
        jogadores[1]: 0
    }

    jogador_atual = jogadores[1] if n % (m+1) == 0 else jogadores[0]

    print('\n{} começa!\n'.format(jogador_atual))

    pecas = pecas_restantes = n
    pecas_tiradas = 0
    while pecas > 0:
        
        if jogador_atual == 'Computador':
            pecas_tiradas = computador_escolhe_jogada(pecas_restantes, m)
            pecas_restantes -= pecas_tiradas
            pontos[jogador_atual] += pecas_tiradas

            if pecas_restantes == 0:
                vencedor = jogador_atual
                break

            jogador_atual = 'Voce'

            if pecas_restantes == 1:
                print('Agora resta apenas uma peça no tabuleiro.\n')
            else:
                print('Agora restam {} peças no tabuleiro.\n'.format(pecas_restantes))

        if jogador_atual == 'Voce':
            pecas_tiradas = usuario_escolhe_jogada(pecas_restantes, m)
            pecas_restantes -= pecas_tiradas
            pontos[jogador_atual] += pecas_tiradas

            if pecas_restantes == 0:
                vencedor = jogador_atual
                break

            jogador_atual = 'Computador'

            if pecas_restantes == 1:
                print('Agora resta apenas uma peça no tabuleiro.\n')
            else:
                print('Agora restam {} peças no tabuleiro.\n'.format(pecas_restantes))
                    
        pecas = pecas_restantes
    
    if vencedor == 'Voce':
        print('Fim de jogo! {} ganhou!\n'.format(vencedor))
    else:
        print('Fim de jogo! O {} ganhou!\n'.format(vencedor))

    return vencedor


def campeonato():
    n_rodadas = 3
    placar = {
        'Computador': 0,
        'Voce': 0,
        'Empate': 0
    }
    for i in range(n_rodadas):
        print('*'*4, ' Rodada {} '.format(i+1), '*'*4)
        vencedor = partida()

        placar[vencedor] += 1
    
    print('*'*4, ' Final de campeonato! ', '*'*4)
    print('Placar: Voce {} X {} Computador'.format(placar['Voce'], placar['Computador']))
   


while True:
    options = ['partida', 'campeonato']
    print('Bem vindo ao jogo do NIM! Escolha:\n')
    print('1 - para jogar uma partida isolada.')
    print('2 - para jogar um campeonato.')
    option = int(input())

    if option < 1 or option > len(options):
        print('Opção inválida! Tente de novo.\n')
        continue

    if options[option-1] == 'campeonato':
        print('Voce escolheu um campeonato!')
        campeonato()
        break
    elif options[option-1] == 'partida':
        print('Voce escolheu uma partida!')
        partida()
        break
# partida()