print('PROGRAMA DE VALIDAÇÃO DE DADOS')
print('='*60)

sexo = str(input('Digite o seu sexo [M/F]:   ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('Dados invalidos..Digite seu Sexo: '))

print('Sexo {} registrado com sucesso'.format(sexo))