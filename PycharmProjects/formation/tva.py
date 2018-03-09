from six.moves import input # Pour être compatible avec Python3

#reponse = input("Entrer le prix HT de votre produit:") # input: une fonction permet d'entrer d'entrer quelque chose depuis le clavier
#print(reponse)

# 1 Demander le taux de tva du produit en pourcentage
# 2 calculer et afficher le prix ttc du produit
reponse = input ("Entrer le prix HT du produit : ")
prix_ht = float(reponse)
reponse = input ("Entrer le taux de TVA en % : ")
tva = float(reponse)
prix_ttc = prix_ht + (prix_ht * tva)/100
print( "Prix TTC : " + str(prix_ttc))
