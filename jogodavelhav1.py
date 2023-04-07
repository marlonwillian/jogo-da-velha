from random import randint

    # Titulo #

print('-' * 30)
print('Jogo da velha'.center(30))
print('-' * 30)

jogador1 = ''
jogador2 = ''

    # Sorteio de quem começa #

j1 = 1
j2 = 2
sorteio = randint(1, 2)

if j1 == sorteio:
    sorteado = 'Jogador 1'
    nsorteado = 'Jogador 2'
    print(f'O {sorteado} começa!')
    jogador1 = str(input('Você quer jogar com \033[0;34mX\033[m ou \033[0;31mO\033[m? ').upper())
    s = jogador1
else:
    if j2 == sorteio:
        sorteado = 'Jogador 2'
        nsorteado = 'Jogador 1'
        print(f'O {sorteado} começa!')
        jogador2 = str(input('Você quer jogar com \033[0;34mX\033[m ou \033[0;31mO\033[m? ').upper())
        s = jogador2
print('-' * 30)

    # X ou O #
if jogador1 == 'X':
    jogador2 = 'O'
    print(f'O {sorteado} escolheu o {jogador1}, o Jogador 2 é o O.')
    print('-' * 30)
    ns = jogador2
elif jogador1 == 'O':
    jogador2 = 'X'
    print(f'O {sorteado} escolheu o {jogador1}, o Jogador 2 é o X.')
    print('-' * 30)
    ns = jogador2
else:
    if jogador2 == 'X':
        jogador1 = 'O'
        print(f'O {sorteado} escolheu o {jogador2}, o Jogador 1 é o O.')
        print('-' * 30)
        ns = jogador1
    if jogador2 == 'O':
        jogador1 = 'X'
        print(f'O {sorteado} escolheu o {jogador2}, o Jogador 1 é o X.')
        print('-' * 30)
        ns = jogador1

    # Gerador de tabela #

casas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = 0
while True:
    if contador % 2 == 0:
        c = 0
        if contador == 0:
            for c in range(casas[c] + 1, casas[len(casas) - 1]):
                print(f'|{casas[c]}|', end='')
                if c == 3 or c == 6:
                    print(end='\n')
                if c == 9:
                    pos = int(input('\nVocê quer jogar em qual posição? '))
                    while casas[pos] == s or casas [pos] == ns:
                        print('-' * 30)
                        print('Já jogaram nesssa posição!')
                        pos = int(input('Você quer jogar em qual posição? '))
                        print('-' * 30)
                    casas[pos] = s
        else:
            for c in range(casas[c] + 1, casas[len(casas) - 1]):
                print(f'|{casas[c]}|', end='')
                if c == 3 or c == 6:
                    print(end='\n')
                if c == 9:
                    pos = int(input('\nVocê quer jogar em qual posição? '))
                    while casas[pos] == s or casas [pos] == ns:
                        print('-' * 30)
                        print('Já jogaram nesssa posição!')
                        pos = int(input('Você quer jogar em qual posição? '))
                        print('-' * 30)
                    casas[pos] = s
        contador += 1
    else:
        c = 0
        if contador == 0:
            for c in range(casas[c] + 1, casas[len(casas) - 1]):
                print(f'|{casas[c]}|', end='')
                if c == 3 or c == 6:
                    print(end='\n')
                if c == 9:
                    pos = int(input('\nVocê quer jogar em qual posição? '))
                    while casas[pos] == s or casas [pos] == ns:
                        print('-' * 30)
                        print('Já jogaram nesssa posição!')
                        pos = int(input('Você quer jogar em qual posição? '))
                        print('-' * 30)
                    casas[pos] = ns
        else:
            for c in range(casas[c] + 1, casas[len(casas) - 1]):
                print(f'|{casas[c]}|', end='')
                if c == 3 or c == 6:
                    print(end='\n')
                if c == 9:
                    pos = int(input('\nVocê quer jogar em qual posição? '))
                    while casas[pos] == s or casas [pos] == ns:
                        print('-' * 30)
                        print('Já jogaram nesssa posição!')
                        pos = int(input('Você quer jogar em qual posição? '))
                        print('-' * 30)
                    casas[pos] = ns
        contador += 1

    # Casas Horizontais #

    if casas[1] == s and casas[2] == s and casas[3] == s:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[1] == ns and casas[2] == ns and casas[3] == ns:
        print('-' * 30)
        print(f'O {nsorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[4] == s and casas[5] == s and casas[6] == s:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[4] == ns and casas[5] == ns and casas[6] == ns:
        print('-' * 30)
        print(f'O {nsorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[7] == s and casas[8] == s and casas[9] == s:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[7] == ns and casas[8] == ns and casas[9] == ns:
        print('-' * 30)
        print(f'O {nsorteado} ganhou!!'.center(30))
        print('-' * 30)
        break

    # Casas Verticais #

    if casas[1] == s and casas[4] == s and casas[7] == s:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[1] == ns and casas[4] == ns and casas[7] == ns:
        print('-' * 30)
        print(f'O {nsorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[2] == s and casas[5] == s and casas[8] == s:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[2] == ns and casas[5] == ns and casas[8] == ns:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[3] == s and casas[6] == s and casas[9] == s:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[3] == ns and casas[6] == ns and casas[9] == ns:
        print('-' * 30)
        print(f'O {nsorteado} ganhou!!'.center(30))
        print('-' * 30)
        break

    # Diagonais #

    if casas[7] == s and casas[5] == s and casas[3] == s:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[7] == ns and casas[5] == ns and casas[3] == ns:
        print('-' * 30)
        print(f'O {nsorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[9] == s and casas[5] == s and casas[1] == s:
        print('-' * 30)
        print(f'O {sorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
    elif casas[9] == ns and casas[5] == ns and casas[1] == ns:
        print('-' * 30)
        print(f'O {nsorteado} ganhou!!'.center(30))
        print('-' * 30)
        break
