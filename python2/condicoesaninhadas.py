#Estudando sobre estrutura condicional aninhada- iniciando python mundo 2
nome = str(input('Qual o seu nome?'))
if nome == 'Leticia':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
else: 
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format (nome))