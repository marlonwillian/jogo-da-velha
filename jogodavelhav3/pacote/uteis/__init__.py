from random import randint
from pacote.dado import leiaInt
from tkinter import *

def fechar(janela):
    janela.after(3000, lambda:janela.destroy())

def tela_sorteio():
    global janela_sorteio
    janela_sorteio = Tk()
    janela_sorteio.title('Jogo da velha')
    janela_sorteio.geometry('225x180')

    texto_orientacao = Label(janela_sorteio, text='Digite os nomes dos jogadores abaixo: ')
    texto_orientacao.grid(column = 0, row = 0)

    texto_j1 = Label(janela_sorteio, text='Nome do jogador 1: ')
    texto_j1.grid(column = 0, row = 2)

    global jogador1, jogador2
    jogador1 = Entry(janela_sorteio)
    jogador1.grid(column = 0, row = 3)

    texto_j2 = Label(janela_sorteio, text='Nome do jogador 2: ')
    texto_j2.grid(column = 0, row = 5)
    jogador2 = Entry(janela_sorteio)
    jogador2.grid(column = 0, row = 6)

    espaco = Label(janela_sorteio, text='')
    espaco.grid(column = 0, row = 8)

    botao = Button(janela_sorteio, text='Sortear', command=lambda: [sorteio(), fechar(janela_sorteio)])
    botao.grid(column = 0, row = 9)

    global texto_sorteado
    texto_sorteado = Label(janela_sorteio, text='')
    texto_sorteado.grid(column = 0, row = 10)

    janela_sorteio.mainloop()

def sorteio():
    j1 = 1
    j2 = 2
    sorteio = randint(1, 2)
    global sorteado, nsorteado
    if j1 == sorteio:
        sorteado = jogador1.get()
        nsorteado = jogador2.get()
        texto_sorteado['text'] = f'{sorteado} joga primeiro!'
        return sorteado, nsorteado
    else:
        if j2 == sorteio:
            sorteado = jogador2.get()
            nsorteado = jogador1.get()
            texto_sorteado['text'] = f'{sorteado} joga primeiro!'
            return sorteado, nsorteado

def tela_definidor():
        global janela_definidor, escolha, aviso1, aviso2

        janela_definidor = Tk()
        janela_definidor.title('Jogo da velha')
        janela_definidor.geometry('225x180')

        texto_escolha = Label(janela_definidor, text = f'{sorteado}, você quer jogar com o X ou O? ')
        texto_escolha.grid(column=0, row=1)

        escolha = Entry(janela_definidor)
        escolha.grid(column=0, row=2)
        
        botao = Button(janela_definidor, text='Pronto', command=lambda: [definidor(), fechar(janela_definidor)])
        botao.grid(column = 0, row = 3)

        aviso1 = Label(janela_definidor, text='')
        aviso1.grid(column=0, row=4)

        aviso2 = Label(janela_definidor, text='')
        aviso2.grid(column=0, row=5)

        janela_definidor.mainloop()

def definidor():
    if escolha.get() == 'X' or escolha.get() == 'x':
        jogador1 = 'X'
        jogador2 = 'O'
        aviso1['text'] = f'{sorteado} jogará com o {jogador1}.'
        aviso2['text'] = f'{nsorteado} jogará com o {jogador2}.'
        if jogador1 == 'X':
            X = jogador1
            O = jogador2 
        return X, O
    elif escolha == 'O':
        jogador1 = 'O'
        jogador2 = 'X'
        aviso1['text'] = f'{sorteado} jogará com o {jogador1}.'
        aviso2['text'] = f'{nsorteado} jogará com o {jogador2}.'
        if jogador1 == 'O':
            O = jogador1
            X = jogador2
        return O, X

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