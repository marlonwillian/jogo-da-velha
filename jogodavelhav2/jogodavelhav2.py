from pacote import uteis

print('-' * 50)
print('Jogo da velha'.center(50))
print('-' * 50)

sorteado = uteis.sorteio()
letras = uteis.definidor(sorteado[0], sorteado[1])
tabela = uteis.geraTabela(letras[0], letras[1])
