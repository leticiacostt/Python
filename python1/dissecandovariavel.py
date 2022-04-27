#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo 
#e todas as informações posíveis sobre ele

a = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(a))
print("Só tem espaços? ", a.isspace())
print("É número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("Está em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())
