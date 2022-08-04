'''
DESAFIO 36
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valorcasa = float(input('Digite o valor da sua casa: R$'))
salario = float(input('Digite o valor seu salário: R$'))
anos = int(input('Em quantos anos você pretende pagar?'))
prestacao = valorcasa / (anos * 12)
minimo = salario * 30/100
print( 'Para pagar uma casa de R${:.2f} em {} anos'.format(valorcasa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')