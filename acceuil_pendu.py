import pygame
import sys
import subprocess
import time

pygame.init()

# Initialiser la fenêtre
largeur_ecran = 800
hauteur_ecran = 800
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))     
pygame.display.set_caption("HANGMAN - Le Pendu")

# Icone
icon = pygame.image.load(r"pendu_icon.png")
pygame.display.set_icon(icon)

# Charger l'image de fond
image_fond = pygame.image.load(r"background.png")
image_fond = pygame.transform.scale(image_fond, (800, 800))

# Police
font = pygame.font.Font(None, 50)

# Bannière
banniere = pygame.image.load(r"logo.png")
banniere = pygame.transform.scale(banniere, (300, 300)) 
banniere_rect = banniere.get_rect()

# Bouton Jouer
bouton_jouer = pygame.image.load(r"bouton_jouer.png")
bouton_jouer = pygame.transform.scale(bouton_jouer, (270, 60)) 
rect_bouton_jouer = bouton_jouer.get_rect(topleft=(265, 400))  # Position du bouton 

# Bouton Settings
bouton_option = pygame.image.load(r"settings.png")
bouton_option = pygame.transform.scale(bouton_option, (270, 60)) 
rect_bouton_option = bouton_option.get_rect(topleft=(265, 500))  

# Bouton Retour
bouton_retour = pygame.image.load(r"retour.png")
bouton_retour = pygame.transform.scale(bouton_retour, (290, 150)) 
rect_bouton_retour = bouton_retour.get_rect(topleft=(265, 650))

# Bouton Quitter
bouton_quitter = pygame.image.load(r"quitter.png")
bouton_quitter = pygame.transform.scale(bouton_quitter, (290, 150)) #longeur,largeur
rect_bouton_quitter = bouton_quitter.get_rect(topleft=(257,550))

bouton_son_actif = pygame.image.load(r"volum_up.png")

# Son
mute = True
pygame.mixer.init()
pygame.mixer.music.load(r"musique.mp3")
def action_bouton_son ():
    global mute
    if mute == False:
        mute = True
        bouton_son_inactiF = pygame.image.load(r"volume_down.png")
        pygame.mixer.music.pause()
    else :
        mute = False
        bouton_son_actif = pygame.image.load(r"volum_up.png")
        pygame.mixer.music.play(-1, 0.0)     	
pygame.display.flip()
action_bouton_son()

#Bouton_son_actif
bouton_son_actif = pygame.image.load(r"volum_up.png")
bouton_son_actif = pygame.transform.scale(bouton_son_actif,(290,150))
rect_bouton_son_actif = bouton_son_actif.get_rect(topleft=(255,100))

#bouton_son_inactif
bouton_son_inactiF = pygame.image.load(r"volume_down.png")
bouton_son_inactif = pygame.transform.scale(bouton_son_inactiF,(290,150))
rect_bouton_son_inactif = bouton_son_inactif.get_rect(topleft=(255,100)) 

#bouton_mot
bouton_mot = pygame.image.load(r"bouton_ajouter_mot.png")
bouton_mot = pygame.transform.scale(bouton_mot,(850,470))
rect_bouton_mot = bouton_mot.get_rect(topleft=(-15,200))

# Variables pour gérer les écrans
dans_menu_options = False  



# Vérifier si la souris est sur le bouton "Jouer"
def souris_est_sur_bouton_volume(pos):
    return rect_bouton_son_actif

def souris_est_sur_bouton_jouer(pos):
    return rect_bouton_jouer.collidepoint(pos)

def souris_est_sur_bouton_options(pos):
    return rect_bouton_option.collidepoint(pos)

def souris_est_sur_bouton_retour(pos):
    return rect_bouton_retour.collidepoint(pos)

def souris_est_sur_bouton_quitter(pos):
    return rect_bouton_quitter.collidepoint(pos)

def souris_est_sur_bouton_ajouter_mot(pos):
    return rect_bouton_mot.collidepoint(pos)



#action touche
def action_bouton_jouer():
    subprocess.Popen(["python", r"jeu_pendu.py"])
    pygame.quit()
    sys.exit()


def action_bouton_options():
    afficher_menu_options()


def action_bouton_retour():
    global dans_menu_options
    dans_menu_options = False  # Revenir au menu principal

def action_bouton_mot():
    subprocess.Popen(["notepad", r"mots.txt"])

# Fonction pour afficher le menu principal
def afficher_menu_principal():
    ecran.blit(image_fond, (0, 0))
    ecran.blit(banniere, (250, 50))  # Afficher la bannière
    ecran.blit(bouton_jouer, rect_bouton_jouer.topleft)  
    ecran.blit(bouton_option, rect_bouton_option.topleft)  
    ecran.blit(bouton_quitter, rect_bouton_quitter.topleft)
    pygame.display.update()

# Fonction pour afficher le menu des options
def afficher_menu_options():
    ecran.fill((205, 127, 50))  # Fond bleu clair pour le menu des options
    font_option = pygame.font.Font(None, 40)
    titre_options = font_option.render("Options du jeu", True, (0, 0, 0))
    ecran.blit(titre_options, (300, 50))  # Titre du menu
    ecran.blit(bouton_mot, rect_bouton_mot)


    # Affichage du bouton Retour
    ecran.blit(bouton_retour, rect_bouton_retour.topleft)
    ecran.blit(bouton_son_actif if not mute 
    else bouton_son_inactif, rect_bouton_son_inactif.topleft)

    pygame.display.update()


# Fonctionnement de la page
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Quitter la boucle si l'utilisateur ferme la fenêtre

        # Détecter un clic de souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if dans_menu_options:
                if rect_bouton_son_actif.collidepoint(event.pos):
                    action_bouton_son()
                if souris_est_sur_bouton_ajouter_mot(event.pos):
                    action_bouton_mot()
                if souris_est_sur_bouton_retour(event.pos):  
                    action_bouton_retour()  # Revenir au menu principal
            else:
                if souris_est_sur_bouton_jouer(event.pos):
                    action_bouton_jouer()

                elif souris_est_sur_bouton_options(event.pos):  
                    action_bouton_options()  # Ouvrir le menu des options
                    dans_menu_options = True  # Passer à l'écran des options

            if souris_est_sur_bouton_quitter(event.pos): 
                pygame.quit()
                sys.exit()  # Quitter le programme            

    # Afficher soit le menu principal, soit le menu des options
    if dans_menu_options:
        afficher_menu_options()
    else:
        afficher_menu_principal()

pygame.quit()
sys.exit()

