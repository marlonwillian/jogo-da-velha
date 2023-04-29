from random import randint
from tkinter import *

def fechar(janela, tempo):
    janela.after(tempo, lambda:janela.destroy())

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

    botao = Button(janela_sorteio, text='Sortear', command=lambda: [sorteio(), fechar(janela_sorteio, 1500)])
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
    else:
        if j2 == sorteio:
            sorteado = jogador2.get()
            nsorteado = jogador1.get()
            texto_sorteado['text'] = f'{sorteado} joga primeiro!'
            
def tela_definidor():
        global janela_definidor, escolha, aviso1, aviso2
    
        janela_definidor = Tk()
        janela_definidor.title('Jogo da velha')
        janela_definidor.geometry('225x180')

        texto_escolha = Label(janela_definidor, text = f'{sorteado}, você quer jogar com o X ou O? ')
        texto_escolha.grid(column=0, row=1)

        escolha = Entry(janela_definidor)
        escolha.grid(column=0, row=2)
        
        botao = Button(janela_definidor, text='Pronto', command=lambda: [definidor(), fechar(janela_definidor, 2000)])
        botao.grid(column = 0, row = 3)

        aviso1 = Label(janela_definidor, text='')
        aviso1.grid(column=0, row=4)

        aviso2 = Label(janela_definidor, text='')
        aviso2.grid(column=0, row=5)

        janela_definidor.mainloop()

def definidor():
    global jogador1, jogador2
    if escolha.get() == 'X' or escolha.get() == 'x':
        jogador1 = 'X'
        jogador2 = 'O'
        aviso1['text'] = f'{sorteado} jogará com o {jogador1}.'
        aviso2['text'] = f'{nsorteado} jogará com o {jogador2}.'
    elif escolha == 'O':
        jogador1 = 'O'
        jogador2 = 'X'
        aviso1['text'] = f'{sorteado} jogará com o {jogador1}.'
        aviso2['text'] = f'{nsorteado} jogará com o {jogador2}.'

def tela_tabela():
    cor_fundo = 'black'
    cor_linha = 'white'

    global janela_tabela
    
    janela_tabela = Tk()
    janela_tabela.title('Jogo da Velha')
    janela_tabela.geometry('235x330')

    # frames #

    frame_topo = Frame(janela_tabela, width=235, height=100, bg=cor_fundo)
    frame_topo.grid(row=0, column=0)

    frame_meio = Frame(janela_tabela, width=235, height=100, bg=cor_fundo)
    frame_meio.grid(row=2, column=0)

    frame_baixo = Frame(janela_tabela, width=235, height=100, bg=cor_fundo)
    frame_baixo.grid(row=4, column=0)

    global c, contador
    c = 0
    contador = 0

    while True:

        # botões topo #

        global b1, b2, b3, b4, b5, b6, b7, b8, b9

        b1 = Button(frame_topo, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b1), verificaGanhador()])
        b1.place(x=0, y=0)

        b2 = Button(frame_topo, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b2), verificaGanhador()])
        b2.place(x=80, y=0)

        b3 = Button(frame_topo, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b3), verificaGanhador()])
        b3.place(x=160, y=0)

        # botões meio #

        b4 = Button(frame_meio, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b4), verificaGanhador()])
        b4.place(x=0, y=1)

        b5 = Button(frame_meio, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b5), verificaGanhador()])
        b5.place(x=80, y=1)

        b6 = Button(frame_meio, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b6), verificaGanhador()])
        b6.place(x=160, y=1)

        # botões de baixo #

        b7 = Button(frame_baixo, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b7), verificaGanhador()])
        b7.place(x=0, y=1)

        b8 = Button(frame_baixo, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b8), verificaGanhador()])
        b8.place(x=80, y=1)

        b9 = Button(frame_baixo, text='', width=10, height=8, bg=cor_linha, command=lambda: [marcador(b9), verificaGanhador()])
        b9.place(x=160, y=1)

        global aviso
        aviso = Label(janela_tabela, text=f'Vez de {sorteado} jogar! |{jogador1}|')
        aviso.grid(row=5, column=0)

        janela_tabela.mainloop()
        
        break

def marcador(nbotao):
    global c, contador, vencedor, verifica
    verifica = False
    if c % 2 == 0 and nbotao['text'] == '':
        nbotao['text'] = jogador1
        aviso['text'] = f'Vez de {nsorteado} jogar! |{jogador2}|'
        vencedor = sorteado
        c += 1
        contador += 1
        if contador == 9:
            aviso['text'] = f'Deu velha!'
            fechar(janela_tabela, 2000)
    elif c % 2 != 0 and nbotao['text'] == '':
        nbotao['text'] = jogador2
        aviso['text'] = f'Vez de {sorteado} jogar! |{jogador1}|'
        vencedor = nsorteado
        c += 1
        contador += 1
        if contador == 9:
            aviso['text'] = f'Deu velha!'
            fechar(janela_tabela, 2000)
    elif nbotao['text'] != '': 
            aviso['text'] = 'Marque em lugar vazio!'

def verificaGanhador():
    # Horizontal #

    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)

    # Vertical #

    if b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    
    # Diagonal #

    if b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' and verifica == False:
        verifica = True
        aviso['text'] = f'{vencedor} ganhou!'
        fechar(janela_tabela, 2000)