#faça um programa que leia a largura e altura de uma parede em metros. Calcule a sua área e a
#quantidade de tintas necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área 
#de 2m²

larg = float(input("Qual a largura da parede? "))
alt = float(input("Qual a altura da parede? "))
area = larg * alt
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(larg, alt, area))
tinta = area / 2
print("Para pintar essa parede você precisa de {}L de tinta".format(tinta))
