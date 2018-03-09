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


class CategorieOuModele:
    pass


class Unite(object):
    """
    Cette classe représente une unité dans un jeu que nous vendons 1 milliards d'euros / pièce.
    """
    # nom = None
    # x = None
    # y = None
    # vie = None
    # force = None

    VIE_MAX = 100

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
        self._nom = nom  # attribut protégé
        self.x = x
        self.y = y
        self.vie = vie
        self.force = force
        self.__fichier = 'unite.json'  # attribut privé

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
        print("{} se repose et regagne 1 point de vie.".format(self._nom))
        self.vie += 1

    def __str__(self):
        """
        Renvoie une représentation de l'unité sous forme de chaîne de caractères.

        :return: la chaîne de caractère représentant l'unité
        :rtype: str
        """
        return "<Unite nom:{} x:{} y:{} vie:{} force:{}>".format(self._nom, self.x, self.y, self.vie, self.force)

    def __lt__(self, autre):  # lt = lower than <
        return self.vie < autre.vie

    def __gt__(self, autre):  # gt = greater than >
        return self.vie > autre.vie

    def __le__(self, autre):  # le = lower or equal <=
        return self.vie <= autre.vie

    def __ge__(self, autre):  # ge = greater or equal >=
        return self.vie >= autre.vie

    def __eq__(self, autre):  # eq = equals
        return self.vie == autre.vie

    def __ne__(self, autre):  # ne = not equals
        return self.vie != autre.vie


mechant = Unite('méchant', 12, 7, 42, 9)  # instanciation de l'objet
# mechant est une instance de la classe Unite
# mechant.nom = 'méchant'
# mechant.x = 12
# mechant.y = 7
# mechant.vie = 42
# mechant.force = 9
mechant.defense = 5
print(mechant.defense)

gentil = Unite('gentil', 11, 7, 8, 3)
# print(gentil.defense)

gentil.attaque(mechant)
print(mechant.vie)
Unite.attaque(gentil, mechant)
print(mechant.vie)

mechant.se_repose()
# méchant se repose et regagne 1 point de vie.
print(mechant.vie)

print(mechant)
print(str(mechant))
print(mechant.__str__())
chaine = mechant.__str__()

# gentil.attaque(123)

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
print(mechant.__dict__)

# Héritage
# ========


# class Guerrier(Unite, Tank, Affichable):
class Guerrier(Unite):
    # Unite est la superclasse de Guerrier

    def __init__(self, nom, x, y, vie, force, rage=100):
        # super().__init__(nom, x, y, vie, force)  # Python 3
        # Tank.__init__(self)
        # Affichable.__init__(self)
        Unite.__init__(self, nom, x, y, vie, force)
        self.rage = rage
        # self.__fichier = 'guerrier.json'
        # print("***", dir(self))
        # print(self.__fichier)
        # print(self._Unite__fichier)  # déconseillé

    def __str__(self):
        return "<Guerrier nom:{} x:{} y:{} vie:{} force:{} rage:{}>".format(self._nom, self.x, self.y, self.vie, self.force, self.rage)

    def frappe_heroique(self, cible):

        """
        Exécute une frappe héroïque.

        :param cible: cible de la frapep
        :type cible: Unite
        """
        # if not isinstance(cible, Unite):
        #     print("*** La cible n'est pas une Unite !")
        #     return

        if self.rage < 20:
            print("*** Echec de la frappe héroïque !")
            return
        print("{} exécute une frappe héroïque sur {} !".format(self._nom, cible._nom))
        cible.vie -= self.force * 2
        self.rage -= 20


conan = Guerrier('Conan', 11, 8, 10000, 20, 50)
conan.attaque(mechant)
print(mechant)
print(conan)

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

print(conan._nom)  # déconseillé
#conan._nom = 'fichier.json'
print(conan._Unite__fichier)  # déconseillé

hercule = Guerrier('Hercule', 1, 2, 3, 4)
hercule.frappe_heroique(conan)
print(conan)

# isinstance
# ==========


print(isinstance(gentil, Unite)) # permet de tester l'héritage
print(isinstance(gentil, Guerrier))
print(isinstance(conan, Unite))
print(isinstance(conan, Guerrier))
print(type(conan))
print(type(conan) is Guerrier) # test s'ils sont de même type
print(type(conan) is Unite)


# Classe de service
# =================
# Sert à grouper les fonctions

