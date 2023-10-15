dias = int(input('Qantos dias vc quer alugar o Carro? : '))
km = int(input('Qual foi a km que vc rodou? : '))
p = dias * 100 + (km * 0.25)

print('O total a pagar é de R$ {:.2f}'.format(p))

