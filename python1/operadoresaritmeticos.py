#crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n = int(input("Digite um número: "))
print("O dobro de {} é {}, o triplo é {} e a sua raiz é {}".format(n, (n*2), (n*3), (n**(1/2)))) 
#na raiz quadrada também poderia usar pow(n, (1/2)) que é uma função