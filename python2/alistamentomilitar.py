'''
Faça um programa que leia o ano de nascimento de um jovem 
e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
nascimento = int(input("Em que ano você nasceu? "))
anoatual= 2022
idade = anoatual - nascimento
alistamento = 18
tempo = 18 - idade
print("Sua idade é {}".format(idade))
if idade == 18:
    print("Está na hora de fazer seu alistamento militar!")
elif idade < 18:
    print("Você não tem idade suficiente para se alistar!")
    print("Faltam {} ano(s) para o seu alistamento! Se liga!".format(tempo))
else:
    print("Já passou o tempo de você se alistar... Que pena!")
