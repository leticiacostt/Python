'''
Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juro
'''

print(10*"-=-", "DANIELE SEMIJÓIAS", 10*"-=-")
preco = float(input("Qual o preço do produto?R$ "))
print("FORMAS DA PAGAMENTO")
print('''
[1] à vista dinheiro/chuque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input("Qual a opção? "))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print("Sua compra será parcelada em 2x de {:.2f} sem juros".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total/totparc
    print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(totparc, parcela))
else:
    total = 0
    print("Opção inválida de pagamento. Tente novamente.")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))
    