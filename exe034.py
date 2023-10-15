viagem = float (input('Qual a Kilometragem percorrida em sua viagem:   '))
print('Nós percorremos um total de {}km' .format(viagem))
if viagem <= 200:
    valor = 200 * 0.50
    print('Sua passagem custará R$ {:.2f}'.format(valor))
else:
    valor = 200 * 0.90
    print('A multa da passagem será R$ {:.2f}por km rodado.'.format(valor))