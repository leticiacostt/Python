'''
Desafio 39
Faça um programa que leia o ano de nascimento de um jovem 
e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
Dica: verificar se o sexo é feminino ou masculino, pois o alistamento no Brasil é obrigatório apenas para homens.
'''
from datetime import date
from re import M
atual = date.today().year #para pegar o ano atual
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
sexo = str(input('Qual o seu sexo? (F) Feminino ou (M) Masculino? '))
if sexo == 'M':
    print('Pessoas do sexo MASCULINO são obrigadas a se alistar!')
    print('Quem nasceu em {}, tem {} anos.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem idade suficiente para se alistar! Ainda faltam {} anos para o seu alisatamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:    
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos!'. format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif sexo == 'F':
    print('Pessoas do sexo FEMININO não são obrigadas a se alistar!')
else:
    print('Opção inválida!')

