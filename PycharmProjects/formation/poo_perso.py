
# programme sans objet

unite1 = {
    'nom': 'méchant',
    'x': 12,
    'y': 7,
    'vie': 42,
    'force': 9
}
unite2 = {
    'nom': 'gentil',
    'x': 11,
    'y': 7,
    'vie': 8,
    'force': 3
}



def attaque(attaquant, cible):
    print("{} attaque {} !".format(attaquant['nom'], cible['nom']))
    cible['vie'] -= attaquant['force']


attaque(unite1, unite2)
print(unite2)

# Programmation objet
# class c'est des catégorie d'objet ou model

class CategorieOuModele:
    pass


class Unite:
    """
    Ici documentation de la classe
    Cette classe représente une unité dans un jeu que nous vendons 1 milliards d'euros / pièce.

    """
    # nom = None # on peux ne pas les mettres ici, car on peut créer à la voler les attributs, on le
    # x = None# déclare uniquement dans le constructeur
    # y = None
    # vie = None
    # force = None
    VIE_MAX = 100

# Constructeur
    def __init__(self, nom, x, y, vie, force):

        """
        Constructeur de la classe unité.

        :param nom: nom de l'unité
        :type nom: str
        :param x: abscisse de l'unité
        :type x: int
        :param y: ordonnée de l'unité
        :type y: int
        :param vie: points de vie de l'unité
        :type vie: int
        :param force: force de l'unité
        :type force: int
        """
        super().__init__()

        self._nom = nom
        self.x = x
        self.y = y
        self.vie = vie
        self.force = force

    def attaque(self, cible):
        """
        Cette méthode sert à attaquer une unité.

        :param cible: cible de l'attaque
        :type cible: Unite
        """
        print("{} attaque {} !".format(self._nom, cible._nom))
        cible.vie -= self.force

    def se_repose(self):
        """
        Sert à regagner un point de vie.
        """
        print("{} se repose et regagne 1 point de vie".format(self._nom))
        self.vie += 1

    def __str__(self): # permet d'afficher un objet de façon compréhensible
        """
        Renvoie une représentation de l'unité sous forme de chaîne de caractères.

        :return: la chaîne de caractère représentant l'unité
        :rtype: str
        """
        return "<Unite nom:{} x:{} y:{} vie:{} force:{}>".format(self._nom, self.x, self.y, self.vie, self.force)
    # Les opérateurs ne fontionne pas par défaut sur les objets qu'on a défini, Il faut les redéfinir
    # et l'adapter à notre besoin
    def __lt__(self, autre):  # lt = lower than <
        return self.vie < autre.vie

    def __gt__(self, autre):  # gt = greater than >
        return self.vie > autre.vie

    def __le__(self, autre):  # le = lower or equal <=
        return self.vie <= autre.vie

    def __gt__(self, autre):  # gt = greater than >
        return self.vie > autre.vie

#mechant = Unite()  # instanciation de l'objet
# mechant est une instance de la classe Unite

mechant = Unite('méchant', 12, 7, 42, 9)  # instanciation de l'objet
# mechant.nom = 'méchant'
# mechant.x = 12
# mechant.y = 7
# mechant.vie = 42
# mechant.force = 9
mechant.defense = 5 # on peut aussi crée à la voler un attribut,
print(mechant.defense)

# pour accéder au attribut, on fait <objet>.<attribut>

gentil = Unite('gentil', 11, 7, 8, 3)
# print(gentil.defense)

gentil.attaque(mechant)
print(mechant.vie)
Unite.attaque(gentil, mechant) # c'est pareille que gentil.attaque(mechant) mais pas très utilisé
print(mechant.vie)

mechant.se_repose()
print(mechant.vie)

print(mechant)
print(str(mechant))
print(mechant.__str__())

# gentil.attaque(123)
# dans la console python
# >>> import poo
# >>> help(poo)
# >>> help(poo.Unite)
# >>> help(poo.Unite.attaque)
# >>> help(print)
# >>> poo.Unite.__doc__
# >>> poo.Unite.attaque.__doc__

print(dir())  # liste de toutes les variables de notre programme
print(dir(mechant))

print(Unite.__lt__)
print(mechant < gentil)


# Héritage
# ========

# class Guerrier(Unite, Tank, Affichable):
class Guerrier(Unite): # la classe Guerrier hérite de tous les méthodes et attibut de la classe Unite
    # unite est la superclasse de Gurrier
    def __init__(self, nom, x, y, vie, force, rage = 100): # ajout d'un nouveau attribut, qui n'existe pas dans la classe parent
        super().__init__(nom, x, y, vie, force) # appel du constructeur de Unite , Python3
        #Unite.__init__(self, nom, x, y, vie, force) # appel du constructeur de Unite , Python2
        #Tank.__init__self)
        #Affichable__init__(self)
        # c'est mieux d'utiliser la syntaxe en python2
        self.rage = rage

    def __str__(self): # en plus de l'héritage on peut redéfinir les méthodes comme on veut
        return "<Guerrier nom:{} x:{} y:{} vie:{} force:{} rage:{}>".format(self._nom, self.x, self.y, self.vie, self.force, self.rage)


    def frappe_heroique(self, cible):
        if self.rage < 20:
            print("*** Echec de la frappe héroïque !")
            return
        print("{} exécute une frappe héroïque sur {} !".format(self._nom, cible._nom))
        cible.vie -= self.force * 2
        self.rage -= 20

conan = Guerrier('Conan', 11, 8, 10000, 20, 50)
conan.attaque(mechant)
print(mechant)

conan.frappe_heroique(mechant)
conan.frappe_heroique(mechant)
conan.frappe_heroique(mechant)
print(mechant)


# Une frappe héroïque consomme 20 de rage
# 1) Si le guerrier n'a pas assez de rage pour exécuter la frappe
# héroïque, afficher un message d'erreur, et annuler la frappe.
# 2) Gérer la consommation de la rage.
# 3) Afficher la rage dans __str__
# 4) Par défaut, un guerrier a 100 de rage.


# Attributs publics, protégés, privés
# ===================================

print(conan._nom)
conan._nom = 'fichier.json'
