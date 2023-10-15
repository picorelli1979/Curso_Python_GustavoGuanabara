from random import randint

computador = randint(0,5) # FAZ O COMPUTADOR PENSAR
print('-=-'*20)
print('TENTE ACERTAR O NÚMERO DE 0 Á 5 .....')
print('=/='*20)

jogador = int(input('EM QUE NUMERO PENSEI:  ')) # JOGADOR TENTA ACERTAR

if jogador == computador:
    print('PARABENS, VC ME VENCEU !!!!!')
else:
    print('ERRADO NÚMERO ERA {} E VC ESCOLHEU {}'.format(computador,jogador))


