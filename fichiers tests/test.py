scores = open("./scores.txt", "r")
def init_scores() :
    nom = 0
    nombre = 1

    dict_scores = {}
    liste = scores.readlines()
    longueur = len(liste)

    for i in range(longueur//2) :
        dict_scores[liste[nom].strip()] = liste[nombre].strip()
        nom += 2
        nombre += 2
    
    return dict_scores

dict_scores = init_scores()

for i in dict_scores :
    print(f"{i} : {dict_scores[i]}")