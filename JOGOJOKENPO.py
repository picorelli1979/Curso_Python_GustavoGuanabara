from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('{:=^60}'.format('JOGO DE JOKENPO '))
Computador = randint(0,2)
print('''QUAL A SUA ESCOLHA :
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA ''')
Jogador= int (input('QUAL A SUA JOGADA ?:   '))
print('PEDRA')
sleep(2)
print('PAPEL')
sleep(2)
print('TESOURA')

print('-=-' * 70)
print('O COMPUTADOR ESCOLHEU {}'.format(itens[Computador]))
print('O JOGADOR ESCOLHEU {} '.format(itens[Jogador]))
print('-=-' * 70)
if Computador == 0: # COMPUTADOR JOGOU PEDRA
    if Jogador ==0:
        print('EMPATE')
    elif Jogador ==1:
        print('JOGADOR VENCEU')
    elif Jogador ==2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif Computador == 1: # COMPUTADOR JOGOU PAPEL
    if Jogador == 0:
       print('COMPUTADOR VENCEU')
    elif Jogador == 1:
        print('EMPATE')
    elif Jogador ==2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif Computador == 2 :  # COMPUTADOR JOGOU TESOURA
    if Jogador == 0:
        print('JOGADOR VENCEU')
    elif Jogador == 1:
        print('COMPUTADOR  VENCEU')
    elif Jogador ==2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
