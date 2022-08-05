''' DESAFIO 50
 Desenvolva um programa que leia seis números inteiros 
 e mostre a soma apenas daqueles que forem pares. 
 Se o valor digitado for ímpar, desconsidere-o.
'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Ditgite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num #vai informar a soma
        cont += 1 #vai informar a quantidade de números
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))