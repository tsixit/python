# coding:utf-8

from __future__ import division, print_function
#print_function permet d'adapter print en phyton 2 et python3
1 + 1
print (1+1)
print("hello world")
print(1+2*3)
print((1+2)*3)
print(5-2)
print(10/3)# attention: division entière en python 2
print(10.0/3)
print(11%3) # % = modulo=reste de la division entière
print(5**2)# puissance
print(round(6.9))
print(round(6.12345,2))

x=3
print(x)
largeur = 3
print(largeur)
hauteur = 5*9
print(hauteur)
aire = largeur * hauteur
print(aire)
#print(n)


#Chaine de caractère
print('abc')
print("je vais à l'école")
print("ça s'appele une \"pomme\".")
print("-python\n-ruby\n-perl")
print("colonne 1\t colonne2\t colonne 3")
print("c:\\nvidia")
print(r"c:\nicolas\toto\nvidia") #r = raw: permet de ne pas ajouter à chaque fois le \
print("""
"Dawan Paris":
  11, rue Antoine Bourdelle
  75015 Paris
""")#les trilpes guillemets permettent aussi de délimmiter


#concaténation
print("hello " + "world")
print("=" * 10)# Multiplier la chaine de caractère

#Le slicing(tranchage) avec les chaine de caractères
#=====================================================
mot="python"
print(mot[0])
print(mot[5])
print(mot[-1])#le dernier caractère, les indexes en python commence à 0
print(mot[-2])
print(mot[0:2])# le slicing; la deuxième borne est tojours exclu
print(mot[2:5])
print(mot[:2])# depuis le début jusqu'au cactère num 2
print(mot[2:])
print(mot[-2:])
print(mot[4:42])
print(mot[42:])
phrase = "hello zorld!"
#phrase[6] = "W" #TypeError: str object does not support item assignement.
# on ne peut pas modifier directement un caractère au milieur d'une chaine dans python
phrase2 = phrase[0:6] + "W"+ phrase[7:]
print(phrase2)
print(len(phrase2))# len() retorne le nombre de caractère
print(len("é"))# En python3 toutes les chaines sont en Unicode, Ajouter u en python2 pour être compatible
print(len(u"é"))


maVariableFlotante = 2.3 #Camel case
ma_variable_flottante = 2.3 #snake_case
print(1.1 + 1.1 + 1.1)

from decimal import Decimal
prix = Decimal("1.1")# Pour arrondir les nombres décimaux
print(prix + prix + prix )

print(type(ma_variable_flottante))
print(type(aire))
print(type(phrase))

#conversion de type de variable
#==============================
print("Superficie du terrain: " + str(aire))
print(123 + int("456"))
print(123.456 + float("789.101112"))

# Interpolation de chaine de caractère
#======================================
nom="Damien"
age = 30
print("Je m'appelle " + nom + "et j'ai " + str(age) +  " ans.")
print("Je m'appelle %s." % nom)# %s = string; obsolète
print("Je m'appelle %s et j'ai %d ans" % (nom,age))# %d = int; obsolète
# %s= string
# %d=int
# %f = float
print("je m'appelle {} et j'ai {} ans".format(nom, age))
motif = "je m'appelle {} et j'ai {} ans."
print(motif.format(nom, age))
jour = 5
mois = 3
annee = 2018
motif = "Nous sommes le {}/{}/{}"
print(motif.format(jour, mois, annee))

motif= "Today is {1}/{0}/{2}"[]
print(motif.format(jour, mois, annee))

motif = motif= "Today is {month}/{day}/{year}"
print(motif.format(day=jour, month=mois, year=annee))

motif =  "Today is {month:02d}/{day:02d}/{year}"
print(motif.format(day=jour, month=mois, year=annee))

from datetime import date
d = date(annee, mois, jour)
print(d)
print(type(d))
print(d.year)
print(d.month)

#Les tests
#==========
jour_du_mois = 31
if jour_du_mois == 31:
    print("Il faut payer les employés")
    print("Et dépêche-toi s'il te plaît")
print("Suite du programme")

if jour_du_mois == 31:
    pass
print("je vais continuer mon programme...")

