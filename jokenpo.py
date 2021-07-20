from random import randint

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']

while True:
    print('='*29)
    print('-'*10, 'JOKENPÔ', '-'*10)
    print('='*29)
    vitorias_jogador = 0
    vitorias_computador = 0
    qtd_rodadas = int(input('Quantas rodadas iremos jogar? '))
    for i in range(qtd_rodadas):
        print()
        escolha_jogador = int(input('[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nQual é a sua escolha? '))
        escolha_computador = randint(0,2)
        print()
        print(f'O computador escolheu {jokenpo[escolha_computador]}')
        print(f'Você escolheu {jokenpo[escolha_jogador]}')
        print()
        if escolha_computador == 0:
            if escolha_jogador == 0:
                print('EMPATOU')
            elif escolha_jogador == 1:
                print('VOCÊ VENCEU')
                vitorias_jogador += 1
            elif escolha_jogador == 2:
                print('COMPUTADOR VENCEU')
                vitorias_computador += 1
            else:
                print('ESCOLHA INVÁLIDA')
        elif escolha_computador == 1:
            if escolha_jogador == 0:
                print('COMPUTADOR VENCEU')
                vitorias_computador += 1            
            elif escolha_jogador == 1:
                print('EMPATOU')
            elif escolha_jogador == 2:
                print('VOCÊ VENCEU')
                vitorias_jogador += 1
            else:
                print('ESCOLHA INVÁLIDA')
        elif escolha_computador == 2:
            if escolha_jogador == 0:
                print('VOCÊ VENCEU')
                vitorias_jogador += 1           
            elif escolha_jogador == 1:
                print('COMPUTADOR VENCEU')
                vitorias_computador += 1
            elif escolha_jogador == 2:
                print('EMPATOU')
            else:
                print('ESCOLHA INVÁLIDA')
    print()
    print(f'O computador venceu {vitorias_computador} rodadas.')
    print(f'Você venceu {vitorias_jogador} rodadas.')
    if vitorias_jogador > vitorias_computador:
        print('\nO grande campeão dessa partida foi VOCÊ')
    elif vitorias_computador > vitorias_jogador:
        print('\nO grande campeão dessa partida foi o COMPUTADOR')
    elif vitorias_jogador == vitorias_computador:
        print('\nNão tivemos um campeão nessa rodada. Jogue Novamente!')
    continuar = input('\nVamos jogar novamente? [S/N]: ').upper()
    if continuar == 'N':
        break
print('\nVocê finalizou o programa.')