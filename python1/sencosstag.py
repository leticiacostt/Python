'''
faça um programa que leia um angulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse angulo.
'''
import math
ang = float(input("Digite o valor do ângulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print("O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}".format(sen, cos, tg)) 