age = 20
if age < 18:
    print("Vous n'êtes pas autorisé")
    print("veuillez partir")
else:
    print("Soyez le bienvenu")

print(age >= 18)
print(age <= 18)
print(age != 18)

majeur = False
majeur = True
print(type(majeur))
if majeur:
    print("Vous pouvez visiter ce site")

nom = "Nicolas"
if nom == "Nicolas":
    print("Bienvenu monsieur l'admin")
elif nom == "Damien":
    print("Bienvenu monsieur le visiteur")
elif nom == marc:
    print("Beinvenu Monsieur le développeur")
else:
    print("je ne vous connais pas")

nom = None # Chaine vide
nom = ""
nom= "Nicolas"
if nom: # test s'il variable est vide ou pas. Vide =  false; pas vide = True
    print("Vous avez un  nom")
else:
    print("Vous n'avez pas de nom")

bonbon = None
bonbon = 0 # C'est comme False
bonbon = 5
if bonbon:
    print("Donnez moi un bonbon")

nom = "Paul"
if nom == "Paul" or nom == "Roman" or nom == "Charles":
    print("Bienveneu dans la formation Python")
else:
    print("Vous ne faites pas partie de la formation")

j_ai_paye_les_employes = False
argent = 10

#if j_ai_paye_les_employes == False and argent >= 5:
#if j_ai_paye_les_employes is False and argent >= 5:
if not j_ai_paye_les_employes and argent >= 5:
    print("je dois payer les employés")

## Boucle
i = 0
while i < 3:
    print(i)
    #i = i + 1 ou i += 1
    i += 1

argent = 13
while argent >= 12:
    print("je paie un employé !" )
    argent -= 12
print("je n'ai plus d'argent")

#boucle infinie
# while True:
#     print("itératon")


# Les Listes
restaurents = list() #liste vide
restaurents = [] #liste vide
restaurents = ["l'oncle pom", "le yeti", "au delice", "mcdo", "la taverne", "flunch"]
print(restaurents)
print(restaurents[0])
print(restaurents[2])

i = 0
while i < len(restaurents): # len(): sur une liste retourne la taille d'une liste
    print(i, restaurents[i])
    i += 1
# équivaut à
for restau in restaurents:
    print(restau)
# avec la foncion enumerate() pour afficher les indices
for i, restau in enumerate(restaurents):
    print(i, restau)
# avec la focntion zip()
places = [10, 50, 32, 45, 20, 15]
for restau, chaises in zip(restaurents, places):# zip() : fonction permettant de travailler sur deux listes
    print(restau, chaises)

# On peut mettre  des éléments de types différentes dans une liste
restaurents[2] = "la belle Chaurienne"
print(restaurents)

restaurents.append("Les abattoirs de Carmen")# la méthode append permet d'ajouter un élément à la fin  dans une liste
print(restaurents)

restaurents.insert(2, "L'entrecôte")# insert: méthode qui permet d'inserer un élément
print(restaurents)

dernier = restaurents.pop()# enlever un élément d'une liste
print(dernier)

premier = restaurents.pop(0)
print(restaurents)

print([1, 2, 3] + [4, 5, 6])#Concaténation de deux listes

if "flunch" in restaurents:# in permet de vérifier la présence d'un élément dans une liste
    print("Flunch est dans la,liste")

a, b, c = [1, 2, 3] #Décomposition
print(a)
print(b)
print(c)

for restau in restaurents:
    print(restau)
    if restau == "mcdo":
        break #Arrêter l'itération quand l'élément est trouvé
print("=" * 70)

for restau in restaurents:
    print(restau)
    if restau == "mcdo":
        continue

# Les range
#==========

for i in range(10):
    print(i)
print("=" * 70)

for i in range(1,10):
    print(i)
print("=" * 70)

for i in range(1, 10, 2):
    print(i)
print("=" * 70)

for i in range(1, 10, -1):
    print(i)

# Le slicing (tranchage) sur les listes

