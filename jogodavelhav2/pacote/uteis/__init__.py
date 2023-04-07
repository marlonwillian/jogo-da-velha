from random import randint
from pacote.dado import leiaInt

def sorteio():
    print('-' * 50)
    jogador1 = str(input('Nome do jogador 1: '))
    jogador2 = str(input('Nome do jogador 2: '))
    j1 = 1
    j2 = 2
    sorteio = randint(1, 2)
    global sorteado, nsorteado
    if j1 == sorteio:
        sorteado = jogador1
        nsorteado = jogador2
        print('-' * 50)
        print(f'{sorteado} joga primeiro!'.center(50))
        return sorteado, nsorteado
    else:
        if j2 == sorteio:
            sorteado = jogador2
            nsorteado = jogador1
            print('-' * 50)
            print(f'{sorteado} joga primeiro!'.center(30))
            return sorteado, nsorteado


def definidor(sorteado, nsorteado):
    print('-' * 50)
    jogador1 = str(input(f'{sorteado}, você quer jogar com o X ou O? ')).upper()
    if jogador1 == 'X':
        jogador2 = 'O'
        print('-' * 50)
        print(f'{sorteado} jogará com o {jogador1}.'.center(50))
        print(f'{nsorteado} jogará com o {jogador2}.'.center(50))
        if jogador1 == 'X':
            X = jogador1
            O = jogador2 
        return X, O
    elif jogador1 == 'O':
        jogador2 = 'X'
        print('-' * 50)
        print(f'{sorteado} jogará com o {jogador1}.'.center(50))
        print(f'{nsorteado} jogará com o {jogador2}.'.center(50))
        if jogador1 == 'O':
            O = jogador1
            X = jogador2
        return O, X
    print('-' * 50)

def geraTabela(letra1, letra2):
    print('-' * 50)
    global casas
    casas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    contador = 0
    jogadas = 0 
    verificador = False
    while verificador != True:
        print('\n')
        for c in range(1, 10):
            if c == 1 or c == 4 or c == 7:
                print(f'|{casas[c]}|'.rjust(23), end='')
            else:
                print(f'|{casas[c]}|', end='')
            if c == 3 or c == 6:
                print(end='\n')
            if c == 9:
                if contador % 2 == 0: 
                    print('\n')
                    casa = leiaInt(f'É a vez de {sorteado}, você quer jogar em qual posição? ')
                    if casas[casa] == letra1 or casas[casa] == letra2:
                        print('\n')
                        mostraTabela(sorteado, False)
                        print('\n')
                        casa = leiaInt(f'Erro! {sorteado} escolha uma casa vazia: ')
                        casas[casa] = letra1
                    else:
                        casas[casa] = letra1
                    verificador = verificaGanhador(sorteado, letra1)
                    contador += 1
                else:
                    if contador % 2 != 0:
                        print('\n')
                        casa = leiaInt(f'É a vez de {nsorteado}, você quer jogar em qual posição? ')
                        if casas[casa] == letra1 or casas[casa] == letra2:
                            print('\n')
                            mostraTabela(nsorteado, False)
                            print('\n')
                            casa = leiaInt(f'Erro! {nsorteado} escolha uma casa vazia: ')
                            casas[casa] = letra2
                        else:
                            casas[casa] = letra2
                        verificador = verificaGanhador(nsorteado, letra2)
                        contador +=1
                jogadas +=1
            if jogadas == 9:
                print('-' * 50)
                print('Deu velha!'.center(50))
                print('-' * 50)
                verificador = True

def verificaGanhador(jogador, letra):
    colunas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    contadorl = 0
    # Horizontal #
    for c in range(0, 3):
        if casas[colunas[0][c]] == letra:
            contadorl += 1
        if contadorl == 3:
            mostraTabela(jogador)
            return True
    contadorl = 0
    for c in range(0, 3):
        if casas[colunas[1][c]] == letra:
            contadorl += 1
        if contadorl == 3:
            mostraTabela(jogador)
            return True
    contadorl = 0
    for c in range(0, 3):
        if casas[colunas[2][c]] == letra:
            contadorl += 1
        if contadorl == 3:
            mostraTabela(jogador)
            return True
    # Vertical #
    contadorl = 0
    for c in range(0, 3):
        if casas[colunas[c][0]] == letra:
            contadorl += 1
        if contadorl == 3:
            mostraTabela(jogador)
            return True
    contadorl = 0   
    for c in range(0, 3):
        if casas[colunas[c][1]] == letra:
            contadorl += 1
        if contadorl == 3:
            mostraTabela(jogador)
            return True
    contadorl = 0    
    for c in range(0, 3):
        if casas[colunas[c][2]] == letra:
            contadorl += 1
        if contadorl == 3:
            mostraTabela(jogador)
            return True
    # Diagonais #
    contadorl = 0
    for c in range(0, 3):
        if casas[colunas[c][c]] == letra:
            contadorl += 1
        if contadorl == 3:
            mostraTabela(jogador)
            return True
    contadorl = 0
    for c in range(0, 3):
        if casas[colunas[0][2]] == letra and casas[colunas[1][1]] == letra and casas[colunas[2][0]] == letra:
            contadorl += 1
        if contadorl == 3:
            mostraTabela(jogador)
            return True
                 
def mostraTabela(jogador, vencedor = True):
    if vencedor == True:
        print('-' * 50)
        print(f'{jogador} ganhou!'.center(50))
        print('-' * 50)
        print('\n')
    for c in range(1, 10):
        if c == 1 or c == 4 or c == 7:
            print(f'|{casas[c]}|'.rjust(23), end='')
        else:
            print(f'|{casas[c]}|', end='')
        if c == 3 or c == 6:
            print(end='\n')
        if c == 9 and vencedor == True:
            print('\n')
            print('-' * 50)
            print(f'{jogador} ganhou!'.center(50))
            print('-' * 50)