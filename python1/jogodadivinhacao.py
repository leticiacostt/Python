'''
 -Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
 -peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
 -O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint #vai escolher algo aleatório
from time import sleep #o computador meio que dorme por alguns segundos
comp = randint(0, 5)
#print("Pensei no número {}...".format(comp)) ---> não mostrar para o usuário a resposta
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" *20)
jogador = int(input("Em que número eu pensei? ")) #jogador tentando adivinhar
print("Processando...")
sleep(2)
if jogador == comp:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("Ganhei! Eu pensei no número {} e não no número {}!".format(comp, jogador))   
    