nombres = range(100)# nombre ici n'est pas une liste,quand on l'intérroge pas il ne sort pas une liste
nombres = list(range(100)) # là il sort une liste
print(nombres)
print(nombres[12])
print(nombres[5:10]) #slicing
print(nombres[90:]) # de 90 jusqu'à la fin de la liste
print(nombres[:10]) # du début de laiste jusqu'à l'élément 10
print(nombres[24:75:5]) # de 24 à 75 ,avec un pas de 5
print(nombres[49::10]) # de 49 jusqu'à la fin de la liste avec un pas de 10
print(nombres[90:-1])
print(nombres[9::-1])
print(nombres[::-1])# depuis le dernier élément vers le début de la liste (décroissance)

# Itérer sur une chaîne de caractère
#==================================

for caractere in "abcdefg":
    print(caractere)

phrase = "hello zorld!"
caracteres = list(phrase)
print(caracteres)
caracteres[6] = "W"
print(caracteres)
#phrase2 = "-".join(caracteres)# join() méthode crée une chaine de caractère à partir d'une liste
phrase2 = "".join(caracteres)
print(phrase2)

ligne = "dupont,jacques,49,14 rue de la paix,12345"
personne = ligne.split(",")# split() contraire de join(), découpe une chaine de caractère pour créer une liste
print(personne)
print(personne[2])

# Les tuples
#===========

t = tuple() #tuple vide
t = () # tuple
t = (1, 2, 3)
print(t)
print(t[0]) # a la différence d'une liste, les tuples ne sont pas modifiables
print(t[1])
print(t[2]) # les tuples sont immuables (immutables)
# on ne peut pas intervertir les éléments d'un tuple

#t.append(4) # AttribueError; 'tuple object has no atribute 'append'

a, b, c = t
print(a)
print(b)
print(c)

t = ("a")# python ne connait pas que c'est un tuple avec un seul élément
print(t)
print(type(t))

t = ("a", ) # tuple avec un seul élément
print(t)
print(type(t))

a = (1, 2, 3)
for cordonnee in a: # itérer avec les éléments d'un tuple
    print(cordonnee)

plugins = ('database', 'xml', 'http')
if 'xml' in plugins:
    print("Plugins XML disponible")

print(1, 2, 3)# affiche comme des chaines de caractères en  python3, python2 affiche un tuple

# Les dictionnaires
#===================

dictionnaire = dict() # dictionnaire vide
dictionnaire = {} # dictionnaire vide
dictionnaire['maison'] = 'house' # pour accéder aux élément, on mets entrecrochet une chaine de caractère
dictionnaire = dict(maison='house', chaise='chair', porte='door')
dictionnaire = {'maison': 'house', 'chaise':'chair', 'porte':'door'}
print(dictionnaire['maison'])# acceder au valeur de la clé "maison"
print(dictionnaire['chaise'])
print(dictionnaire['porte'])

dictionnaire['fenetre'] = 'window'# ajouter un élément du dictionnaire
print(dictionnaire)

dictionnaire['maison'] = 'home' # changer une valeur
print(dictionnaire)

del dictionnaire['fenetre'] # supprime une clé dans le dictionnaie. Les clés sont uniques
print(dictionnaire)

print(dictionnaire.keys())
for cle in dictionnaire.keys():# boucler sur les clés
    print(cle)

for cle in dictionnaire:
    print(cle, dictionnaire[cle])

print(dictionnaire.values())# dictionnnaire.values affiche les valeurs
for valeur in dictionnaire.values():# boucler sue les valeus
    print(valeur)

#for cle, valeur in dictionnaire.iteritems(): # à partir de python 2.7
for cle, valeur in dictionnaire.items(): #Boucler sur les clée e valeur
    print(cle, valeur)

#print(dictionnaire['table'])# KeyError: 'table'
if 'table' in dictionnaire.keys():# in cherche rpar défaut sur les clé
    # on peut faire if 'table" in dictiionnaire:
    print(dictionnaire['table'])
traduction = dictionnaire.get('table')# get() permet d'acccéder à une valeur, si elle n'exista pas, elle retourne None
print(traduction)

personne = {'nom': 'Dupont', 'prenom':'Jacque', 'age':'49', 'adresse':'14 rue de la paix', 'code_postal':'12345'}
print(personne)
print(personne['age'])


