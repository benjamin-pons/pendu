import pygame
import sys
import os

pygame.init()

# Initialiser la fenêtre
largeur_ecran = 800
hauteur_ecran = 800
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))     
pygame.display.set_caption("HANGMAN - Le Pendu")

# Icone
icon = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\pendu_icon.png")
pygame.display.set_icon(icon)

# Charger l'image de fond
image_fond = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\background.png")
image_fond = pygame.transform.scale(image_fond, (800, 800))

# Police
font = pygame.font.Font(None, 50)

# Bannière
banniere = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\logo.png")
banniere = pygame.transform.scale(banniere, (300, 300)) 
banniere_rect = banniere.get_rect()

# Bouton Jouer
bouton_jouer = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\bouton_jouer.png")
bouton_jouer = pygame.transform.scale(bouton_jouer, (270, 60)) 
rect_bouton_jouer = bouton_jouer.get_rect(topleft=(265, 400))  # Position du bouton 

# Bouton Settings
bouton_option = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\settings.png")
bouton_option = pygame.transform.scale(bouton_option, (270, 60)) 
rect_bouton_option = bouton_option.get_rect(topleft=(265, 500))  

# Bouton Retour
bouton_retour = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\retour.png")
bouton_retour = pygame.transform.scale(bouton_retour, (290, 150)) 
rect_bouton_retour = bouton_retour.get_rect(topleft=(265, 400))

# Bouton Quitter
bouton_quitter = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\quitter.png")
bouton_quitter = pygame.transform.scale(bouton_quitter, (290, 150)) #longeur,largeur
rect_bouton_quitter = bouton_quitter.get_rect(topleft=(257,550))

# Son
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\musique.mp3")
pygame.mixer.music.play(-1, 0.0)



# Variables pour gérer les écrans
dans_menu_options = False  



# Vérifier si la souris est sur le bouton "Jouer"
def souris_est_sur_bouton_jouer(pos):
    return rect_bouton_jouer.collidepoint(pos)

def souris_est_sur_bouton_options(pos):
    return rect_bouton_option.collidepoint(pos)

def souris_est_sur_bouton_retour(pos):
    return rect_bouton_retour.collidepoint(pos)

def souris_est_sur_bouton_quitter(pos):
    return rect_bouton_quitter.collidepoint(pos)




def action_bouton_jouer():
    print("Le bouton 'Jouer' a été cliqué !")
    os.system(r"C:\Users\ponsb\OneDrive\Documents\pendu\jeu_pendu.py")  # Lancer le fichier jeu.py
    pygame.quit()
    sys.exit()


def action_bouton_options():
    afficher_menu_options()


def action_bouton_retour():
    print("Retour au menu principal")
    global dans_menu_options
    dans_menu_options = False  # Revenir au menu principal

    

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

    # Affichage du bouton Retour
    ecran.blit(bouton_retour, rect_bouton_retour.topleft)
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
                if souris_est_sur_bouton_retour(event.pos):  
                    action_bouton_retour()  # Revenir au menu principal
            else:
                if souris_est_sur_bouton_jouer(event.pos):
                    action_bouton_jouer()  # Démarrer le jeu
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

