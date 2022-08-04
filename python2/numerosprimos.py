'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0: 
        print('{} é um número primo!'.format(c), end='') 
        tot += 1
    else:
        print('{} não é um número primo!'.format(c), end='') 
    print('{}'.format(c), end='')
print('O número {} foi divisível {} vezes'.format(num, tot))