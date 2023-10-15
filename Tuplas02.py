cont = ('Zero', 'Um' , 'Dois', 'Três',
        'Quatro', 'Cinco', 'Seis', 'Sete',
        'Oito', 'Nove', 'Dez')
while True:
   num = int(input('DIGITE UM NúMERO ENTRE 0 e 10:'))
   if 0 <= num <= 10:
    break
   print('TENTE NOVAMENTE', end='')
print(f'VOCÊ DIGITOU O NÚMERO {cont[num]}')