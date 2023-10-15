from random import randint
computador = randint(0,10)

print('SOU SEU COMPUTADOR !!!')
print('ESTOU PENSANDO EM NÚMERO DE 0 HÁ 10...')
print('SERÁ QUE VC CONSEGUE ADVINHAR????????')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('QUAL O SEU PALPITE?:   '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... Tente mais uma vez!!!')
        elif jogador > computador:
            print('Menos... Tente outra vez!!!')
print('='*70)
print('ACERTOU !!!!!')
print ('='*70)

