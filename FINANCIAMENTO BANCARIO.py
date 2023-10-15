print('-=-'*30)
print('\033[1;30;46mPROGRAMA DE SIMULAÇÃO DE FINANCIAMENTO BANCÁRIO\033[m')
print('-=-'*30)
Imóvel = float(input('QUAL O VALOR DO IMÓVEL: R$   '))
Sinal = float(input('QUAL O VALOR DE SINAL R$    '))
Finan = Imóvel - Sinal
Sálario = float (input('QUAL A SUA RENDA MENSAL: R$   '))
Prazo = int(input('QUANTOS ANOS SERÁ SEU FINANCIAMENTO:   '))

print('-=-'*80)
Prestação = Imóvel / (Prazo * 12)
Minimo = Sálario * 30/100

if Prestação < Minimo:
    print('\033[1;31;107mAPROVADO!! FAVOR ANEXAR OS DOCUMENTOS\033[m')
    print('='*80)
    print('\033[1;30;103m COM SINAL DE R$ {:.3f} VOCê CONSEGUIU UM CRÉDITO R${:.3f}\033[m'.format(Sinal,Finan))
else:
    print('\033[1;97;41mNEGADO ... SUA RENDA É INSUFICIENTE\033[m')
print('\033[1;34m=\033[m' * 80 )
print('\033[1;30;46mPARA FINANCIAR UM IMÓVEL DE R$ {:.3f}, EM {} ANOS E COM RENDA DE R$ {:.3f}\033[m'.format(Imóvel,Prazo,Sálario))
print('\033[1;34m=\033[m' * 80 )
print('\033[1;30;41mSUA PRESTAÇÃO SERÁ R$ {:.3f}\033[m'.format(Prestação))
print('-=-'*80)