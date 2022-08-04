'''
DESAFIO 37
Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 1 para binário, 
2 para octal e 3 para hexadecimal.
'''
import math
numero = int(input('Digite um número: '))
opcao = int(input('Você deseja converter o número para qual base numérica? (1)Binário, (2)Octal ou (3)Hexadecimal? Escolha sua opção: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida! Tente novamente.')
