print( '{:/^100}'.format (' LOJAS CATEL TEMPERADOS '))
valor = float (input('QUAL O VALOR DAS COMPRAS? : R$   '))
print(''' FORMAS DE PAGAMENTO : 
[ 1 ] = A VISTA / CHEQUE. 
[ 2 ] = CARTÃO A VISTA.
[ 3 ] = CARTÃO EM 2 VEZES.
[ 4 ] = CARTÃO EM 3 VEZES. ''')
Opção = int(input('QUAL A SUA OPÇÃO:   '))
if   Opção == 1:
     total = valor - (valor * 10/100)
elif Opção == 2:
     total = valor - (valor * 5/100)
elif Opção == 3:
     total = valor
     parcela = total / 2
     print('VOCÊ COMPROU EM 2X NO CARTÃO, SUA PARCELA FICOU R$ {:.2f} SEM JUROS'.format(parcela))
elif Opção == 4:
     total = valor + (valor * 20/100)
     totalparc = int(input('QUANTAS PARCELAS?:   '))
     parcelas = total / totalparc
     print('VOCÊ COMPROU EM {} VEZES NO CARTÃO, SUA PARCELA FICOU R$ {:.2f} COM JUROS'.format(totalparc,parcelas))
print('Sua compra de R$ {:.2f} e ficou no final por R$ {:.2f}'.format(valor,total))

print('**'*60)