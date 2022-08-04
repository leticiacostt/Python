#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$1,00 = R$5.00

real = float(input("Quanto dinheiro você tem na carteira? R$S"))
dolar = real / 5.00
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar)) 
