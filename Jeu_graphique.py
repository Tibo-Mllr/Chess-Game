from Classes.Pieces import *
from Jeu.Chess import *
import pygame
from pygame import image
from pygame.locals import *
from pygame.constants import RESIZABLE

pygame.init()

Plateau = {(0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): '', (0, 7): '',
           (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): '', (1, 7): '',
           (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): '', (2, 7): '',
           (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): '', (3, 7): '',
           (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (4, 7): '',
           (5, 0): '', (5, 1): '', (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (5, 7): '',
           (6, 0): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): '', (6, 7): '',
           (7, 0): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (7, 7): ''}

def jeu_init():
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

def jeu_Final():
    #Création de la fenêtre
    fenetre = pygame.display.set_mode((640, 640), RESIZABLE)

    #Importation du fond
    Damier = image.load("Interface/Damier.png").convert()
    Damier = pygame.transform.scale(Damier, (640, 640))
    fenetre.blit(Damier, (0,0))

    #Importation des poèces
    #Importation des pièces blanches
    PionBlanc = image.load("Interface/Pièces/PionBlanc.png").convert_alpha()
    PionBlanc1G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc2G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc3G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc4G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc5G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc6G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc7G = pygame.transform.scale(PionBlanc, (80, 80))
    PionBlanc8G = pygame.transform.scale(PionBlanc, (80, 80))

    TourBlanche = image.load("Interface/Pièces/TourBlanche.png").convert_alpha()
    TourBlanche1G = pygame.transform.scale(TourBlanche, (80, 80))
    TourBlanche2G = pygame.transform.scale(TourBlanche, (80, 80))

    CavalierBlanc = image.load("Interface/Pièces/CavalierBlanc.png").convert_alpha()
    CavalierBlanc1G = pygame.transform.scale(CavalierBlanc, (80, 80))
    CavalierBlanc2G = pygame.transform.scale(CavalierBlanc, (80, 80))

    FouBlanc = image.load("Interface/Pièces/FouBlanc.png").convert_alpha()
    FouBlanc1G = pygame.transform.scale(FouBlanc, (80, 80))
    FouBlanc2G = pygame.transform.scale(FouBlanc, (80, 80))

    RoiBlanc = image.load("Interface/Pièces/RoiBlanc.png").convert_alpha()
    RoiBlancG = pygame.transform.scale(RoiBlanc, (80, 80))

    ReineBlanche = image.load("Interface/Pièces/ReineBlanche.png").convert_alpha()
    ReineBlancheG = pygame.transform.scale(ReineBlanche, (80,80))


    #Importation des pièces noires
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

    CavalierNoir = image.load("Interface/Pièces/CavalierNoir.png").convert_alpha()
    CavalierNoir1G = pygame.transform.scale(CavalierNoir, (80, 80))
    CavalierNoir2G = pygame.transform.scale(CavalierNoir, (80, 80))

    FouNoir = image.load("Interface/Pièces/FouNoir.png").convert_alpha()
    FouNoir1G = pygame.transform.scale(FouNoir, (80, 80))
    FouNoir2G = pygame.transform.scale(FouNoir, (80, 80))

    RoiNoir = image.load("Interface/Pièces/RoiNoir.png").convert_alpha()
    RoiNoirG = pygame.transform.scale(RoiNoir, (80, 80))

    ReineNoire = image.load("Interface/Pièces/ReineNoire.png").convert_alpha()
    ReineNoireG = pygame.transform.scale(ReineNoire, (80,80))

    PiècesGraphique = {(0, 0): TourBlanche1G, (0, 1): PionBlanc1G, (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): PionNoir1G, (0, 7): TourNoire1G, 
            (1, 0): CavalierBlanc1G, (1, 1): PionBlanc2G, (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): PionNoir2G, (1, 7): CavalierNoir1G,
            (2, 0): FouBlanc1G, (2, 1): PionBlanc3G, (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): PionNoir3G, (2, 7): FouNoir1G,
            (3, 0): RoiBlancG, (3, 1): PionBlanc4G, (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): PionNoir4G, (3, 7): ReineNoireG,
            (4, 0): ReineBlancheG, (4, 1): PionBlanc5G, (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): PionNoir5G, (4, 7): RoiNoirG,
            (5, 0): FouBlanc2G, (5, 1): PionBlanc6G, (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): PionNoir6G, (5, 7): FouNoir2G,
            (6, 0): CavalierBlanc2G, (6, 1): PionBlanc7G, (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): PionNoir7G, (6, 7): CavalierNoir2G,
            (7, 0): TourBlanche2G, (7, 1): PionBlanc8G, (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): PionNoir8G, (7, 7): TourNoire2G}

    for cle, valeur in PiècesGraphique.items():
        if valeur == '':
            pass
        else :
            fenetre.blit(valeur, (cle[0]*80, cle[1]*80))
		#Rafraichissement
        pygame.display.flip()

    k=1
    while k !=3:
        if k == 2:
            k = 0

        for element in Plateau:
            if Plateau[element] != '' and Plateau[element].name == 'roi' and Plateau[element].Color == 'White':
                RoiBlanc = Plateau[element]
            if Plateau[element] != '' and Plateau[element].name == 'roi' and Plateau[element].Color == 'Black':
                RoiNoir = Plateau[element]

        for event in pygame.event.get():    #On parcours la liste de tous les événements reçus
            if event.type == QUIT:    	 	#Si un de ces événements est de type QUIT
                pygame.quit()     			#On arrête le programme
                #MenuStart()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:	#Si clic gauche
                    mouse = event.pos
                    X=int(mouse[0]/80)
                    Y=int(mouse[1]/80)
                    if Plateau[(X,Y)] =='':
                        pass
                    else:
                        if k==1:
                            if Plateau[(X, Y)].Color == 'White':
                                event_happened = False
                                while not event_happened: #Tant que le déplacement de la pièce ne s'est pas produit, on attend
                                    event = pygame.event.wait()
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:	#Si clic gauche
                                            mouse2 = event.pos
                                            X2=int(mouse2[0]/80)
                                            Y2=int(mouse2[1]/80)
                                            if Plateau[(X, Y)] != '' and (X2, Y2) in mvt_final(Plateau[(X, Y)], Plateau):
                                                PiècesGraphique[(X2,Y2)]= PiècesGraphique[(X, Y)]
                                                PiècesGraphique[(X, Y)] = ''
                                                event_happened = True
                                                Plateau[(X, Y)].move(X2, Y2)
                                                Plateau[(X2, Y2)] = Plateau[(X, Y)]
                                                Plateau[(X, Y)] = ''
                                                k=2
                                            else:
                                                print("Ce déplacement n'est pas possible")
                                                event_happened = True
                            else:
                                print('Les pièces blanches doivent jouer')
                        if k==0:
                            if Plateau[(X, Y)].Color == 'Black':
                                event_happened = False
                                while not event_happened: #Tant que le déplacement de la pièce ne s'est pas produit, on attend
                                    event = pygame.event.wait()
                                    if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:	#Si clic gauche
                                            mouse2 = event.pos
                                            X2=int(mouse2[0]/80)
                                            Y2=int(mouse2[1]/80)
                                            if (X2, Y2) in mvt_final(Plateau[(X, Y)], Plateau):
                                                PiècesGraphique[(X2,Y2)]= PiècesGraphique[(X, Y)]
                                                PiècesGraphique[(X, Y)] = ''
                                                event_happened = True
                                                Plateau[(X, Y)].move(X2, Y2)
                                                Plateau[(X2, Y2)] = Plateau[(X, Y)]
                                                Plateau[(X, Y)] = ''
                                                k=1
                                            else:
                                                print("Ce déplacement n'est pas possible")
                                                event_happened = True
                            else:
                                print('Les pièces noires doivent jouer')
    
        #Recollage
        fenetre.blit(Damier, (0,0))	#On remet le fond 
        for cle, valeur in PiècesGraphique.items(): #On reparcourt le dictionnaire pour remettre toutes les pièces en place
            if valeur == '':
                pass
            else :
                fenetre.blit(valeur, (cle[0]*80, cle[1]*80))
            
        pygame.display.flip()	

        if roi_en_echec(RoiBlanc, Plateau) and mvt_final(RoiBlanc, Plateau) == []:
            k = 3
            print("Sortie Blanche")
        if roi_en_echec(RoiNoir, Plateau) and mvt_final(RoiNoir, Plateau) == []:
            k = 3
            print("Sortie Noire")

    egalite(RoiBlanc, Plateau)
    egalite(RoiNoir, Plateau)
    victoire(RoiBlanc, Plateau)
    victoire(RoiNoir, Plateau)

    #A changer: La fin du jeu ne marche pas j'ai l'impression

if __name__ == "__main__":
    jeu_init()
    jeu_Final()