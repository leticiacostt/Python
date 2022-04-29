#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("Digite um número: "))
resultado = num % 2
#print("O resultado é {}".format(resultado)) --- não mostrar para o usuário
if resultado == 0:
    print("Esse número é PAR!")
else:
    print("Esse número é ÍMPAR!")
