import pygame
from pygame import image
from pygame.locals import *
from pygame.constants import RESIZABLE
import time



pygame.init()

clock= pygame.time.Clock()

def Echiquier():
	#Création de la fenêtre
	fenetre = pygame.display.set_mode((640, 640), RESIZABLE)

	#Importation du fond
	Damier = image.load("Interface/Damier.png").convert()
	Damier = pygame.transform.scale(Damier, (640, 640))
	fenetre.blit(Damier, (0,0))

	#Importation des poèces
	#Importation des pièces blanches
	PionBlanc = image.load("Interface/Pièces/PionBlanc.png").convert_alpha()
	PionBlanc1 = pygame.transform.scale(PionBlanc, (80, 80))
	PionBlanc2 = pygame.transform.scale(PionBlanc, (80, 80))
	PionBlanc3 = pygame.transform.scale(PionBlanc, (80, 80))
	PionBlanc4 = pygame.transform.scale(PionBlanc, (80, 80))
	PionBlanc5 = pygame.transform.scale(PionBlanc, (80, 80))
	PionBlanc6 = pygame.transform.scale(PionBlanc, (80, 80))
	PionBlanc7 = pygame.transform.scale(PionBlanc, (80, 80))
	PionBlanc8 = pygame.transform.scale(PionBlanc, (80, 80))

	TourBlanche = image.load("Interface/Pièces/TourBlanche.png").convert_alpha()
	TourBlanche1 = pygame.transform.scale(TourBlanche, (80, 80))
	TourBlanche2 = pygame.transform.scale(TourBlanche, (80, 80))

	CavalierBlanc = image.load("Interface/Pièces/CavalierBlanc.png").convert_alpha()
	CavalierBlanc1 = pygame.transform.scale(CavalierBlanc, (80, 80))
	CavalierBlanc2 = pygame.transform.scale(CavalierBlanc, (80, 80))

	FouBlanc = image.load("Interface/Pièces/FouBlanc.png").convert_alpha()
	FouBlanc1 = pygame.transform.scale(FouBlanc, (80, 80))
	FouBlanc2 = pygame.transform.scale(FouBlanc, (80, 80))

	RoiBlanc = image.load("Interface/Pièces/RoiBlanc.png").convert_alpha()
	RoiBlanc = pygame.transform.scale(RoiBlanc, (80, 80))

	ReineBlanche = image.load("Interface/Pièces/ReineBlanche.png").convert_alpha()
	ReineBlanche = pygame.transform.scale(ReineBlanche, (80,80))
	
	
	#Importation des pièces noires
	PionNoir = image.load("Interface/Pièces/PionNoir.png").convert_alpha()
	PionNoir1 = pygame.transform.scale(PionNoir, (80, 80))
	PionNoir2 = pygame.transform.scale(PionNoir, (80, 80))
	PionNoir3 = pygame.transform.scale(PionNoir, (80, 80))
	PionNoir4 = pygame.transform.scale(PionNoir, (80, 80))
	PionNoir5 = pygame.transform.scale(PionNoir, (80, 80))
	PionNoir6 = pygame.transform.scale(PionNoir, (80, 80))
	PionNoir7 = pygame.transform.scale(PionNoir, (80, 80))
	PionNoir8 = pygame.transform.scale(PionNoir, (80, 80))

	TourNoire = image.load("Interface/Pièces/TourNoire.png").convert_alpha()
	TourNoire1 = pygame.transform.scale(TourNoire, (80, 80))
	TourNoire2 = pygame.transform.scale(TourNoire, (80, 80))

	CavalierNoir = image.load("Interface/Pièces/CavalierNoir.png").convert_alpha()
	CavalierNoir1 = pygame.transform.scale(CavalierNoir, (80, 80))
	CavalierNoir2 = pygame.transform.scale(CavalierNoir, (80, 80))

	FouNoir = image.load("Interface/Pièces/FouNoir.png").convert_alpha()
	FouNoir1 = pygame.transform.scale(FouNoir, (80, 80))
	FouNoir2 = pygame.transform.scale(FouNoir, (80, 80))

	RoiNoir = image.load("Interface/Pièces/RoiNoir.png").convert_alpha()
	RoiNoir = pygame.transform.scale(RoiNoir, (80, 80))

	ReineNoire = image.load("Interface/Pièces/ReineNoire.png").convert_alpha()
	ReineNoire = pygame.transform.scale(ReineNoire, (80,80))

	plateau = {(0, 0): TourBlanche1, (0, 1): PionBlanc1, (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): PionNoir1, (0, 7): TourNoire1, 
           (1, 0): CavalierBlanc1, (1, 1): PionBlanc2, (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): PionNoir2, (1, 7): CavalierNoir1,
           (2, 0): FouBlanc1, (2, 1): PionBlanc3, (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): PionNoir3, (2, 7): FouNoir1,
           (3, 0): RoiBlanc, (3, 1): PionBlanc4, (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): PionNoir4, (3, 7): ReineNoire,
           (4, 0): ReineBlanche, (4, 1): PionBlanc5, (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): PionNoir5, (4, 7): RoiNoir,
           (5, 0): FouBlanc2, (5, 1): PionBlanc6, (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): PionNoir6, (5, 7): FouNoir2,
           (6, 0): CavalierBlanc2, (6, 1): PionBlanc7, (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): PionNoir7, (6, 7): CavalierNoir2,
           (7, 0): TourBlanche2, (7, 1): PionBlanc8, (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): PionNoir8, (7, 7): TourNoire2}

	for cle, valeur in plateau.items():
		if valeur == '':
			pass
		else :
			fenetre.blit(valeur, (cle[0]*80, cle[1]*80))

		#Rafraichissement
		pygame.display.flip()

	while True:
		for event in pygame.event.get():    #On parcours la liste de tous les événements reçus
			if event.type == QUIT:    	 	#Si un de ces événements est de type QUIT
				pygame.quit()     			#On arrête le programme
				MenuStart()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:	#Si clic gauche
					mouse = event.pos
					if plateau[int(mouse[0]/80), int(mouse[1]/80)] =='':
						pass
					else:
						event_happened = False
						while not event_happened:
							event = pygame.event.wait()
							if event.type == MOUSEBUTTONDOWN:
								if event.button == 1:	#Si clic gauche
									mouse2 = event.pos
									plateau[(int(mouse2[0]/80),int(mouse2[1]/80))]= plateau[(int(mouse[0]/80), int(mouse[1]/80))]
									plateau[(int(mouse[0]/80), int(mouse[1]/80))] = ''
									event_happened = True
	
	
		#Re-collage
		fenetre.blit(Damier, (0,0))	
		for cle, valeur in plateau.items():
			if valeur == '':
					pass
			else :
				fenetre.blit(valeur, (cle[0]*80, cle[1]*80))
		#Rafraichissement
		pygame.display.flip()						


