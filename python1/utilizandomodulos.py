import math #ou form math import sqrt (2 forma)
num = int(input("Digite um número: "))
raiz = math.sqrt(num) #caso utilize a segunda forma
#print("A raiz de {} é igual a {}".format(num, raiz)) //vou mandar arredondar a raiz no ex abaixo
print("A raiz de {} é igual a {}".format(num, math.ceil(raiz)))  #para arrendondar para baixo math.floor(raiz)