class TextFormat:

    def souligner(self, texte):
        print(texte)
        print('=' * len(texte))

    @staticmethod # permet de ne pas mettre self
    def encadrer(texte):
        print('#' * (len(texte) + 4))
        print('#', texte, '#')
        print('#' * (len(texte) + 4))

    def espacer(self, texte):
        caracteres = list(texte)
        # print(caracteres)
        print(' '.join(caracteres))


t = TextFormat()
t.souligner("Appel de souligner()")
t.encadrer("Est-ce que ça marche ?")

TextFormat.encadrer("Texte à encadrer")

# Agrégation
# ==========

class Familier:
    proprietaire = None  # agrégation


chien = Familier()
chien.proprietaire = conan

class Personnage:
    inventaire = [] # agrégation


    def ramasse(self, accessoire):
        self.inventaire.append(accessoire)

class Accessoire:
    pass


harry = Personnage()
baguette = Accessoire()
harry.ramasse(baguette)

# Les exceptions : sont des class
# ===============


# 1/0  # ZeroDivisionError: division by zero

# l = [1, 2, 3]
# l[100]  # IndexError: list index out of range

try:
    print("On va faire quelque chose de mal :")
    1 / 0
    print("Ceci ne s'affiche jamais.")
except ArithmeticError as e:
    print("*** Vous avez fait une erreur arithmétique !")
    print(e)
    print(type(e))
# except ZeroDivisionError:
#     print("*** Vous avez divisé par zéro !")
except:
    print("*** Une exception s'est déclenchée, ceci capture toute les excéptions !")


# protocole = 'gsfdgfsdgsd'
protocole = 'http'

if protocole not in ('http', 'https', 'ftp', 'ssh'):
    raise ValueError("Protocole non supporté !") # Déclenche une exception crée à la main


# Le bubbling avec les exceptions
# ===============================


def a():
    b()


def b():
    c(10, 0)

def c(dividende, diviseur):

    f = None

    try:
        f = open('fichier.txt') # dans try s'il y a une excéption, alors les autres blocs ne seront pas exécute,
        dividende / diviseur # direcement dans except, try, except et finally vont ensemble
        # f.close()
    except IndexError:
        print("*** Cette fois-ci, vous avez dépassé les bornes !")
    else:
        print("Tout s'est bien passé, aucune exception n'a été déclenchée.")
    finally:
        print("Ceci s'exécute tout le temps à la sortie du bloc de capture d'exception.")
        f.close()

    try:
        a()
    except ZeroDivisionError:
        print("*** Vous avez divisé par zéro !")


# Créer nos propres exceptions
# ============================


class ProblemeMajeurError(Exception): # Exception est une class de base python
    pass


try:
    raise ProblemeMajeurError()
except ProblemeMajeurError:
    print("*** Un problème grave est survenu !!!")

# Les accesseurs (getter, setter)
#  ===============================
# C'est pour accéder aux attibuts privée


class Personnage:

    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    # Accesseurs façon Java et PHP :

    def set_nom(self, valeur):
        if type(valeur) is not str:
            raise ValueError("Cher collègue, tu as écrit n'importe quoi !")
        self.__nom = valeur

    def get_nom(self):
        return "Monsieur " + self.__nom

    # Accesseur façon Python :

    @property # decorateur de base de python
    def age(self):
        print("Appel du getter de age...")
        return self.__age

    @age.setter
    def age(self, valeur):
        print("Appel du setter de age...")
        self.__age = valeur


harry = Personnage('Harry Potter', 12)
harry.set_nom('Voldemort')
print(harry.get_nom())

# harry.set_nom(123)

print(harry.age)
harry.age = 13


# Décorateurs
#============
from time import time

def decorateur(autre_fonction):

    def fonction_de_remplacement():
        print("Exécuter quelque chose avant...")
        start = time()
        autre_fonction()
        end = time()
        print("Exécuter quelque chose après...")
        print("Nombre de secondes pour exécuter la fonction :", end - start)

    return fonction_de_remplacement

@decorateur # appel du decorateur sur la fonction compteur
def compteur():
    for i in range(5):
        print(i)


#compteur = decorateur(compteur) # une autre facon d'appeler le décorateur

compteur()

# Contextes
# =========



class Chrono:

    def __enter__(self):
        self.start = time()

    def __exit__(self, *exc):
        self.end = time()
        print(self.end - self.start)


with Chrono() as c:
    for i in range(1000000):
        print(i)


