'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
print(10 * "-=-", "GAME", 10  * "-=-")
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0, 2)
print('''
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input("Qual é a sua jogada? "))
print("-=-" * 10)
print("O computador jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print("-=-" * 10)
if computador == 0: #jogou pedra
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador vence")
    elif jogador == 2:
        print("Computador vence")
    else: 
        print("Jogada inválida")
elif computador == 1: #jogou papel
    if jogador == 0:
        print("Computador vence")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador vence")
    else: 
        print("Jogada inválida")
elif computador == 2: #jogou tesoura
    if jogador == 0:
        print("Jogador vence")
    elif jogador == 1:
        print("Computador vence")
    elif jogador == 2:
        print("Empate")
    else: 
        print("Jogada inválida")
