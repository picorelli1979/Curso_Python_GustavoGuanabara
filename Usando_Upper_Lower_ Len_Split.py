nome= str(input('Digite seu nome:'))
print('Analisando seu nome:')
print('Seu nome em Maisculas é {}'.format(nome.upper()))
print('Seu nome em Minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)))
sp = nome.split()
print('O seu primeiro nome {} tem {} letras'.format(sp[0], len(sp[0])))



