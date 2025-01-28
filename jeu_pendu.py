import pygame
import os
import random
import subprocess
import json

mots=[] #liste
lettre_erreur = [] #liste lettre deja utilisées

# Charger la liste de mots possibles
try:
    with open(r"mots.txt") as f:
        for ligne in f:
            mots.append(ligne.strip())

    if not mots:
        print("Le fichier 'mots.txt' est introuvable.")
        exit()
except Exception :
    print(f"Une erreur est survenue lors du chargement du fichier")
    exit()
    
try:
    mot_choisi = random.choice(mots)
except IndexError:
    print("Erreur")
    exit()

mot_masque = ['_'] * len(mot_choisi)
lettre_trouvees= set()
vie_joueur=6


pygame.init()


# Score
dictionnaire_scores = {}
    # Lecture du fichier scores
def lire_fichier_scores() :
    with open("scores.json", "r") as lecture :
        dictionnaire_scores = json.load(lecture)
    return dictionnaire_scores
dictionnaire_scores = lire_fichier_scores()

    # Ecriture dans fichier scores
def ecrire_fichier_scores(dictionnaire_scores) :
    with open("scores.json", "w") as sortie :
        json.dump(dictionnaire_scores, sortie)
    return

    # Enregistrer nouveau score
def enregistrer_score(nom) :
    dictionnaire_scores[nom] = int(vie_joueur*100)


# Initialiser la fenêtre
largeur_ecran = 800
hauteur_ecran = 800
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))     
pygame.display.set_caption("HANGMAN - Le Pendu")

#image 0
image_pendu0 = pygame.image.load(r"images/pendu/0.png")
image_pendu0 = pygame.transform.scale(image_pendu0,(150, 150))

#image 1
image_pendu1 = pygame.image.load(r"images/pendu/1.png")
image_pendu1 = pygame.transform.scale(image_pendu1,(150, 150))

#image 2
image_pendu2 = pygame.image.load(r"images/pendu/2.png")
image_pendu2 = pygame.transform.scale(image_pendu2,(150, 150))

#image 3
image_pendu3 = pygame.image.load(r"images/pendu/3.png")
image_pendu3 = pygame.transform.scale(image_pendu3,(150, 150))

#image 4
image_pendu4 = pygame.image.load(r"images/pendu/4.png")
image_pendu4 = pygame.transform.scale(image_pendu4,(150, 150))

#image 5
image_pendu5 = pygame.image.load(r"images/pendu/5.png")
image_pendu5 = pygame.transform.scale(image_pendu5,(150, 150))

#image 6
image_pendu6 = pygame.image.load(r"images/pendu/6.png")
image_pendu6 = pygame.transform.scale(image_pendu6,(150, 150))

#Liste des images pendu
liste_image = [image_pendu0, image_pendu1, image_pendu2, image_pendu3, image_pendu4, image_pendu5, image_pendu6]

# Son
pygame.mixer.init()
pygame.mixer.music.load(r"musique.mp3")
pygame.mixer.music.play(-1, 0.0)


# Icone
icon = pygame.image.load(r"images/pendu_icone.png")
pygame.display.set_icon(icon)
pygame.display.update()

# Charger l'image de fond
image_fond = pygame.image.load(r"images/background_flou.png")
image_fond = pygame.transform.scale(image_fond, (800, 800))

#texte
police = pygame.font.SysFont("monospace" ,40)

def souris_est_sur_bouton_retour(pos):
    return rect_bouton_retour.collidepoint(pos)

def afficher():
    ecran.blit(image_fond, (0, 0))
    texte_mot = police.render(" ".join(mot_masque),True,(255, 000, 000))
    ecran.blit(texte_mot,(largeur_ecran // 2 - texte_mot.get_width() // 2 , hauteur_ecran // 3))
    ecran.blit(liste_image[6 - vie_joueur], (300, 90)) 
    texte_vie = police.render(f"Vies restantes : {vie_joueur}",True,(255,0,0))
    ecran.blit(texte_vie,(20,20))
    texte_liste = police.render(" ".join(lettre_erreur),True,(255, 000, 000))
    ecran.blit(texte_liste,(largeur_ecran // 5 , hauteur_ecran // 1.2))
    pygame.display.update()



running = True
fin_de_partie = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            lettre = event.unicode.upper()
            if lettre.isalpha(): #verifie si valide
                if lettre in mot_choisi and lettre not in lettre_trouvees:
                    lettre_trouvees.add(lettre)

                    for f, char in enumerate(mot_choisi):
                        if char == lettre:
                            mot_masque[f] = lettre

                elif lettre not in mot_choisi:
                    vie_joueur = vie_joueur -1
                    lettre_erreur.append(lettre)



    afficher()

        
    # Vérifier si toutes les lettres ont été trouvées
    if vie_joueur == 0 or '_' not in mot_masque:
        fin_de_partie = True

    if fin_de_partie:
        if vie_joueur == 0:
            texte_perdu = police.render(f"Perdu, le mot était : {mot_choisi}", True, (255, 0, 0))
            ecran.blit(texte_perdu, (largeur_ecran // 2 - texte_perdu.get_width() // 2, hauteur_ecran // 2))
        else:
            texte_gagne = police.render("Tu as Gagné !", True, (255, 0, 0))
            ecran.blit(texte_gagne, (largeur_ecran // 2 - texte_gagne.get_width() // 2, hauteur_ecran // 2))
            enregistrer_score()
            ecrire_fichier_scores(dictionnaire_scores)

        bouton_retour = pygame.image.load(r"images/boutons/retour.png")
        bouton_retour = pygame.transform.scale(bouton_retour, (290, 150))
        rect_bouton_retour = bouton_retour.get_rect(topleft=(265, 500))
        ecran.blit(bouton_retour, rect_bouton_retour.topleft)
        pygame.display.update()

        # Attente de la fermeture ou du clic sur le bouton
        waiting_for_exit = True
        while waiting_for_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_exit = False
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Vérifier si l'événement est un clic de souris
                    if rect_bouton_retour.collidepoint(event.pos):  # Vérifier si le clic est sur le bouton
                        subprocess.Popen(["python", r"acceuil_pendu.py"])
                        pygame.quit()

    else:
        afficher()

pygame.quit()