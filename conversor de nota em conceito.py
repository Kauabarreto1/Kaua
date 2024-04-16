nota = float(input("Qual a sua nota? "))
if nota >= 9:
    print ("Você tirou nota A.")
elif nota >= 7.5 and nota <= 9:
    print ("Sua nota foi B.")
elif nota >= 6 and nota <= 7.5:
    print ("Sua nota foi C")
elif nota >= 4 and nota <= 6:
    print ("Sua nota foi D.")
elif nota <= 3.9:
    print ("Sua nota foi F, Você foi reprovado.")
else :
    print ("fim")