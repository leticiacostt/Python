'''
 -Escreva um programa que leia a velocidade de um carro. 
 -Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
- A multa vai custar R$7,00 por cada Km acima do limite.
'''
vel = float(input("Qual a velocidade do carro? "))
print("A velocidade do carro é {}km/h".format(vel))
if vel > 80:
    print("ih, deu ruim, cara...Você foi MULTADO!")
    multa = (vel-80) * 7
    print("Sua multa é de R${:.2f}".format(multa))
else:
    print("Você está dentro dos limites de velocidade! Siga em frente :)") 
    