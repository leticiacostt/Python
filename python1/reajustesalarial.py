#faça um algoritmo que mostre um salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input("Qual o valor atual do seu salário? R$"))
novo = salario + (salario * 15 /100)
print("Seu salário que antes era de R${:.2f} agora, com aumento de 15%,  fica no valor de R${:.2f}".format(salario, novo)) 