n1 = float (input('Digite á Primeira Nota:  '))
n2 = float (input('Digite á Segunda Nota:   '))
n3 = float (input('Digite á Terceira Nota:   '))
n4 = float (input('Digite á Quarta Nota:   '))
média = (n1+n2+n3+n4)/4
print('VOCÊ TIROU  NO TESTE {} E NA PROVA {} ENTÃO FICOU COM MÉDIA {}'.format(n1,n2,média))
if média >= 6:
    print('PARABENS VC ESTÁ APROVADO !!!')
elif média <= 5:
    print('REPROVADO !!!')
elif 6 > média >=5:
    print('VC ESTÁ EM RECUPERAÇÃO....')



