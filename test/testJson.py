import json
dictionnaire_scores = {}

# Lecture fichier score
def lire_fichier_scores() :
    with open("scores.json", "r") as lecture :
        dictionnaire_scores = json.load(lecture)
    return dictionnaire_scores

# Ecriture dans fichier score
def ecrire_fichier_scores(dictionnaire_scores) :
    with open("scores.json", "w") as sortie :
        json.dump(dictionnaire_scores, sortie)
    return

# Charger le dictionnaire dans une variable
dictionnaire_scores = lire_fichier_scores()

nom = input("Nom ? : ")
dictionnaire_scores[nom] = int(input("Quel Score ? : "))

ecrire_fichier_scores(dictionnaire_scores)