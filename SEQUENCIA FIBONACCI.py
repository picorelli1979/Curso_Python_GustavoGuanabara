print('-=-'*30)
print('SEQUENCIA FIBONACCI')
print('-=-'*30)
n = int(input('QUANTOS TERMOS VC QUER MOSTRAR ? :   '))
t1 = 0
t2 = 1
print('-'*30)
print('{} -> {} '.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1+t2
    print( ' -> {} '.format(t3), end='')
    t1=t2
    t2=t3
    cont +=1
print(' -> FIM')