# Les fonctions
#==============

def deux():
    resultat = 1 + 1
    return resultat # return quitte la fonction
    print("Ceci ne s'affiche jamais")
r = deux()
print(r)

def plus_tard():
    pass

def addition(a, b):
    return a + b

print(addition(1, 2))

def souligner(text):
    print("#", text)
    print("#", "=" * len(text))

souligner("Bonjour")

# Un certain titre
#================

def encadrer(text):
    print("#" * (len(text) + 4))
    print("#", text, "#")
    print("#" * (len(text) + 4))


encadrer("Bonfgfg")

###################
# Text à encadrer #
###################

phase = "Hello zorld !"

def change(text, pos, lettre):
    return text[0:pos] + lettre + text[pos + 1:]

phrase2 = change("hello zolrd", 2 , "H")
print(phrase2)

# Etape 1
personnes = [ 'jean', 'paul', 'sophie', 'marc', 'damien', 'nicolas']

def piscine(liste):
    return ",".join(liste) + " vont à la piscine"

# etape 2
# personnes = ['Jean', 'Paul', 'Sophie', 'Marc', 'Damien', 'Nicolas']
# phrase = piscine2(personnes)
# print(phrase)  # Jean, Paul, Sophie, Marc, Damien et Nicolas vont à la piscine.

def piscine2(liste):
    if len(liste) == 1:
        return liste[0] + " va à  la piscine tout seul"
    if len(liste) == 0 or liste is None: # ou if not liste
        return "Personne ne va à la piscine"
    return ",".join(liste[:-1]) + " et " + liste[-1] + " vont à la piscine"

personnes = []
# # Etape 3 :
#
# personnes = ['Nicolas']
# phrase = piscine2(personnes)
# print(phrase)  # Nicolas va à la piscine tout seul.

# # Etape 4 :
#
# personnes = []
# phrase = piscine2(personnes)
# print(phrase)  # Personne ne va à la piscine.

# # Etape 5 :
#
# personnes = None
# phrase = piscine2(personnes)
# print(phrase)  # Personne ne va à la piscine.




phrase = piscine(personnes)
phrase = piscine2(personnes)
print(phrase)


# Retoue Multiple
#================

def multiple():
    return 1, "un"

nombre, chaine = multiple() # un tuple qui reçoie simultanément les valeurs de retour
print(nombre, chaine)

# Variable globale et locale
#===========================

resultat = 123 # resultat est une variable globale
def addition(a, b):
    # global resultat à éviter car fait référence à la variable globale
    resultat = a + b # resultat une variable locale à la fonction
    return resultat

print(addition(2, 3))
print(resultat)

# Designer le paramètres par leur nom
#====================================

def division(dividende, diviseur):
    return dividende / diviseur

print(division(10, 3))
print(division(dividende=10, diviseur=3))
print(division(diviseur=3, dividende=10))


# paramètre par défaut
# =====================
def bonjour(verbose = True):
    if verbose:
        print("je suis en traind'exécuter la focntion bonjour()...")
    print("Bonjour")

bonjour(True)
bonjour(False)
bonjour()

# paramètres en nombre variables
#===============================

def somme(*nombres): # * = opérateur splat : reçois un nombre illimité d'argument et le transforme en une liste
    total = 0
    for nombre in nombres:
        total += nombre
    return total

r = somme(*[1, 2, 3])# liste de nombre: eclate une liste en plusieur arguement
print(r)

r = somme(1, 2, 3, 4)
print(r)

nombres = [1, 2, 3, 4]
r = somme(*nombres)
print(r)

def affiche_recette(nom, **ingredients): # ** pemet de traiter des arguements avec de nom sous forme de dictionnaire
    print(nom)
    for ingredient, quantite in ingredients.items():
        print("- {} : {}".format(ingredient, quantite))


ingredients = {
    'farine': '1kg',
    'levure':'2kg',
    'eau': '3 L',
    'sel': '4kg'
}

#affiche_recette('pain', ingredients)
affiche_recette('Pain', farine='1 kg', levure='2 kg', eau='3 L', sel='4 kg')

