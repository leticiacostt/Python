'''
Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 1 para binário, 
2 para octal e 3 para hexadecimal.
'''
import math
numero = int(input("Digite um número: "))
base = int(input("Qual será a base de conversão? (1)binário, (2)octal, (3)hexadecimal? "))
if base == 1:
    print("O valor de {} em binário é {}".format(numero, bin(numero)[2:]))
elif base == 2:
    print("O valor {} em octa é {}".format(numero, oct(numero)[2:]))
elif base == 3:
    print("O valor {} em hexadecimal é {}".format(numero, hex(numero)[2:]))
else:
    print("Opção inválida. Tente de novo.")
