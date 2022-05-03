'''
A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''
nascimento = int(input("Digite o ano de nascimento: "))
anoatual = 2022
idade = 2022 - nascimento
print("Sua idade é {}.".format(idade))
if idade <= 9:
    print("Atleta MIRIM")
if idade <= 14: #não preciso adicionar o >9 aqui pois o programa já entende isso com o comando anterior
    print("Atleta INFANTIL")
if idade <= 19:
    print("Atleta JÙNIOR")
elif idade <= 25:
    print("Atleta SÊNIOR")
elif idade > 25:
    print("Atleta MASTER")
