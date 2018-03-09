phrases = []

# 1) Demander à l'utilisateur d'entrer des phrases qu'on va stocker dans la liste.
# S'il entre une chaîne vide, on passe à la suite du programme.
# 3) Afficher également l'indice de la phrase la plus longue.

while True:
    phrase = input ("Entrer une phrase: ")
    if phrase == "":
        break
    phrases.append(phrase)

# 2) Chercher la phrase la plus longue dans cette liste, et l'afficher.
longue_phrase = ""
longue_indice = None

for i, phrase in enumerate(phrases): # enumerate fonctionne aussi avec les chaines de caractères
        print(phrase, len(phrase))
        if len(phrase) > len(longue_phrase):
            longue_phrase = phrase
            longue_indice = i

print("Phrase la plus longue:", longue_phrase)

# 3) Afficher également l'indice de la phrase la plus longue.
print("Son indice:", longue_indice)