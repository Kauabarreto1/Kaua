preco = float(input("Qual o preço do produto? R$"))
desconto = float (input("Qual o valor de desconto? %"))
preco_descontado = preco - (preco * desconto / 100)
print ("O produto que custava", "R$",preco, "com o desconto ficou", "R$",preco_descontado)