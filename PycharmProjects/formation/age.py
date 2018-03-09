from datetime import date


aujourdhui = date.today()
print(aujourdhui)
print(aujourdhui.year)
print(aujourdhui.month)
print(aujourdhui.day)

# 1) Demander l'année de naissance de l'utilisateur
# 2) Demander le mois de naissance de l'utilisateur
# 3) Demander le jour de naissance de l'utilisateur#
# 4) Déterminer et afficher l'âge de l'utilisateur

annee_de_naissance = input("Entrez votre annee de naissance: ")
annee_de_naissance = int(annee_de_naissance)
mois_de_naissane = input("Entrez votre mois de naissance: ")
mois_de_naissane = int(mois_de_naissane)
jour_de_naissance = input("Entrez votre jour de naissance: ")
jour_de_naissance = int(jour_de_naissance)
age = aujourdhui.year - annee_de_naissance
age = int(age)

if mois_de_naissane > aujourdhui.month or aujourdhui.month == mois_de_naissane and aujourdhui.day > jour_de_naissance:
    age = age - 1
print("Vous avez " + str(age)+ " ans")


