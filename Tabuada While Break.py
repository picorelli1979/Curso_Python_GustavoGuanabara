print('\33[1;30;46m PROGRAMA DE TABUADA \33[m ')

while True:
   n = int (input('DIGITE UM NÚMERO PARA SABER A SUA TABUADA: '))
   print('-=-' * 50)
   if  n < 0:
      break
   for c in range(1,11):
       print(f'{n} X {c} = {n*c}')
   print('-=-'*50)
print('TABUADA ENCERRADA /// NUMEROS NEGATIVOS')


