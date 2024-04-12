print ("Verificador de número ímpar/Par")
n1 = int(input("Digite um número: "))
if n1 %2 == 0:
    print ("O número ", n1, "é par.")
    if n1 > 0:
        print("O Numero é Positivo")
    else:
        print("O Numero é Negativo")
elif n1 %3 == 0:
    print ("O número ", n1, "é ímpar.")
    if n1 > 0:
        print("O Numero é Positivo")
    else:
        print("O Numero é Negativo")
else:
    print ("Não foi possível concluir a operação.")