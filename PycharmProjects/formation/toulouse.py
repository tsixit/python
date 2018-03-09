votes = {
    "L'oncle Pom": 0,
    "Aux délices": 0,
    "Le Yeti": 0
}

# 1) L'Oncle Pom: 0
# 2) Aux Délices: 0
# 3) le Yeti: 0
# q) Quitter
# Votre choix : 1

print(list(votes.keys()))
restaurents = list(votes.keys())
while True:
    for i, restaurent in enumerate(restaurents, 1):# le 1 permet de dire à enumerate de compter à partir de 1
        print("{}) {} : {}".format(i, restaurent, votes[restaurent]))
    print("q ) Quitter")
    reponse = input("Votre choix: ")
    if reponse == "q":
        break
    restaurent = restaurents[int(reponse) - 1]
    print(restaurent)
    votes[restaurent] += 1





