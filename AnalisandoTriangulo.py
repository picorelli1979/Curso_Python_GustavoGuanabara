L1 = float(input('Digite o Primeiro Segmento:   '))
L2 = float(input('Digite o Segundo Segmento:    '))
L3 = float(input('Digite o Terceiro Segmento:   '))
if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2 :
    print('TODOS SEGMENTOS DIGITADOS PODEM FORMAR UM TRIÂNGULO')
    if L1 == L2 == L3:
        print('VOCÊ FORMOU UM TRIAGULO : EQUILATERO  COM TODOS IGUAIS')
    elif L1 != L2 != L3 != L1:
        print('VOCÊ FORMOU UM TRIANGULO : ESCALENO COM TODOS LADOS DIFERENTES')
    else:
        print('VOCÊ FORMOU UM TRIANGULO : ISOCELES  COM 2 LADOS IGUAIS')
else:
    print("OS SEGMENTOS DIGITADOS ACIMA NÃO PODEM FORMAR UM TRIÂNGULO")
