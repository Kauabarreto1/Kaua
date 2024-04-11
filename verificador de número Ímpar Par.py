print ("Verificador de número ímpar/Par")

n1 = int(input("Digite um número: "))
if n1 %2 == 0:
    print ("O número ", n1, "é par.")
elif n1 %3 == 0:
    print ("O número ", n1, "é ímpar.")
else:
    print ("Não foi possível concluir a operação.")