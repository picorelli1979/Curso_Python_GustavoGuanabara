vel = float(input('Digite qual a velocidade atual do carro: '))
if vel > 80:
    print('VELOCIDADE 80 km/h MAXIMA PERMITIDA')
    print('VC ESTÁ MULTADO!Sua velocidade atual foi de {} km/h'.format(vel))
    mul = (vel - 80) * 7
    print('Sua multa por excesso é R$ {} reais'.format(mul))
print('Dirija com Segurança')


