'''
faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
import math
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
#hip = (co ** 2 + ca ** 2) ** (1/2) ou
hip = math.hypot(co, ca)
print("O valor da hipotenusa é {:.2f}".format(hip))