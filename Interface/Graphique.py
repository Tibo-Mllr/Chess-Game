import pygame
from pygame import image
from pygame.locals import *
from pygame.constants import RESIZABLE
import time


pygame.init()

clock = pygame.time.Clock()


def Echiquier():
    k = 1
    # Création de la fenêtre
    fenetre = pygame.display.set_mode((640, 640), RESIZABLE)

    # Importation du fond
    Damier = image.load("Interface/Damier.png").convert()
    Damier = pygame.transform.scale(Damier, (640, 640))
    fenetre.blit(Damier, (0, 0))

    # Importation des poèces
    # Importation des pièces blanches
    PionBlanc = image.load("Interface/Pièces/PionBlanc.png").convert_alpha()
    PionBlanc1G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc2G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc3G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc4G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc5G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc6G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc7G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc8G = pygame.transform.scale(PionBlanc, (80, 80))

    TourBlanche = image.load(
        "Interface/Pièces/TourBlanche.png").convert_alpha()
    TourBlanche1G = pygame.transform.scale(TourBlanche, (80, 80))
    TourBlanche2G = pygame.transform.scale(TourBlanche, (80, 80))

    CavalierBlanc = image.load(
        "Interface/Pièces/CavalierBlanc.png").convert_alpha()
    CavalierBlanc1G = pygame.transform.scale(CavalierBlanc, (80, 80))
    CavalierBlanc2G = pygame.transform.scale(CavalierBlanc, (80, 80))

    FouBlanc = image.load("Interface/Pièces/FouBlanc.png").convert_alpha()
    FouBlanc1G = pygame.transform.scale(FouBlanc, (80, 80))
    FouBlanc2G = pygame.transform.scale(FouBlanc, (80, 80))

    RoiBlanc = image.load("Interface/Pièces/RoiBlanc.png").convert_alpha()
    RoiBlancG = pygame.transform.scale(RoiBlanc, (80, 80))

    ReineBlanche = image.load(
        "Interface/Pièces/ReineBlanche.png").convert_alpha()
    ReineBlancheG = pygame.transform.scale(ReineBlanche, (80, 80))

    # Importation des pièces noires
    PionNoir = image.load("Interface/Pièces/PionNoir.png").convert_alpha()
    PionNoir1G = pygame.transform.scale(PionNoir, (80, 80))
    PionNoir2G = pygame.transform.scale(PionNoir, (80, 80))
    PionNoir3G = pygame.transform.scale(PionNoir, (80, 80))
    PionNoir4G = pygame.transform.scale(PionNoir, (80, 80))
    PionNoir5G = pygame.transform.scale(PionNoir, (80, 80))
    PionNoir6G = pygame.transform.scale(PionNoir, (80, 80))
    PionNoir7G = pygame.transform.scale(PionNoir, (80, 80))
    PionNoir8G = pygame.transform.scale(PionNoir, (80, 80))

    TourNoire = image.load("Interface/Pièces/TourNoire.png").convert_alpha()
    TourNoire1G = pygame.transform.scale(TourNoire, (80, 80))
    TourNoire2G = pygame.transform.scale(TourNoire, (80, 80))

    CavalierNoir = image.load(
        "Interface/Pièces/CavalierNoir.png").convert_alpha()
    CavalierNoir1G = pygame.transform.scale(CavalierNoir, (80, 80))
    CavalierNoir2G = pygame.transform.scale(CavalierNoir, (80, 80))

    FouNoir = image.load("Interface/Pièces/FouNoir.png").convert_alpha()
    FouNoir1G = pygame.transform.scale(FouNoir, (80, 80))
    FouNoir2G = pygame.transform.scale(FouNoir, (80, 80))

    RoiNoir = image.load("Interface/Pièces/RoiNoir.png").convert_alpha()
    RoiNoirG = pygame.transform.scale(RoiNoir, (80, 80))

    ReineNoire = image.load("Interface/Pièces/ReineNoire.png").convert_alpha()
    ReineNoireG = pygame.transform.scale(ReineNoire, (80, 80))

    Pièces = {(0, 0): TourBlanche1G, (0, 1): PionBlanc1G, (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): PionNoir1G, (0, 7): TourNoire1G,
              (1, 0): CavalierBlanc1G, (1, 1): PionBlanc2G, (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): PionNoir2G, (1, 7): CavalierNoir1G,
              (2, 0): FouBlanc1G, (2, 1): PionBlanc3G, (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): PionNoir3G, (2, 7): FouNoir1G,
              (3, 0): RoiBlancG, (3, 1): PionBlanc4G, (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): PionNoir4G, (3, 7): ReineNoireG,
              (4, 0): ReineBlancheG, (4, 1): PionBlanc5G, (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): PionNoir5G, (4, 7): RoiNoirG,
              (5, 0): FouBlanc2G, (5, 1): PionBlanc6G, (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): PionNoir6G, (5, 7): FouNoir2G,
              (6, 0): CavalierBlanc2G, (6, 1): PionBlanc7G, (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): PionNoir7G, (6, 7): CavalierNoir2G,
              (7, 0): TourBlanche2G, (7, 1): PionBlanc8G, (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): PionNoir8G, (7, 7): TourNoire2G}

    for cle, valeur in Pièces.items():
        if valeur == '':
            pass
        else:
            fenetre.blit(valeur, ((7-cle[0])*80, (7-cle[1])*80))
        # Rafraichissement
    pygame.display.flip()

    while k != 3:
        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                pygame.quit()  # On arrête le programme
                MenuStart()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Si clic gauche
                    mouse = event.pos
                    if Pièces[7-int(mouse[0]/80), 7-int(mouse[1]/80)] == '':
                        pass
                    else:
                        event_happened = False
                        while not event_happened:  # Tant que le déplacement de la pièce ne s'est pas produit, on attend
                            event = pygame.event.wait()
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:  # Si clic gauche
                                    mouse2 = event.pos
                                    Pièces[(7-int(mouse2[0]/80), 7-int(mouse2[1]/80))
                                           ] = Pièces[(7-int(mouse[0]/80), 7-int(mouse[1]/80))]
                                    Pièces[(7-int(mouse[0]/80),
                                            7-int(mouse[1]/80))] = ''
                                    event_happened = True

        # Re-collage
        fenetre.blit(Damier, (0, 0))  # On remet le fond
        for cle, valeur in Pièces.items():  # On reparcourt le dictionnaire pour remettre toutes les pièces en place
            if valeur == '':
                pass
            else:
                fenetre.blit(valeur, ((7-cle[0])*80, (7-cle[1])*80))
        # Rafraichissement
        pygame.draw.rect(fenetre, (255,255, 255), (96, 146, 158, 158))
        pygame.draw.rect(fenetre, (0,0,50), (100, 150, 150, 150), 2)
        pygame.draw.rect(fenetre, (0,0,50), (96, 146, 158, 158), 2)
        ReineBlancheF = pygame.transform.scale(ReineBlanche, (150, 150))
        fenetre.blit(ReineBlancheF, (100, 150))

        pygame.draw.rect(fenetre, (255,255, 255), (640-96-158, 146, 158, 158))
        pygame.draw.rect(fenetre, (0,0,50), (640-100-150, 150, 150, 150), 2)
        pygame.draw.rect(fenetre, (0,0,50), (640-96-158, 146, 158, 158), 2)
        CavalierBlancF = pygame.transform.scale(CavalierBlanc, (150, 150))
        fenetre.blit(CavalierBlancF, (640-100-150, 150))

        pygame.draw.rect(fenetre, (255,255, 255), (96, 396, 158, 158))
        pygame.draw.rect(fenetre, (0,0,50), (100, 400, 150, 150), 2)
        pygame.draw.rect(fenetre, (0,0,50), (96, 396, 158, 158), 2)
        FouBlancF = pygame.transform.scale(FouBlanc, (150, 150))
        fenetre.blit(FouBlancF, (100, 400))

        pygame.draw.rect(fenetre, (255,255, 255), (640-96-158, 396, 158, 158))
        pygame.draw.rect(fenetre, (0,0,50), (640-100-150, 400, 150, 150), 2)
        pygame.draw.rect(fenetre, (0,0,50), (640-96-158, 396, 158, 158), 2)
        TourBlancF = pygame.transform.scale(TourBlanche, (150, 150))
        fenetre.blit(TourBlancF, (640-100-150, 400))
        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        if 254 > mouse[0] > 96 and 304 > mouse[1] > 146:
            print("Vous avez choisi la Reine")
        if 640-96 > mouse[0] > 640-254 and 304 > mouse[1] > 146:
            print("Vous avez choisi le Cavalier")
        if 254 > mouse[0] > 96 and 554 > mouse[1] > 396:
            print("Vous avez choisi le Fou")
        if 640-96 > mouse[0] > 640-254 and 554 > mouse[1] > 396:
            print("Vous avez choisi la Tour")