def CréationTexte(text, font, couleur):
    textSurface = font.render(text, True, couleur)
    return textSurface, textSurface.get_rect()

def MenuStart():
	#On crée la fenêtre
	Menu = pygame.display.set_mode((500, 335), RESIZABLE)
	
	#Importation du fond
	Fond = image.load("Interface/FondMenu.jpg").convert()
	Fond = pygame.transform.scale(Fond, (500, 335)) #On met la fenêtre à la bonne taille
	Menu.blit(Fond, (0,0))
	
	#Initialisation du titre du jeu
	pygame.draw.rect(Menu, (255,255,255) , (175-100, 10 , 350, 35 ) )
	pygame.draw.rect(Menu, (0,0,0) , (175-100, 10 , 350, 35 ) , 1)
	pygame.font.init()		#On initialise la création de texte sur pygame
	TexteSurface = pygame.font.SysFont('Times New Roman', 30)	#On choisit la police d'écriture et la taille de la police du texte
	TexteMenu, TextRectMenu = CréationTexte('Garry Kasparov simulator', TexteSurface , (0, 0, 0))
	TextRectMenu.center = ((500/2),(25)) #On centre le texte
	Menu.blit(TexteMenu, TextRectMenu)
	while True:
		for event in pygame.event.get():    #On parcours la liste de tous les événements reçus
			if event.type == QUIT:    	 	#Si un de ces événements est de type QUIT
				pygame.quit()     			#On arrête le programme

		#Création des boutons
		mouse = pygame.mouse.get_pos()
		#Création du bouton démarrage de partie
		if 250+70 > mouse[0] > 250-70 and 275/2+30 > mouse[1] > 275/2:
			pygame.draw.rect(Menu, '#00FFFF' , (250-70, 275/2 , 140, 30 ) ) #Pour le mettre en évidence, le bouton change de couleur quand la souris est dessus
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:	#Si clic gauche
					pygame.quit()
					Echiquier()
		else:
			pygame.draw.rect(Menu, '#0080ff' , (250-70, 275/2 , 140, 30 ) )

		pygame.draw.rect(Menu, (0,0,0) , (250-70, 275/2 , 140, 30 ) , 1)
		ButtonStart = pygame.font.SysFont('Times New Roman',15)
		TextSurf, TextRect = CréationTexte("Démarrer une partie", ButtonStart, (0,0,0))
		TextRect.center = ((500/2),(275/2+30/2))
		Menu.blit(TextSurf, TextRect)

		#Création du bouton quitter la partie
		if 250+70 > mouse[0] > 250-70 and 435/2+30 > mouse[1] > 435/2:
			pygame.draw.rect(Menu, '#8B0000' , (250-70, 435/2 , 140, 30 ) )
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:	#Si clic gauche
					pygame.quit()
		else:
			pygame.draw.rect(Menu, '#DC143C' , (250-70, 435/2 , 140, 30 ) )

		pygame.draw.rect(Menu, (0,0,0) , (250-70, 435/2 , 140, 30 ) , 1)
		ButtonStart = pygame.font.SysFont('Times New Roman',15)
		TextSurf, TextRect = CréationTexte("Quitter le jeu", ButtonStart, (0,0,0))
		TextRect.center = ((500/2),(435/2+30/2))
		Menu.blit(TextSurf, TextRect)


		pygame.display.update()
		clock.tick(15)

MenuStart()