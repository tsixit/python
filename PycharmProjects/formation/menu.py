# 1) Lister les fichiers (ls -l)
# 2) Afficher l'espace disque (df)
# 3) Afficher l'utilisation disque (du)
# 4) Quitter
# Votre choix : 3

import os # module os permettant aussi d'exécuter une commande unix

# os.system('ls -l')
# os.system('df')
# os.system('du')
#
# exit(0) # 0 = pas d'erreur

import os

class Commande:

    def __init__(self, intitule, commande_systeme):
        self._intitule = intitule
        self._commande_systeme = commande_systeme

    def executer(self):
        os.system(self._commande_systeme)

    def __str__(self):
        return "{} ({})".format(self._intitule, self._commande_systeme)


class Quitter(Commande):

    def __init__(self):
        super().__init__("Quitter", None)

    def executer(self):
        exit(0)

    def __str__(self):
        return self._intitule


class Menu:

    _commandes = []

    def ajouter(self, commande):
        self._commandes.append(commande)

    def afficher(self):
        for i, commande in enumerate(self._commandes, 1):
            print("{}) {}".format(i, commande))

    def interroger(self):
        while True:
            try:
                reponse = input("Votre choix : ")
                i = int(reponse) - 1
                if i < 0:
                    # print("*** Vous avez écrit n'importe quoi !")
                    # continue
                    raise IndexError()
                return self._commandes[i]
            except (ValueError, IndexError):
                print("*** Vous avez écrit n'importe quoi !")


class Application:

    def __init__(self):
        menu = Menu()

        c1 = Commande("Lister les fichiers", "ls -l")
        c2 = Commande("Afficher l'espace disque", "df")
        c3 = Commande("Afficher l'utilisation disque", "du")
        # c4 = Commande("Quitter", None)
        c4 = Quitter()

        menu.ajouter(c1)
        menu.ajouter(c2)
        menu.ajouter(c3)
        menu.ajouter(c4)

        self._menu = menu

    def run(self):
        menu = self._menu
        while True:
            menu.afficher()
            commande = menu.interroger()
            commande.executer()


if __name__ == '__main__':
    app = Application()
    app.run()
