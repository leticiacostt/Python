'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
print(15*"-=-")
print("A CONTAGEM REGRESSIVA VAI COMEÇAR...")
print(15*"-=-")
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print("BUM!BUM! POW!")
