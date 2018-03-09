from  decimal import Decimal
nombre = 7

# 1) Demander à l'utilisateur d'entrer un nombre, tant qu'il n'a pas deviné notre nombre.
# 2) Si le nombre entré est trop grand, afficher "Moins !", s'il est trop petit, afficher "Plus !"

var = None
while var != nombre:
    var = input("Enter un nombre: ")
    if var.isdecimal(): #tester que c'est bien des chiffres
        var = int(var)
        if var > nombre:
            print("Moins")
        elif var < nombre:
            print("Plus")
print("Bravo !")

