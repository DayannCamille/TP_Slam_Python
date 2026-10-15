
#PARTIE 1

#CODE PIN

"""code_pin = 4567
code_p = int(input("Saisissez votre code PIN : "))
if code_p != code_pin :
    print("Code incorrect")
else :
    print("Code correct")"""

# SIGNE D'UN NOMBRE

"""nombre = int(input("Saisissez un nombre : "))
if nombre > 0 :
    print("Positif")
elif nombre < 0 :
    print("Negatif")
else :
    print("Nul")"""

# PARITE

"""n_entier = int(input("Saisissez un nombre : "))
if n_entier % 2 == 0 :
    print(n_entier, "est un nombre pair")
else :
    print(n_entier, "est un nombre impair")"""

#AGE

"""age=int(input("Saisissez votre âge : "))
if age < 12 :
    print("A" ,age, "ans, vous êtes un enfant")
elif 12 < age < 18 :
    print("A" ,age, "ans, vous êtes un adolescent")
else :
    print("A" ,age, "ans, vous êtes un adulte")"""


#PERTE OU PROFIT

"""prix_fab = float(input("Saisissez le prix de fabrication : "))
prix_vente = float(input("Saisissez le prix de vente : "))
if prix_fab > prix_vente :
    print("Perte")
else :
    print("Profit")"""


#MAXIMUM

"""nb1 = float(input("Saisissez le premier nombre : "))
nb2 = float(input("Saisissez le deuxième nombre : "))
nb3 = float(input("Saisissez le troisième nombre : "))

if nb1 > nb2 and nb1 > nb3 :
    print("Le maximum est le premier nombre", nb1)
elif nb2 > nb1 and nb2 > nb3 :
    print("Le maximum est le second nombre", nb2)
else :
    print("Le maximum est le troisième nombre", nb3)"""


#TRIANGLE RECTANGLE

"""cote1 = float(input("Saisissez la longueur 1 : "))
cote2 = float(input("Saisissez la longueur 2 : "))
cote3 = float(input("Saisissez la longueur 3 : "))

    if cote3**2 == cote1**2 + cote2**2 :
        print("Ce triangle est rectangle")
    else :
        print("Ce triangle n'est pas rectangle")"""

#POUR ALLER PLUS LOIN

"""cote1 = float(input("Saisissez la longueur 1 : "))
cote2 = float(input("Saisissez la longueur 2 : "))
cote3 = float(input("Saisissez la longueur 3 : "))
if cote1 < cote2 < cote3 :
    if cote3**2 == cote1**2 + cote2**2 :
        print("Ce triangle est rectangle")
    else :
        print("Ce triangle n'est pas rectangle")
else :
    print("Les longueurs n'ont pas été saisies dans l'ordre croissant")"""






#PARTIE 2

#ANNEE BISSEXTILE

"""annee = int(input("Saisissez une année : "))

if (annee % 4 == 0) and (annee % 100 != 0) or (annee % 400 == 0):
    print("L'année", annee, "est bissextile")
else :
    print("L'année", annee, "n'est pas bissextile")"""

#SOCIETE DE TRANSPORT

"""age = int(input("Saisir votre âge : "))
prix = 10

if age < 5 : #Si l'âge est inférieur à 5
    prix_r = prix - 10
    print("Le tarif est de ", prix_r, "€")
elif age < 16 : #Si l'âge est inférieur à 16
    prix_r = prix * 50/100
    print("Le tarif est de ", prix_r, "€")
elif age < 21 : #Si l'âge est inférieur à 21
    prix_r = prix * 60/100
    print("Le tarif est de ", prix_r, "€")
else :
    prix_r = prix * 90/100
    print("Le tarif est de ", prix_r, "€")"""


#VOYAGE SCOLAIRE

"""nb_eleves = int(input("Saisir le nombre d'élèves : "))
nb_jours = int(input("Saisir la durée du voyage : "))

nourriture = 3.50 * nb_jours #Calcul le prix total de nourriture par élève

if nb_eleves < 25 : #S'il y'a 25 élèves ou moins
    cout_transport = 110 #Le coût du transport est de 110 €
else :
    cout_transport = 100 #Le coût du transport est de 100 €

if nb_eleves < 20 : #S'il y'a 20 élèves ou moins
    heberg = 4.20 * nb_jours #L'hébergement coûte 4.20€ par jour
elif 20 < nb_eleves < 35 : #Si le nombre d'élèves est entre 20 et 35
    heberg = 3.80 * nb_jours #L'hébergement coûte 3.80€ par jour
else :
    heberg = 4.00 * nb_jours #L'hébergement coûte 4.00€ par jour

total = cout_transport + nourriture + heberg #Variable qui calcule le tout

print("Le prix du voyage revient à", total, "euros par élève.")"""


#VINCI LOCATION

"""type_v = int(input("Type de véhicule : Citadine -> 1 , Berline -> 2 , Sportive -> 3 : ")) #Saisir le type de véhicule
type_c = int(input("Carburant : Essence -> 1 , Diesel -> 2 : ")) #Saisir le carburant
duree_l = int(input("Durée de  location en jour : ")) #Saisir la durée de location en jour
nombre_k = int(input("Distance en km : ")) #Saisir la distance en km
offre_c = int(input("Offre acceptée : Oui -> 0 , Non -> 1 : ")) #Si l'offre est acceptée, 0 sinon 1

if type_v == 1 : #Si la voiture est Citadine
    montant_l = 80 * duree_l #Prix multipliée par le nombre de jours loués
elif type_v == 2 : #Si la voiture est Berline
    montant_l = 100 * duree_l #Prix multipliée par le nombre de jours loués
elif type_v == 3 : #Si la voiture est Sportive
    montant_l = 130 * duree_l #Prix multipliée par le nombre de jours loués
else :
    print("Saisissez le bon chiffre")

if type_c == 1 : #Si le carburant est essence
    montant_c = 1.93 * nombre_k #Prix multipliée par le nombre de km
elif type_c == 2 : #Si le carburant est Diesel
    montant_c = 1.89 * nombre_k #Prix multipliée par le nombre de km
else :
    print("Saisissez le bon chiffre")

if offre_c == 0 : #Si le client a accepté l'offre commerciale
    calcul = ((montant_l + montant_c) * 0.9) + 30 #Somme des montants de carburants et location, multiplié par la remise et les frais de dossier
    print("Le prix total de la location est de", calcul, "euros.")
else : #Si le client n'a pas accepté l'offre commerciale
    calcul = (montant_l + montant_c) * 0.9 #Somme des montants de carburants et location, multiplié par la remise
    print("Le prix total de la location est de", calcul, "euros.")"""