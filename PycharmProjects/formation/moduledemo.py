import textformat

textformat.souligner("Module importé")
textformat.encadrer("Module importé !")
print(textformat)

import textformat as t # renomé le module importé


t.souligner("Module renomé")
t.encadrer("Module renomé")

from textformat import souligner # Importer une seule fonction dans un module

souligner("Importation de la fonction seule.")
from textformat import souligner, encadrer as e, pizza

souligner("Importation de la fonction seule.")
e("Fonction renommée !")
print(pizza)

from textformat import * # Importe les éléments individuelement, à utiliser avec précaution car peut entrer en conflit avec les variables dans le programme principale
espacer("Fonction importé par l'étoile")

espacer("Fonction importée par l'étoile.")

import restaurants # import packages

restaurants.affiche_restaurants() # appel d'une fonction dans un package

import restaurants.principal # Import d'un module dans un package

restaurants.principal.run() # appel d'une fonction d'un module d'un package

from restaurants import principal

import sys

print(sys.path)

# ajouter un path
#sys.path.append("/path/à/ajouter")
sys.path.append("/home/stagiaire/PycharmProjects/formation/lib")

# PYTHONPATH


# $ export PYTHONPATH=/home/lphan/PycharmProjects/formation/lib

print(sys.path)

import unmodulededans

print(unmodulededans.division(10, 3))