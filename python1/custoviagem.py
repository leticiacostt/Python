'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e 
R$0,45 para viagens mais longas.
'''
distancia = float(input("Qual a distância da viagem em km? "))
if distancia <= 200:
    preco = 0.50
    passagem = preco*distancia
    print("O preço da sua passagem é de R${:.2f}".format(passagem))
else:
   preco = 0.45
   passagem = preco*distancia
   print("O preço da passagem é de R${:.2f}".format(passagem))
   