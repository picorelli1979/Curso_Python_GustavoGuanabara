print('{:=^50}'.format('LOJAO DE PRODUTOS'))
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('QUAL O PRODUTO: '))
    preço = float(input('PREÇO: R$  '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor :
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
       resp = str(input('QUER CONTINUAR? [S/N]')).strip().upper()[0]
    if resp == 'N':
       break
print('{:=^50}'.format('FIM DO PROGRAMA'))
print(f'O TOTAL DA COMPRA FOI {total:.2f}')
print(f'TEMOS {totmil}, PRODUTOS DESTA LISTA ACIMA DE R$ 1.000,00')
print(f'O PRODUTO MAIS BARATO FOI {barato} ELE CUSTA R${menor:.2f}')