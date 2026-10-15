# Collecte d'informations

nom_prenom = input("Saisir votre nom et votre prénom : ")
ad_mail = input("Saisir votre adresse mail : ")
numero = input("Saisir votre numéro de téléphone : ")
poste = input("Quel est le poste recherché ? : ")
entreprise = input("Quel entreprise voulez-vous cibler ? : ")

# Valeurs initiées
print("Nom & Prénom",nom_prenom)
print("Adresse Mail",ad_mail)
print("Numéro de téléphone",numero)
print("Poste recherché",poste)
print("Entreprise ciblé",entreprise)

#Texte avec F String

texte_fstring = f"Bonjour, je m'appelle, {nom_prenom} et je vous contacte pour déposer ma candidature pour le poste de {poste}, que vous avez déposé sur Indeed,\nVous pouvez me contacter au {numero} ou via l'adresse mail {ad_mail}\nCordialement,\n{nom_prenom}."

#Texte sans F String

print("Bonjour, je m'appelle",nom_prenom,"et je vous contacte pour déposer ma candidature pour le poste de",poste,"que vous avez déposé sur Indeed,\nVous pouvez me contacter au",numero,"ou via l'adresse mail",ad_mail,"\nCordialement,\n",nom_prenom)
print(texte_fstring)