#desenvolva um programa que desenvolva as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) /2
print("A média é: {:.1f} ".format(media))