print (" 1 milhas, 2 polegadas, 3 centímetros, 4 quilômetros, 5 metros")
medida = float(input("Qual a distância? "))
N1 = str (input("Digite o numero correspondente "))

if N1 == 1:
    print ("O número em milhas para polegadas é", medida * 39370)
    print ("em centímetros é ", medida * 100000,)
    print ("em quilômetros é",  medida / 1000,)
    print ("em pés é", medida * 3,281,)
    print ("em metros é", medida * 1,609)


