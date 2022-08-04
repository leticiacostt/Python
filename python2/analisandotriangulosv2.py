'''
DESAFIO 42
Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
'''
print("-=-"*10, "Analisador de Triângulo", "-=-"*10)
r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))
if r1< r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo', end= '')
    if r1 == r2 == r3:
        print(' EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('Os segmentos não podem formar um triângulo!')
