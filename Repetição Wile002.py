from time import sleep
n1 = int(input('PRIMEIRO VALOR:   '))
n2 = int(input('SEGUNDO VALOR:   '))
opção = 0
while opção != 5:
    print('''    [ 1 ] SOMAR 
    [ 2 ] MULTIPLICAR 
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS 
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('QUAL A SUA OPÇÃO:    '))
    if   opção == 1 :
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1,n2,soma))
    elif opção == 2 :
        multiplicar = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1,n2,multiplicar))
    elif opção == 3 :
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif opção == 4 :
        print('Informe os Números novamente')
        n1 = int(input('PRIMEIRO VALOR:  '))
        n2 = int(input('SEGUNDO VALOR:   '))
    elif opção == 5 :
        print('FINALIZANDO..........')
    else:
        print('OPÇÃO INVALIDA.. TENTE NOVAMENTE')
    print('=-='*60)
    sleep(5)
print('FIM DO PROGRAMA!! VOLTE SEMPRE....')