print('TABUADA')
print('\=/'*20)
num = int(input('DIGITE UM NÚMERO E SAIBA SUA TABUADA:  '))
for z in range (1,11):
    print('{} x {:2} = {}'.format(num,z,num*z))