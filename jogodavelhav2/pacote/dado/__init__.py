def leiaDinheiro(txt='Preço: R$ '):
    valor = input(txt)
    while valor.isnumeric() == False:
        if ',' in valor or '.' in valor:
            convertido = valor.replace(',', '.')
            valor = float(convertido)
            return valor
        print(f'\033[0;31mErro: "{valor}" não é um preço válido!\033[m')
        valor = input('\033[0;33mDigite um preço: R$ \033[m')
    valor = float(valor)
    return valor

def leiaInt(txt='Digite um número Inteiro: '):
    numero = input(txt)
    while type(numero) != int:
        try:
            numero = int(numero)
            return numero
        except KeyboardInterrupt:
            print('\033[0;33mO usuário preferiu não digitar esse número.\033[m')
            numero = 0
            return numero
        except:
            print('\033[0;33mERRO! Você não digitou um número!\033[m')
            numero = input(txt)

def leiaFloat(txt='Digite um número Real: '):
    numero = input(txt)
    while type(numero) != float:
        try:
            if type(numero) == float:
                float(numero)
                return numero
            else:
                if ',' in numero or '.' in numero:
                    convertido = numero.replace(',', '.')
                    numero = float(convertido)
                    return numero
                numero = ''
                float(numero)
        except KeyboardInterrupt:
            print('\033[0;33mO usuário preferiu não digitar esse número.\033[m')
            numero = 0
            return numero
        except:
            print('\033[0;33mERRO! Você não digitou um número real!\033[m')
            numero = input(txt)
