from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
print('Você nasceu em {} e tem {} anos..'.format(nasc,idade))
if idade == 18:
   print('VOCÊ TERÁ QUE SE ALISTAR IMEDIATAMENTE !!!!')
elif idade < 18:
    saldo = 18 - idade
    print('VOCÊ NÃO COMPLETOU A IDADE EXATA RESTAM {} ANOS ....'.format(saldo))
    ano = atual + saldo
    print('SEU ALISTAMENTO SERÁ EM {}'.format(ano))
else:
    saldo = idade - 18
    print('VOCê JÁ DEVERIA TER SE ALISTADO Á {} ANOS'.format(saldo))
    ano = atual - saldo
    print('SEU ALISTAMENTO FOI EM {}'.format(ano))
