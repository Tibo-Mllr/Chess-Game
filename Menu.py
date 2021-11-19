import pygame
from pygame import image
from pygame.locals import *
from pygame.constants import RESIZABLE
import Jeu_graphique as Jeu
import Jeu_VS as VS

pygame.init()

def CréationTexte(text, font, couleur):
    """La fonction permet de faciliter l'affichage d'un texte
        Argument
        ------
        Le text, la page d'affichage et une couleur

        Sortie
        ------
        Un pygame.surface et ses coordonées
        """
    textSurface = font.render(text, True, couleur)
    return textSurface, textSurface.get_rect()


def MenuStart():
    """La fonction affiche un menu avec deux boutons. Le premier permet d'initialiser deux fonctions
    Le second permet de quitter le jeu
        Argument
        ------
        Deux fonctions

        Sortie
        ------
        Deux fonctions qui s'initialisent si on appuie sur le bouton. La fermeture de la page sinon
        """
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
                    Jeu.jeu_init()
                    Jeu.jeu_Final()
        else:
            pygame.draw.rect(Menu, '#0080ff', (250-70, 275/2, 140, 30))

        pygame.draw.rect(Menu, (0, 0, 0), (250-70, 275/2, 140, 30), 1)
        ButtonStart = pygame.font.SysFont('Times New Roman', 15)
        TextSurf, TextRect = CréationTexte(
            "Démarrer une partie", ButtonStart, (0, 0, 0))
        TextRect.center = ((500/2), (275/2+30/2))
        Menu.blit(TextSurf, TextRect)

        # Création du bouton jouer contre une IA
        # Permet de savoir si la souris se situe au niveau du bouton
        if 250+120 > mouse[0] > 250-120 and 375/2+30 > mouse[1] > 375/2:
            # Pour le mettre en évidence, le bouton change de couleur quand la souris est dessus
            pygame.draw.rect(Menu, '#00FFFF', (250-120, 375/2, 240, 30))
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Si clic gauche
                    pygame.quit()
                    VS.jeu_init()
                    VS.jeu_Final()
        else:
            pygame.draw.rect(Menu, '#0080ff', (250-120, 375/2, 240, 30))

        pygame.draw.rect(Menu, (0, 0, 0), (250-120, 375/2, 240, 30), 1)
        ButtonStart = pygame.font.SysFont('Times New Roman', 15)
        TextSurf, TextRect = CréationTexte(
            "Démarrer une partie contre un IA", ButtonStart, (0, 0, 0))
        TextRect.center = ((500/2), (375/2+30/2))
        Menu.blit(TextSurf, TextRect)

        # Création du bouton jouer contre une IA
        # Permet de savoir si la souris se situe au niveau du bouton
        if 250+70 > mouse[0] > 250-70 and 475/2+30 > mouse[1] > 475/2:
            # Pour le mettre en évidence, le bouton change de couleur quand la souris est dessus
            pygame.draw.rect(Menu, '#FF0000', (250-70, 475/2, 140, 30))
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Si clic gauche
                    pygame.quit()
        else:
            pygame.draw.rect(Menu, '#DC143C', (250-70, 475/2, 140, 30))

        pygame.draw.rect(Menu, (0, 0, 0), (250-70, 475/2, 140, 30), 1)
        ButtonStart = pygame.font.SysFont('Times New Roman', 15)
        TextSurf, TextRect = CréationTexte(
            "Quitter le jeu", ButtonStart, (0, 0, 0))
        TextRect.center = ((500/2), (475/2+30/2))
        Menu.blit(TextSurf, TextRect)

        pygame.display.update()

if __name__ == "__main__":
    MenuStart()