def CréationTexte(text, font, couleur):
    textSurface = font.render(text, True, couleur)
    return textSurface, textSurface.get_rect()


def MenuStart(fonction1,fonction2):
    # On crée la fenêtre
    Menu = pygame.display.set_mode((500, 335), RESIZABLE)

    # Importation du fond
    Fond = image.load("Interface/FondMenu.jpg").convert()
    # On met la fenêtre à la bonne taille
    Fond = pygame.transform.scale(Fond, (500, 335))
    Menu.blit(Fond, (0, 0))

    # Initialisation du titre du jeu
    pygame.draw.rect(Menu, (255, 255, 255), (175-100, 10, 350, 35))
    pygame.draw.rect(Menu, (0, 0, 0), (175-100, 10, 350, 35), 1)
    pygame.font.init()  # On initialise la création de texte sur pygame
    # On choisit la police d'écriture et la taille de la police du texte
    TexteSurface = pygame.font.SysFont('Times New Roman', 30)
    TexteMenu, TextRectMenu = CréationTexte(
        'échec et mat', TexteSurface, (0, 0, 0))
    TextRectMenu.center = ((500/2), (25))  # On centre le texte
    Menu.blit(TexteMenu, TextRectMenu)
    while True:
        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                pygame.quit()  # On arrête le programme

        # Création des boutons
        mouse = pygame.mouse.get_pos()
        # Création du bouton démarrage de partie
        # Permet de savoir si la souris se situe au niveau du bouton
        if 250+70 > mouse[0] > 250-70 and 275/2+30 > mouse[1] > 275/2:
            # Pour le mettre en évidence, le bouton change de couleur quand la souris est dessus
            pygame.draw.rect(Menu, '#00FFFF', (250-70, 275/2, 140, 30))
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Si clic gauche
                    pygame.quit()
                    fonction1()
                    fonction2()
        else:
            pygame.draw.rect(Menu, '#0080ff', (250-70, 275/2, 140, 30))

        pygame.draw.rect(Menu, (0, 0, 0), (250-70, 275/2, 140, 30), 1)
        ButtonStart = pygame.font.SysFont('Times New Roman', 15)
        TextSurf, TextRect = CréationTexte(
            "Démarrer une partie", ButtonStart, (0, 0, 0))
        TextRect.center = ((500/2), (275/2+30/2))
        Menu.blit(TextSurf, TextRect)

        # Création du bouton quitter la partie
        # Permet de savoir si la souris se situe au niveau du bouton
        if 250+70 > mouse[0] > 250-70 and 435/2+30 > mouse[1] > 435/2:
            # Pour le mettre en évidence, le bouton change de couleur quand la souris est dessus
            pygame.draw.rect(Menu, '#8B0000', (250-70, 435/2, 140, 30))
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Si clic gauche
                    pygame.quit()  # On quitte la partie
        else:
            pygame.draw.rect(Menu, '#DC143C', (250-70, 435/2, 140, 30))

        pygame.draw.rect(Menu, (0, 0, 0), (250-70, 435/2, 140, 30), 1)
        ButtonStart = pygame.font.SysFont('Times New Roman', 15)
        TextSurf, TextRect = CréationTexte(
            "Quitter le jeu", ButtonStart, (0, 0, 0))
        TextRect.center = ((500/2), (435/2+30/2))
        Menu.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)


if __name__ == "__main__":
    Echiquier()
