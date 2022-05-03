'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''
valorcasa = float(input("Qual o valor da casa?R$ "))
salario = float(input("Qual o seu salário?R$ "))
anos = int(input("Em quanto anos você pretende pagar? "))
prestacao = valorcasa/(anos *12)
minimo = salario * 30/100
print("Para pagar uma casa de R${:.2f} em {} anos.".format(valorcasa, anos), end="") #isso é para colocar a linha debaixo junto com essa
print("A prestação será de R${:.2f}".format(prestacao))
if prestacao <= minimo:
    print("Empréstimo pode ser concedido!")
else:
    print("Empréstimo negado!")