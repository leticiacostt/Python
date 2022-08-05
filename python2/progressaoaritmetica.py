''' DESAFIO 51
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
'''
print(10*'-=', 'TERMOS DE UMA PA', 10*'-=')
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao #formula enesimo termo de uma PA
for c in range(termo, decimo + razao, razao):
    print("{} ".format(c), end= "→ ")
print("ACABOU")