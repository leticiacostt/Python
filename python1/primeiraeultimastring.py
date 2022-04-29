'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
frase = str(input("Digite uma frase: ")).upper().strip() #jogando a string pra maiúsculo(upper) pra não dar erro no primeiro print
print("A letra A aparece {} vezes".format(frase.count("A"))) #primeiro print
print("A primeira posição de A é {}".format(frase.find("A")+1))
print("A ultima posição de A é {}".format(frase.rfind("A")+1))