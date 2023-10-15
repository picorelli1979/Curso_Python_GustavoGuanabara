print('='*50)
print('\033[1;31mANALISE DE MASSA CORPOREA\033[m')
print('='*50)

peso = float(input('QUANTO VOCÊ PESA ? (kg):    '))
altura = float(input('QUANTO VOCÊ MEDE ? (m):   '))
imc = peso / (altura **2)
print('SEU IMC É {:.1f}'.format(imc))
if imc <= 18.5:
    print('\033[1;97;45mABAIXO DO PESO\033[m')
elif imc >= 18.5 and imc <= 25:
    print ('\033[1;31;44mPESO IDEAL\033[m')
elif imc > 25.1 and imc <= 30:
     print('\033[1;36;107mSOBREPESO\033[m')
elif imc >= 30.1 and imc <= 40 :
     print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')



