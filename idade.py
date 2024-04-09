name = str(input("Qual seu nome? "))
idade = float(input("Qual sua idade? "))
if idade <= 13:
    print ("Criança")
elif idade >= 13 and idade <= 17:
    print ("Adolescente")
elif idade >= 18 and idade <= 59:
    print ("Adulto")
elif idade >= 60:
    print ("Idoso")
else:
    print("FIM")