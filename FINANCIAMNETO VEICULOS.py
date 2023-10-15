print('\033[1;30;107mSISTEMA DE CALCULO DE VEICULOS\033[m')
print('-=-'*60)
nome = str(input('QUAL O NOME COMPLETO ? :    '))
cpf = str(input('DIGITE SEU CPF:     '))
valor = float(input('QUAL O VALOR DO VEICULO ?:    '))
ano = int(input('QUAL O ANO DO VEICULO:     '))
sinal = float(input('QUAL O SINAL ? :   '))
meses = int(input('QUANTOS MESES ?:     '))
renda = float (input('QUAL A SUA RENDA ?:   '))

minimo = renda * 30/100
finan = valor - sinal
resto = finan / meses
juros = (30 * 33/100) * 30

prestação= resto + juros

print('O VALOR A SER FINANCIADO É DE {:.3f} mil reais'.format(finan))
print('ESTE É O VALOR DA SUA RENDA IMPACTADA R$ {}'.format(minimo))
print('O VALOR DO JUROS MENSAL É R$ {}'.format(juros))
print('\033[1;31;107m A sua prestação ficou R$ {} reais\033[m'.format(prestação))

print('-'*50)
if prestação < minimo:
    print('\033[1;30;46mFICHA APROVADA, FAVOR ANEXAR OS DOCUMENTOS \033[m')
else:
    print('\033[1;97;41mFICHA NEGADA, TENTE NOVAMENTE COM UMA RENDA MAIOR \033[m')


