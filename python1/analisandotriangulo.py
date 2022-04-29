'''
Desenvolva um programa que leia o comprimento de três retas e 
diga ao usuário se elas podem ou não formar um triângulo.
'''
print("-=-"*5, "Analisador de Triângulo", "-=-"*5)
r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo")
else:
    print("Os segmentos acima não podem formar um triângulo")
