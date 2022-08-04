'''
DESAFIO 41
A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''
from datetime import date
atual = date.today().year
nascimento = int(input('Qual o seu ano de nascimento? '))
idade = atual - nascimento
print('O atelta tem {} anos.'.format(idade))
if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JÚNIOR')
elif idade <= 25:
    print('Atleta SÊNIOR')
elif idade > 25:
    print('Atleta MASTER')
#DEU ERRO. CONSERTAR.
