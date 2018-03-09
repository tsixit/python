# Module contient des fonctions; des variables ou des constantes
def souligner(texte):
    print(texte)
    print('=' * len(texte))


def encadrer(texte):
    print('#' * (len(texte)+4))
    print('#', texte, '#')
    print('#' * (len(texte)+4))


pizza = 5

def espacer(texte):
    caracteres = list(texte)
    #print(caracteres)
    print(' '.join(caracteres))


if __name__ == '__main__': # permet  de lancer un programme quand celui-ci est appeler en tant que programme principale.Le cas contraite il ne sera pas lance
    print(__name__)
    espacer("Hello World!")
