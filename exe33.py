numero = int(input('Digite um numero:  '))

res = numero % 2

print('////'*15)
print('O NUMERO DIGITADO É PAR OU IMPAR? EU QUERO SABER !!!')
print('////'*15)

if res == 0 :
    print("O NÚMERO DIGITADO FOI {} ESTE NÚMERO É PAR !!!! ".format(numero))
else:
    print("O NÚMERO DIGITADO FOI {} ESTE NÚMERO É IMPAR !!!".format(numero))


