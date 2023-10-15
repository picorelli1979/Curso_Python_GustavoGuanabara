print('\033[1;30;46m///////////////////////CONVERSOR DE NÚMEROS///////////////////////////////\033[m')

num = int(input('DIGITE UM NÚMERO :'))
print('''ESCOLHA UMA DA OPÇÕES ABAIXO PARA CONVERSÃO DO NÚMERO: 
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opção = int(input('QUAL A SUA OPÇÃO ?: '))
if opção == 1:
    print('Seu número foi {} e convertendo para BINÁRIO será  {}'.format(num, bin(num)))
elif opção == 2:
    print('Seu número foi {} e convertido para OCTAL será  {}'.format(num, oct(num)))
elif opção == 3:
    print('Seu número foi {} e convertido para HEXADECIMAL será {}'.format(num, hex(num)))
else:
    print('\033[1;97;41mVOCÊ NÃO ESCOLHEU, TENTE NOVAMENTE .. ESCOLHA UMA OPÇÃO ACIMA !!!\033[m')
