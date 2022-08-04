#crie um programa que leia um número real qualquer pelo teclado
#e mostre na tela a sua porção inteira
#ex: digite um número: 6.127, e apareça 6.

import math
num = float(input("Digite um número: "))
#int = math.trunc(num) ou
#print("A valor digitado foi {} e a sua porção inteira é {}".format(num, int))
print("A valor digitado foi {} e a sua porção inteira é {}".format(num, math.trunc(num))) 