f = affiche_recette # on peut mettre une fonction dans une variable
f('Gâteau au chocolat', chocolat='1 kg', beurre='2 kg') # appel de la fonction


# Les tris
#=========
nombres = [5, 7, 2, 3, 9, 4]
nombres.sort()
print(nombres)

fromages = ['Brie', 'Tomme de savoie', 'morbier', 'Munster', 'emmental', 'roquefort', 'brillat-savarin']
fromages_tries = sorted(fromages)
print(fromages_tries)
print(ord('B'))
print(ord('b'))
print('Brie'.lower())


def representant(fromage): # transforme chaque élément en minuscule
    return fromage.lower()

fromages_tries = sorted(fromages, key=representant) # key permet de dire à python de trier par rapport à ce qui est attribuer à l'argument key
# on peut aussi créer une fonction à la voler avec le mot clé "lambda"
#fromages_tries = sorted(fromages, key=lambda fromage: fromage.lower()) # key permet de dire à python de trier par rapport à ce qui est attribuer à l'argument key
# ici fromage est le paramètre en entré
print(fromages_tries)
# sort() et sorted() fonctionne pareille


fromages = [
    ('brie', 3.1),
    ('tomme de savoie', 8),
    ('morbier', 5.5),
    ('munster', 6),
    ('emmental', 2),
    ('roquefort', 6.5),
    ('brillat-savarin', 8.5)
]

#def prix(prix):
 #   return prix[1]

# trier par le prix
fromages_tries = sorted(fromages, key = lambda prix: prix[1])
print(fromages_tries)

# Les mutables
#==============

# Mutables : list, dict
# Immutables : int, float, str, tuple
nombres = list(range(10))
nombres2 = list(range(10))

print(nombres)
print(nombres == nombres2)
print(nombres is nombres2)# is est si c'est le même objet

nombres3 = nombres2 # ici nombre3 fait référence à nombres2, la modification de nombres3 entraine la modification de nombres2
nombres3.append(10)
print(nombres3)
print(nombres2)

print(nombres3 == nombres2)
print(nombres3 is nombres2)

print(id(nombres)) # id affiche l'addresse mémoire d'un nombre
print(id(nombres2))
print(id(nombres3))

def ajouter(element, liste):
    liste.append(element)
    return liste

l1 = [1, 2, 3]
l2 = ajouter(4, l1)
print(l2)
print(l1)
# porut faire une copie d'une lise dans une autre lise
#liste2 = liste[:]
#liste2 = list(liste)
#liste2 = liste.copy()

# list comprehension
#====================
nombres = list(range(10))
print(nombres)
# nombres2 = [2*n for n in nombres] # Lite comprehension
# map permet d'appliquer une fonction à une itérable
nombre2 = map( lambda n: 2*n, nombres) # retrun un oblet map, n python2 ca retour une liste
nombre2 = list(map(lambda  n: 2*n, nombres))
print(nombre2)


# pairs = list(filter(lambda n: n % 2 == 0, nombres)) # liste comprehension
pairs = list(filter(lambda n: n % 2 == 0, nombres)) # Filter la liste, return TRue je garde l'élément et False l'inverse
print(pairs)

# structure d'un programme type
# def init():
#     c = lire_configuration()
#     appliquer_configuration(c)
#
#     def f():
#         print("Bonjour")
#     f()
#
#
# def main():
#     init()
#     loop()
#     save()
#
#
# main()


# Les modules
#==============
# C'est un fichier python

# Les packages
#============
# répertoire contenant des modules ou des fichiers python. Il est possible de créer un package dans un package

# Expression régulière ( expessio relationnelles)
#================================================

import re # regular expression

url = 'https://www.monsiteweb.fr:45678/repertoire1/repertoire2/fichier.html'


m = re.search('^(https?)://([a-z.0-9-]+)(?::(\d+))?(.*)$', url)
# ^ = début de chaîne
# () = capturer ce qu'il y a entre les parenthèses
# ? = l'élément précédent peut être absent ou présent
# [a-z.0-9-] = caractère alphabétique ou chiffre ou point ou tiret
# + = l'élément précédent plusieurs fois (au moins 1 fois)
# \d = digit = chiffre
# (?:) = parenthèses non-capturantes
# . = n'importe quel caractère
# * = l'élément précédent plusieurs fois (peut être 0 fois)
# $ = fin de chaîne


