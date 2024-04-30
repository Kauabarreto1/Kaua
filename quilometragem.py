print (" 1 milhas, 2 polegadas, 3 centímetros, 4 quilômetros, 5 metros, 6 pés")
medida = float(input("Qual a distância? "))
N1 = int(input("Digite o numero correspondente: "))

if N1 == 1:
    print ("O número em milhas para polegadas é", medida * 39370)
    print ("Em centímetros é ", medida * 100000)
    print ("Em quilômetros é",  medida / 1000)
    print ("Em pés é", medida * 3281)
    print ("Em metros é", medida * 1609)
elif N1 == 2:
    print ("O número de polegadas para milhas é", medida / 63360)
    print ("Em centímetros é", medida * 254)
    print ("Em quilômetros é", medida / 39370)
    print ("Em pés é", medida / 12)
    print ("Em metros é", medida / 3937)
elif N1 == 3:
    print ("O número de centímetros para milhas é", medida / 160900)
    print ("Em polegadas é", medida / 2,54)
    print ("em quilômetros é", medida / 100000)
    print ("Em metros é", medida / 100)
    print ("Em pés é", medida / 3048)
elif N1 == 4:
    print ("O número de quilômetros para milhas é", medida / 1609)
    print ("Em centímetros é", medida * 100000)
    print ("Em polegadas é", medida * 39370)
    print ("Em metros é", medida / 1603)
    print ("Em pés é", medida * 3281)
elif N1 == 5:
    print ("O número de metros em milhas é", medida / 1609)
    print ("Em centímetros é", medida * 100)
    print ("Em polegadas é", medida * 3937)
    print ("Em pés é", medida * 3281)
    print ("Em quilômetros é", medida / 1000)
elif N1 == 6:
    print ("O número de pés em milhas é", medida / 5280)
    print ("Em polegadas é", medida / 12)
    print ("Em centímetros é", medida * 3048)
    print ("Em quilômetros é", medida / 3281)
    print ("Em metros é", medida / 3281)
else:
    ("ERRO")