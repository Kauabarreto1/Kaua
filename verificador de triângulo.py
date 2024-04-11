n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
if n1 == n2 == n3:
    print ("Este é um triângulo EQUILÁTERO.")
elif n1 == n2 !=n3:
    print ("Este é um triângulo ISÓSCELES.")
elif n1 != n2 != n3:
    print ("Este é um triângulo ESCALENO.")
else :
    print ("Não foi possível formar um triângulo")