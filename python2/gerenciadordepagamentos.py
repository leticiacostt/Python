'''
DESAFIO 44
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juro
'''
print('{:=^40}'.format(' DANIELE SEMIJÓIAS '))
preco = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x no cartão''')
opcao = int(input(' Qual é a opção? '))
if opcao == 1:
    tot = preco - (preco * 10/100) #esse é o cálculo da porcentagem
elif opcao == 2:
    tot = preco - (preco * 5/100)
elif opcao == 3:
    tot = preco
    parcela = tot / 2
    print('Sua compra será parcelada em 2x de {}'.format(parcela))
elif opcao == 4:
    tot = preco + (preco * 20/100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = tot/ totparcela
    print('Sua compra será parcelada em {}x de {}'.format(totparcela, parcela))
else: 
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('O pagamento será de {} reais'.format(tot))   