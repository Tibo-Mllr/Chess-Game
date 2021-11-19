
from Jeu.Chess import *
from Jeu_graphique import ChangeVS
import pygame
from pygame import image
from pygame.locals import *
from pygame.constants import RESIZABLE
from random import *

pygame.init()


def jeu_init():
    """Créer un tableau contenant les pièces avec leurs attributs

        Argument
        ---------


        Sortie
        ------
        Plateau: Un tableau
        """
    global Plateau
    Plateau = {(0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): '', (0, 7): '',
               (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): '', (1, 7): '',
               (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): '', (2, 7): '',
               (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): '', (3, 7): '',
               (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (4, 7): '',
               (5, 0): '', (5, 1): '', (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (5, 7): '',
               (6, 0): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): '', (6, 7): '',
               (7, 0): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (7, 7): ''}

    # Pions blancs
    PionBlanc0 = Pion(0, 'White')
    Plateau[PionBlanc0.Pos_X, PionBlanc0.Pos_Y] = PionBlanc0

    PionBlanc1 = Pion(1, 'White')
    Plateau[PionBlanc1.Pos_X, PionBlanc1.Pos_Y] = PionBlanc1

    PionBlanc2 = Pion(2, 'White')
    Plateau[PionBlanc2.Pos_X, PionBlanc2.Pos_Y] = PionBlanc2

    PionBlanc3 = Pion(3, 'White')
    Plateau[PionBlanc3.Pos_X, PionBlanc3.Pos_Y] = PionBlanc3

    PionBlanc4 = Pion(4, 'White')
    Plateau[PionBlanc4.Pos_X, PionBlanc4.Pos_Y] = PionBlanc4

    PionBlanc5 = Pion(5, 'White')
    Plateau[PionBlanc5.Pos_X, PionBlanc5.Pos_Y] = PionBlanc5

    PionBlanc6 = Pion(6, 'White')
    Plateau[PionBlanc6.Pos_X, PionBlanc6.Pos_Y] = PionBlanc6

    PionBlanc7 = Pion(7, 'White')
    Plateau[PionBlanc7.Pos_X, PionBlanc7.Pos_Y] = PionBlanc7

    # Roi Blanc
    RoiBlanc = Roi('White')
    Plateau[RoiBlanc.Pos_X, RoiBlanc.Pos_Y] = RoiBlanc

    # Tours Blanches
    TourBlanche1 = Tour('g', 'White')
    Plateau[TourBlanche1.Pos_X, TourBlanche1.Pos_Y] = TourBlanche1

    TourBlanche2 = Tour('d', 'White')
    Plateau[TourBlanche2.Pos_X, TourBlanche2.Pos_Y] = TourBlanche2

    # Fous blancs
    FouBlanc1 = Fou('g', 'White')
    Plateau[FouBlanc1.Pos_X, FouBlanc1.Pos_Y] = FouBlanc1

    FouBlanc2 = Fou('d', 'White')
    Plateau[FouBlanc2.Pos_X, FouBlanc2.Pos_Y] = FouBlanc2

    # Dame Blanche
    DameBlanche = Dame('g', 'White')
    Plateau[DameBlanche.Pos_X, DameBlanche.Pos_Y] = DameBlanche

    # Cavaliers Blancs
    CavalierBlanc1 = Cavalier('g', 'White')
    Plateau[CavalierBlanc1.Pos_X, CavalierBlanc1.Pos_Y] = CavalierBlanc1

    CavalierBlanc2 = Cavalier('d', 'White')
    Plateau[CavalierBlanc2.Pos_X, CavalierBlanc2.Pos_Y] = CavalierBlanc2

    # Pions noirs
    PionNoir0 = Pion(0, 'Black')
    Plateau[PionNoir0.Pos_X, PionNoir0.Pos_Y] = PionNoir0

    PionNoir1 = Pion(1, 'Black')
    Plateau[PionNoir1.Pos_X, PionNoir1.Pos_Y] = PionNoir1

    PionNoir2 = Pion(2, 'Black')
    Plateau[PionNoir2.Pos_X, PionNoir2.Pos_Y] = PionNoir2

    PionNoir3 = Pion(3, 'Black')
    Plateau[PionNoir3.Pos_X, PionNoir3.Pos_Y] = PionNoir3

    PionNoir4 = Pion(4, 'Black')
    Plateau[PionNoir4.Pos_X, PionNoir4.Pos_Y] = PionNoir4

    PionNoir5 = Pion(5, 'Black')
    Plateau[PionNoir5.Pos_X, PionNoir5.Pos_Y] = PionNoir5

    PionNoir6 = Pion(6, 'Black')
    Plateau[PionNoir6.Pos_X, PionNoir6.Pos_Y] = PionNoir6

    PionNoir7 = Pion(7, 'Black')
    Plateau[PionNoir7.Pos_X, PionNoir7.Pos_Y] = PionNoir7

    # Roi Noir
    RoiNoir = Roi('Black')
    Plateau[RoiNoir.Pos_X, RoiNoir.Pos_Y] = RoiNoir

    # Tours Noires
    TourNoire1 = Tour('g', 'Black')
    Plateau[TourNoire1.Pos_X, TourNoire1.Pos_Y] = TourNoire1

    TourNoire2 = Tour('d', 'Black')
    Plateau[TourNoire2.Pos_X, TourNoire2.Pos_Y] = TourNoire2

    # Fous Noirs
    FouNoir1 = Fou('g', 'Black')
    Plateau[FouNoir1.Pos_X, FouNoir1.Pos_Y] = FouNoir1

    FouNoir2 = Fou('d', 'Black')
    Plateau[FouNoir2.Pos_X, FouNoir2.Pos_Y] = FouNoir2

    # Dame Noire
    DameNoire = Dame('g', 'Black')
    Plateau[DameNoire.Pos_X, DameNoire.Pos_Y] = DameNoire

    # Cavaliers Noirs
    CavalierNoir1 = Cavalier('g', 'Black')
    Plateau[CavalierNoir1.Pos_X, CavalierNoir1.Pos_Y] = CavalierNoir1

    CavalierNoir2 = Cavalier('d', 'Black')
    Plateau[CavalierNoir2.Pos_X, CavalierNoir2.Pos_Y] = CavalierNoir2


def ChangeV2(piece, X, plateaugraphique, fenetre):
    """Permet la transformation d'un pion parmis différentes pièces si il arrive au bout du plateau

        Argument
        ---------
        la pièce, les coordonnées de celle-ci, le tableau graphique du jeu et la fenetre pygame d'affichage

        Sortie
        ------
        la pièce avec ses attributs. La pièce de la fenêtre graphique est modifiée
        """
    if piece.name == 'pion':
        # On vérifie que la pièce est un pion blanc situé au bout de plateau
        if piece.Color == 'White' and piece.Pos_Y == 7:
            # Importations des différentes pièces utiles blanches
            ReineBlanche = image.load(
                "Interface/Pièces/ReineBlanche.png").convert_alpha()
            pygame.draw.rect(fenetre, (255, 255, 255), (96, 146, 158, 158))
            pygame.draw.rect(fenetre, (0, 0, 50), (100, 150, 150, 150), 2)
            pygame.draw.rect(fenetre, (0, 0, 50), (96, 146, 158, 158), 2)
            ReineBlancheF = pygame.transform.scale(ReineBlanche, (150, 150))
            fenetre.blit(ReineBlancheF, (100, 150))

            CavalierBlanc = image.load(
                "Interface/Pièces/CavalierBlanc.png").convert_alpha()
            pygame.draw.rect(fenetre, (255, 255, 255),
                             (640-96-158, 146, 158, 158))
            pygame.draw.rect(fenetre, (0, 0, 50),
                             (640-100-150, 150, 150, 150), 2)
            pygame.draw.rect(fenetre, (0, 0, 50),
                             (640-96-158, 146, 158, 158), 2)
            CavalierBlancF = pygame.transform.scale(CavalierBlanc, (150, 150))
            fenetre.blit(CavalierBlancF, (640-100-150, 150))

            FouBlanc = image.load(
                "Interface/Pièces/FouBlanc.png").convert_alpha()
            pygame.draw.rect(fenetre, (255, 255, 255), (96, 396, 158, 158))
            pygame.draw.rect(fenetre, (0, 0, 50), (100, 400, 150, 150), 2)
            pygame.draw.rect(fenetre, (0, 0, 50), (96, 396, 158, 158), 2)
            FouBlancF = pygame.transform.scale(FouBlanc, (150, 150))
            fenetre.blit(FouBlancF, (100, 400))

            TourBlanche = image.load(
                "Interface/Pièces/TourBlanche.png").convert_alpha()
            pygame.draw.rect(fenetre, (255, 255, 255),
                             (640-96-158, 396, 158, 158))
            pygame.draw.rect(fenetre, (0, 0, 50),
                             (640-100-150, 400, 150, 150), 2)
            pygame.draw.rect(fenetre, (0, 0, 50),
                             (640-96-158, 396, 158, 158), 2)
            TourBlancF = pygame.transform.scale(TourBlanche, (150, 150))
            fenetre.blit(TourBlancF, (640-100-150, 400))
            pygame.display.flip()  # Le cadre de choix est affiché
            event_happened = False  # On attend que l'utilisateur choisit sa pièce voulue
            while not event_happened:
                event = pygame.event.wait()  # On attend un évènement
                if event.type == MOUSEBUTTONDOWN:  # Si c'est un clic de souris
                    if event.button == 1:  # Si clic gauche
                        mouse = event.pos
                        # Le clic est situé dans le cadre du choix de la pièce Reine
                        if 254 > mouse[0] > 96 and 304 > mouse[1] > 146:
                            ReineBlancheJ = pygame.transform.scale(
                                ReineBlanche, (80, 80))  # On met la pièce aux bonnes dimensions
                            Changement = Dame('g', piece.Color, True,  # On enregistre le changement
                                              piece.Pos_X, piece.Pos_Y)
                            # On modifie l'apparence du pion dans la fenêtre graphique
                            plateaugraphique[(X[0], X[1])] = ReineBlancheJ
                            event_happened = True
                        # Le clic est situé dans le cadre du choix de la pièce Cavalier
                        if 640-96 > mouse[0] > 640-254 and 304 > mouse[1] > 146:
                            CavalierBlancJ = pygame.transform.scale(
                                CavalierBlanc, (80, 80))
                            Changement = Cavalier('g', piece.Color, True,
                                                  piece.Pos_X, piece.Pos_Y)
                            plateaugraphique[(X[0], X[1])] = CavalierBlancJ
                            event_happened = True
                        # Le clic est situé dans le cadre de la pièce voulue
                        if 254 > mouse[0] > 96 and 554 > mouse[1] > 396:
                            FouBlancJ = pygame.transform.scale(
                                FouBlanc, (80, 80))
                            Changement = Fou('g', piece.Color, True,
                                             piece.Pos_X, piece.Pos_Y)
                            plateaugraphique[(X[0], X[1])] = FouBlancJ
                            event_happened = True
                        # Le clic est situé dans le cadre de la pièce voulue
                        if 640-96 > mouse[0] > 640-254 and 554 > mouse[1] > 396:
                            TourBlancheJ = pygame.transform.scale(
                                TourBlanche, (80, 80))
                            Changement = Tour('g', piece.Color, True,
                                              piece.Pos_X, piece.Pos_Y)
                            plateaugraphique[(X[0], X[1])] = TourBlancheJ
                            event_happened = True
                        return Changement
        # On vérifie que la pièce est un pion noir situé au bout de plateau
        if piece.Color == 'Black' and piece.Pos_Y == 0:
            # Importations des différentes pièces utiles noires
            ReineNoire = image.load(
                "Interface/Pièces/ReineNoire.png").convert_alpha()
            pygame.draw.rect(fenetre, (255, 255, 255), (96, 146, 158, 158))
            pygame.draw.rect(fenetre, (0, 0, 50), (100, 150, 150, 150), 2)
            pygame.draw.rect(fenetre, (0, 0, 50), (96, 146, 158, 158), 2)
            ReineNoireF = pygame.transform.scale(ReineNoire, (150, 150))
            fenetre.blit(ReineNoireF, (100, 150))

            CavalierNoir = image.load(
                "Interface/Pièces/CavalierNoir.png").convert_alpha()
            pygame.draw.rect(fenetre, (255, 255, 255),
                             (640-96-158, 146, 158, 158))
            pygame.draw.rect(fenetre, (0, 0, 50),
                             (640-100-150, 150, 150, 150), 2)
            pygame.draw.rect(fenetre, (0, 0, 50),
                             (640-96-158, 146, 158, 158), 2)
            CavalierNoirF = pygame.transform.scale(CavalierNoir, (150, 150))
            fenetre.blit(CavalierNoirF, (640-100-150, 150))

            FouNoir = image.load(
                "Interface/Pièces/FouNoir.png").convert_alpha()
            pygame.draw.rect(fenetre, (255, 255, 255), (96, 396, 158, 158))
            pygame.draw.rect(fenetre, (0, 0, 50), (100, 400, 150, 150), 2)
            pygame.draw.rect(fenetre, (0, 0, 50), (96, 396, 158, 158), 2)
            FouNoirF = pygame.transform.scale(FouNoir, (150, 150))
            fenetre.blit(FouNoirF, (100, 400))

            TourNoir = image.load(
                "Interface/Pièces/TourNoire.png").convert_alpha()
            pygame.draw.rect(fenetre, (255, 255, 255),
                             (640-96-158, 396, 158, 158))
            pygame.draw.rect(fenetre, (0, 0, 50),
                             (640-100-150, 400, 150, 150), 2)
            pygame.draw.rect(fenetre, (0, 0, 50),
                             (640-96-158, 396, 158, 158), 2)
            TourNoirF = pygame.transform.scale(TourNoir, (150, 150))
            fenetre.blit(TourNoirF, (640-100-150, 400))
            pygame.display.flip()
            event_happened = False
            while not event_happened:
                event = pygame.event.wait()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Si clic gauche
                        mouse = event.pos
                        if 254 > mouse[0] > 96 and 304 > mouse[1] > 146:
                            ReineNoirJ = pygame.transform.scale(
                                ReineNoire, (80, 80))
                            Changement = Dame('g', piece.Color, True,
                                              piece.Pos_X, piece.Pos_Y)
                            plateaugraphique[(X[0], X[1])] = ReineNoirJ
                            event_happened = True
                        if 640-96 > mouse[0] > 640-254 and 304 > mouse[1] > 146:
                            CavalierNoirJ = pygame.transform.scale(
                                CavalierNoir, (80, 80))
                            Changement = Cavalier('g', piece.Color, True,
                                                  piece.Pos_X, piece.Pos_Y)
                            plateaugraphique[(X[0], X[1])] = CavalierNoirJ
                            event_happened = True
                        if 254 > mouse[0] > 96 and 554 > mouse[1] > 396:
                            FouNoirJ = pygame.transform.scale(
                                FouNoir, (80, 80))
                            Changement = Fou('g', piece.Color, True,
                                             piece.Pos_X, piece.Pos_Y)
                            plateaugraphique[(X[0], X[1])] = FouNoirJ
                            event_happened = True
                        if 640-96 > mouse[0] > 640-254 and 554 > mouse[1] > 396:
                            TourNoirJ = pygame.transform.scale(
                                TourNoir, (80, 80))
                            Changement = Tour('g', piece.Color, True,
                                              piece.Pos_X, piece.Pos_Y)
                            plateaugraphique[(X[0], X[1])] = TourNoirJ
                            event_happened = True
                        return Changement
        return piece
    return piece


def jeu_Final():
    """La fonction porte bien son nom, elle permet de jouer au jeu d'échec avec une interface graphique 

        Sortie
        ------
        le jeu
        """
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

    PiècesGraphique = {(0, 0): TourBlanche1G, (0, 1): PionBlanc1G, (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): PionNoir1G, (0, 7): TourNoire1G,
                       (1, 0): CavalierBlanc1G, (1, 1): PionBlanc2G, (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): PionNoir2G, (1, 7): CavalierNoir1G,
                       (2, 0): FouBlanc1G, (2, 1): PionBlanc3G, (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): PionNoir3G, (2, 7): FouNoir1G,
                       (3, 0): ReineBlancheG, (3, 1): PionBlanc4G, (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): PionNoir4G, (3, 7): ReineNoireG,
                       (4, 0): RoiBlancG, (4, 1): PionBlanc5G, (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): PionNoir5G, (4, 7): RoiNoirG,
                       (5, 0): FouBlanc2G, (5, 1): PionBlanc6G, (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): PionNoir6G, (5, 7): FouNoir2G,
                       (6, 0): CavalierBlanc2G, (6, 1): PionBlanc7G, (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): PionNoir7G, (6, 7): CavalierNoir2G,
                       (7, 0): TourBlanche2G, (7, 1): PionBlanc8G, (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): PionNoir8G, (7, 7): TourNoire2G}

    for cle, valeur in PiècesGraphique.items():
        if valeur == '':
            pass
        else:
            fenetre.blit(valeur, ((cle[0])*80, (7-cle[1])*80))
            # Rafraichissement
    pygame.display.flip()

    k = 1
    X1, Y1 = 8, 8
    X2, Y2 = 8, 8

    while k != 3:
        if k == 2:  # Permet de changer les tours tout en vérifiant bien qu'on vérifié si le roi est en échec, etc à chaque fois
            k = 0

        if k == 1:

            for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
                if event.type == QUIT:  # Si un de ces événements est de type QUIT
                    pygame.quit()  # On arrête le programme
                    MenuStart()  # On relance le menu
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:  # Si clic gauche
                        mouse = event.pos
                        X = int(mouse[0]/80)
                        Y = 7-int(mouse[1]/80)
                        if Plateau[(X, Y)] == '':
                            pass
                        else:
                            if Plateau[(X, Y)].Color == 'White':  # C'est le tour des blancs
                                Mouvement = mvt_final(Plateau[(X, Y)], Plateau)
                                pygame.draw.rect(
                                    fenetre, '#008000', (X*80, (7-Y)*80, 80, 80), 5)  # On trace l'emplacement de la pièce
                                for x in Mouvement:
                                    pygame.draw.rect(
                                        fenetre, '#FFFF00', (x[0]*80, (7-x[1])*80, 80, 80), 5)  # On trace les mouvements possibles
                                pygame.display.flip()
                                event_happened = False
                                while not event_happened:  # Tant que le déplacement de la pièce ne s'est pas produit, on attend
                                    event = pygame.event.wait()
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:  # Si clic gauche
                                            mouse2 = event.pos
                                            X2 = int(mouse2[0]/80)
                                            Y2 = 7-int(mouse2[1]/80)
                                            # On vérifie si le mouvement est possible et si c'est un coup spécial
                                            if Plateau[(X, Y)] != '' and (X2, Y2) in mvt_final(Plateau[(X, Y)], Plateau):
                                                _roque = roque(
                                                    Plateau[(X, Y)], X2, Plateau)
                                                if _roque == 'Petit':
                                                    PiècesGraphique[(
                                                        5, Y2)] = PiècesGraphique[(7, Y2)]
                                                    PiècesGraphique[(
                                                        7, Y2)] = ''
                                                elif _roque == 'Grand':
                                                    PiècesGraphique[(
                                                        3, Y2)] = PiècesGraphique[(0, Y2)]
                                                    PiècesGraphique[(
                                                        0, Y2)] = ''

                                                Plateau[(X, Y)].move(
                                                    X2, Y2)
                                                Plateau[(X2, Y2)] = ChangeV2(
                                                    Plateau[(X, Y)], (X, Y), PiècesGraphique, fenetre)  # Le pion est arrivé au bout du plateau
                                                Plateau[(X, Y)] = ''
                                                # Déplacement de la pièce graphique
                                                PiècesGraphique[(
                                                    X2, Y2)] = PiècesGraphique[(X, Y)]
                                                PiècesGraphique[(X, Y)] = ''
                                                event_happened = True
                                                k = 2  # C'est au tour des noirs de jouer
                                            else:
                                                print(
                                                    "Ce déplacement n'est pas possible")
                                                event_happened = True
                            else:
                                # Le joueur a selectionné une pièce noire
                                print('Les pièces blanches doivent jouer')
        if k == 0:
            P = []
            M = []
            for piece in Plateau.values():
                if piece != '' and piece.Color == 'Black' and mvt_final(piece, Plateau) != []:
                    P.append(piece)
                    M = M + [mvt_final(piece, Plateau)]

            p = randint(0, len(P)-1)
            X, Y = P[p].Pos_X, P[p].Pos_Y
            X1, Y1 = X, Y

            m = randint(0, len(M[p])-1)
            X2, Y2 = M[p][m][0], M[p][m][1]

            _roque = roque(
                Plateau[(X, Y)], X2, Plateau)
            if _roque == 'Petit':
                PiècesGraphique[(
                    5, Y2)] = PiècesGraphique[(7, Y2)]
                PiècesGraphique[(
                    7, Y2)] = ''
            elif _roque == 'Grand':
                PiècesGraphique[(
                    3, Y2)] = PiècesGraphique[(0, Y2)]
                PiècesGraphique[(
                    0, Y2)] = ''

            Plateau[(X, Y)].move(
                X2, Y2)
            # Le pion est arrivé au bout de plateau
            Plateau[(X2, Y2)] = ChangeVS(Plateau[(X, Y)],
                                         (X, Y), PiècesGraphique, fenetre)
            Plateau[(X, Y)] = ''
            # Déplacement de la pièce graphique
            PiècesGraphique[(
                X2, Y2)] = PiècesGraphique[(X, Y)]
            PiècesGraphique[(X, Y)] = ''
            event_happened = True

            k = 1  # C'est au tour des blancs de jouer

        # Recollage
        fenetre.blit(Damier, (0, 0))  # On remet le fond
        # On reparcourt le dictionnaire pour remettre toutes les pièces en place
        for cle, valeur in PiècesGraphique.items():
            if valeur == '':
                pass
            else:
                fenetre.blit(valeur, (cle[0]*80, (7-cle[1])*80))

        # Affichage si le roi est en échec
        for piece in Plateau.values():
            if piece != '' and piece.name == 'roi' and piece.Color == 'White':
                RoiBlancP = piece
                if roi_en_echec(RoiBlancP, Plateau):
                    pygame.draw.rect(
                        fenetre, (255, 0, 0), (RoiBlancP.Pos_X*80, (7-RoiBlancP.Pos_Y)*80, 80, 80), 5)
            if piece != '' and piece.name == 'roi' and piece.Color == 'Black':
                RoiBlackP = piece
                if roi_en_echec(RoiBlackP, Plateau):
                    pygame.draw.rect(
                        fenetre, (255, 0, 0), (RoiBlackP.Pos_X*80, (7-RoiBlackP.Pos_Y)*80, 80, 80), 5)

        # Affichage du mouvement de l'ordi
        if k == 1:
            pygame.draw.rect(fenetre, (255, 127, 0),
                             (X1*80, (7-Y1)*80, 80, 80), 5)
            pygame.draw.rect(fenetre, (255, 127, 0),
                             (X2*80, (7-Y2)*80, 80, 80), 5)

        pygame.display.flip()

        if echec_et_mat(Plateau) or egalite(Plateau):
            k = 3


