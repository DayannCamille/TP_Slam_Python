#NATATION

"""seance = int(input("Nombre de séances : "))
tarif_a = 145 + (10.50 * seance)
tarif_b = 15.50 * seance
if tarif_a < tarif_b:
    print("Pour", seance," séances, le tarif A est le plus avantageux.")
else:
    print("Pour", seance," séances, le tarif B est le plus avantageux.")
detail = input("Souhaitez-vous plus de détails ? (yes/no) ")
if detail == "yes":
    print("Tarif A :", tarif_a, "euros")
    print("Tarif B :", tarif_b, "euros")
elif detail == "no":
    print("  ")"""


#VOYELLE, CONSONNE OU CARACTERE

"""caractere = input("Saisir un caractère : ")

if caractere in "aeiouy":
    print(caractere, ": voyelle")
elif caractere in "bcdfghjklmnpqrstvwxz":
    print(caractere, ": consonne")
elif caractere in "!()~" :
    print(caractere, ": caractère")"""


#FACTURE

"""HT = float(input("Saisir le prix hors taxe : "))
print("Prix HT :", round(HT,2), "euros")
# calcul prix TTC (TVA = 19.6)
TVA = 19.6
TTC = HT * (1 + TVA / 100)
print("Prix TTC :", round(TTC,2), "euros")
# remise
if TTC < 1000 :
    pourcentage_remise = 0
elif TTC < 2000 :
    pourcentage_remise = 1
elif TTC < 5000 :
    pourcentage_remise = 3
else :
    pourcentage_remise = 5
remise = TTC * pourcentage_remise / 100
print("Remise :", round(remise,2), "euros")
# Net à payer
NetAPayer = TTC - remise
print("Prix Net à payer :", round(NetAPayer,2), "euros")"""

#CALCULATRICE

"""nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
signe = input("Entrez l'opération (addition, soustraction, multiplication, division) : ")

if signe == "addition" :
    operation = nombre1 + nombre2
    print(nombre1, "+", nombre2, "=", operation)
elif signe == "soustraction" :
    operation = nombre1 - nombre2
    print(nombre1, "-", nombre2, "=", operation)
elif signe == "multiplication" :
    operation = nombre1 * nombre2
    print(nombre1, "*", nombre2, "=", operation)
elif signe == "division" :
    operation = nombre1 / nombre2
    print(nombre1, "/", nombre2, "=", operation)
else :
    print("Saisissez le bon signe ! ")"""

#IMPOTS

revenu_a = float(input("Entrez votre revenu annuel : "))

if revenu_a <= 10000 :
    print("L'impôt à payer est de 0 €.")
elif 10001 <= revenu_a <= 25000 :
    impot = (25000-1000)
    print("L'impôt à payer est de 0 €.")