if m is not None:
    print(m)
    print(m.group(0))
    protocole = m.group(1)
    domaine = m.group(2)
    port = m.group(3)
    route = m.group(4)
    print("Protocole :", protocole)
    print("Domaine :", domaine)
    print("Port :", port)
    print("Route :", route)

else:
    print("*** Echec de l'analyse !")


# Les dates et heurs
#===================
from datetime import datetime, timedelta

maintenant = datetime.now()
print(maintenant)
print(maintenant.hour)
print(maintenant.minute)
print(maintenant.second)
print(maintenant.strftime("%d/%m/%y"))


duree = timedelta(days=7)
semaine_prochaine = maintenant + duree
print(semaine_prochaine)
print(semaine_prochaine.strftime('%d/%m/%Y'))

duree2 = semaine_prochaine - maintenant
print(duree2)
print(duree2.days)

# Manipulation des fichiers
#===========================


#f = open('fichier.txt', 'w')  # w = write
f = open('fichier.txt', 'w', encoding='utf-8')  # w = write, vaut mieux préciser l'encodage

f.write("Une chaîne de caractères dedans...\n")
f.write("Une autre chaîne de caractères dedans...\n")
f.write("Une troisième chaîne de caractères dedans...\n")
print("On peut aussi écrire dans un fichier avec la fonction print()", file=f)

f.close()

# ou aussi avec with, sous une forme de context

def fonction():
    with open('fichier.txt', 'r', encoding='utf-8') as f:  # r = read
        for ligne in f: # Lecture ligne par ligne
            print(ligne, end='')
            # Le fichier est automatiquement fermé lorsque l'interpreteur quitte le bloc
    # dans cette syntaxe, pas besoin de faire open() et f.close(). with ferme automatiquement le fichier
fonction()

with open('fichier.txt', 'r', encoding='utf-8') as f:  # r = read
    tout = f.read()
    print(tout)

# Ecriture dans un fichier de configuration par exemple

config = {
    'database': {
        'host': 'localhost',
        'port': 3366,
        'user': 'luc',
        'password': 'parapluie',
        'database': 'formation'
    },
    'author': None,
    'prod': False,
    'logging': {
        'level': 'WARNING',
        'output': [
            {
                'type': 'standard',
                'target': 'stderr'
            },
            {
                'type': 'file',
                'target': 'formation.log'
            }
        ]
    }
}


print(config['database']['password'])

import json

# Ecriture dans un fichier
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=4) # dump permet de transformer un dictionnaire python en json. indent ici permet d'indenter l'affichage

# Lecture fichier json

with open('config.json', 'r', encoding='utf-8') as f:
    config2 = json.load(f)

print(config2)
print(config2['database']['password'])

# Envoyer vers un API au lieu d'écrire dans un fichier par exemple. dans ce cas il faut transformer le json en string

chaine_json = json.dumps(config)  # s = string; dumps tranforme en string une chaine de caractère json
print(repr(chaine_json))

config3 = json.loads(chaine_json)  # s = string; lire un string de json et la transforme en structure python, un dictionnaire
print(config3)
print(config3['database']['password'])


# lister les fochiers
#======================
import os


liste_noeuds = os.listdir('.') # retourl une liste de fichier et répertoire
print(liste_noeuds)

for noeud in liste_noeuds:
    # print(noeud)
    if os.path.isfile(noeud):
        print("Fichier :", noeud)
    elif os.path.isdir(noeud):
        print("Répertoire :", noeud)

# Ajouter quelque chose dans un fichier
#======================================
with open('append_example.txt', 'a', encoding='utf-8') as f:
    f.write("J'ajoute quelque chose dans ce fichier.\n")

# Ecrire dans un fichier à un endroit particulier
#================================================
with open('fichier.txt', 'r+', encoding='utf-8') as f:
    f.seek(8) # seek permet de faire
    f.write('UN TRUC QUI SE VOIT !')
