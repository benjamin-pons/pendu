import pygame
import random

mots=[] #liste

try:
    with open(r"C:\Users\ponsb\OneDrive\Documents\pendu\mots.txt") as f:
        for ligne in f:
            mots.append(ligne.strip())

    if not mots:
        print("Le fichier 'mots.txt' est introuvable.")
        exit()
except Exception as e:
    print(f"Une erreur est survenue lors du chargement du fichier: {e}")
    exit()
    
try:
    mot_choisi = random.choice(mots)
except IndexError:
    print("Erreur")
    exit()

mot_masque = ['_'] * len(mot_choisi)
trouve= False
vie_joueur=6

pygame.init()

# Initialiser la fenêtre
largeur_ecran = 800
hauteur_ecran = 800
ecran = pygame.display.set_mode((largeur_ecran, hauteur_ecran))     
pygame.display.set_caption("HANGMAN - Le Pendu")

# Icone
icon = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\pendu_icon.png")
pygame.display.set_icon(icon)
pygame.display.update()

# Charger l'image de fond
image_fond = pygame.image.load(r"C:\Users\ponsb\OneDrive\Documents\pendu\background.png")
image_fond = pygame.transform.scale(image_fond, (800, 800))


running=True
while running:
    trouve=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
        lettre = event.unicodelower()
        if lettre in mot_choisi and lettre not in lettre_trouvees:
            lettre_trouvees.add(lettre)
            for f, char in enumerate(mot_choisi):
                char == lettre
                mot_masque[f]==lettre
        elif lettre not in mot_choisi:
            vie_joueur = vie_joueur -1

    # Vérifier si toutes les lettres ont été trouvées
    trouve = '_' not in mot_masque


    # Afficher l'état du mot masqué
    print("Mot : ", ' '.join(mot_masque))
    print(f"Tentatives restantes : {vie_joueur}")

    if trouve:
        print("Félicitations, tu as gagné !")
        time.sleep(2.0)
        os.system("acceuil_pendu.py")
    elif vie_joueur == 0:
        print(f"Tu as perdu. Le mot était : {mot_choisi}")
        time.sleep(2.0)
        os.system("acceuil_pendu.py")
        

pygame.quit()

    
