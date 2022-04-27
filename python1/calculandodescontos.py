#faça um algoritimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto

preco = float(input("Qual é o preço do produto? R$ "))
novo = preco - (preco * 5 /100)
print("O produto que custava R${:.2f}, com o desconto de 5% passa a custar R${:.2f}".format(preco, novo))
