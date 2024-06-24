import os

def bem_vindo():
    print('============================================================')
    print('Bem vindo ao jogo de Papel, Pedra ou Tesoura, vamos começar!')
    print('============================================================')
    

jogador_pontos = 0
computador_pontos = 0

def pontuacao():
    if vencedor == 'Jogador':
        global jogador_pontos
        jogador_pontos += 1
    elif vencedor == 'Computador':
        global computador_pontos
        computador_pontos += 1
    print(f'Jogador: {jogador_pontos} pontos')
    print(f'Computador: {computador_pontos} pontos')
    

    
# def escolha_jogador():
#     while True:
#         #tentar usar o try e except para tratar a exceção
#         escolha = input('Escolha entre pedra, papel ou tesoura: ')
#         if escolha == 'pedra' or escolha == 'papel' or escolha == 'tesoura':
#             return escolha
#         else:
#             print('Escolha inválida, por favor, escolha entre pedra, papel ou tesoura')


def escolha_jogador():
    while True:
        #tentar usar o try e except para tratar a exceção
        try:
            escolha = input('Escolha entre pedra, papel ou tesoura: ')
            if escolha == 'pedra' or escolha == 'papel' or escolha == 'tesoura':
                break
        except Exception as e:
            print("Erro: {}".format(e))
                
    return escolha
        

def escolha_computador():
    import random
    escolha = random.choice(['pedra', 'papel', 'tesoura'])
    return escolha

def verifica_vencedor(jogador, computador):
    if jogador == computador:
        return 'Empate'
    elif jogador == 'pedra':
        if computador == 'tesoura':
            return 'Jogador'
        else:
            return 'Computador'
    elif jogador == 'papel':
        if computador == 'pedra':
            return 'Jogador'
        else:
            return 'Computador'
    elif jogador == 'tesoura':
        if computador == 'papel':
            return 'Jogador'
        else:
            return 'Computador'
    else:
        return 'Escolha inválida, por favor, escolha entre pedra, papel ou tesoura'

bem_vindo()
jogador = escolha_jogador()
computador = escolha_computador()
print(f'O computador escolheu {computador}')
print(f'O jogador escolheu {jogador}')
vencedor = verifica_vencedor(jogador, computador)
print(f'O vencedor foi {vencedor}')
pontuacao()

while True:
    continuar = input('Deseja jogar novamente? (s/n): ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if continuar == 's':
        jogador = escolha_jogador()
        computador = escolha_computador()
        print(f'O computador escolheu {computador}')
        print(f'O jogador escolheu {jogador}')
        vencedor = verifica_vencedor(jogador, computador)
        print(f'O vencedor foi {vencedor}')
        pontuacao()
    else:
        print('Obrigado por jogar!')
        pontuacao()
        break
    
