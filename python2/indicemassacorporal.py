'''
 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
 calcule seu Índice de Massa Corporal (IMC) 
 e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
'''
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso/(altura**2)
print("Com o seu peso sendo {:.2f} e sua altura sendo {:.2f}, seu índice de massa corporal será {:.2f}".format(peso, altura, imc))
if imc <18.5:
    print("Você está abaixo do PESO IDEAL")
elif imc == 18.5 and imc <= 25:
    print("Você está no PESO IDEAL")
elif imc <= 30:
    print("Você está com SOBREPESO")
elif imc <= 40:
    print("Você está com OBESIDADE")
elif imc > 40:
    print("Você está com OBESIDADE MÓRBIDA")