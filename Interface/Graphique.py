import pygame
from pygame import image
from pygame.locals import *
from pygame.constants import RESIZABLE
import sys
import time

pygame.init()

clock= pygame.time.Clock()

def Echiquier():
	#Création de la fenêtre
	fenetre = pygame.display.set_mode((800, 800), RESIZABLE)

	#Importation du fond
	Damier = image.load("Interface/Damier.png").convert()
	Damier = pygame.transform.scale(Damier, (800, 800))
	fenetre.blit(Damier, (0,0))

	#Importation des poèces
	#Importation des pièces blanches
	PionBlanc = image.load("Interface/Pièces/PionBlanc.png").convert_alpha()
	PionBlanc1 = pygame.transform.scale(PionBlanc, (100, 100))
	PionBlanc2 = pygame.transform.scale(PionBlanc, (100, 100))
	PionBlanc3 = pygame.transform.scale(PionBlanc, (100, 100))
	PionBlanc4 = pygame.transform.scale(PionBlanc, (100, 100))
	PionBlanc5 = pygame.transform.scale(PionBlanc, (100, 100))
	PionBlanc6 = pygame.transform.scale(PionBlanc, (100, 100))
	PionBlanc7 = pygame.transform.scale(PionBlanc, (100, 100))
	PionBlanc8 = pygame.transform.scale(PionBlanc, (100, 100))
	fenetre.blit(PionBlanc1, (0, 600))
	fenetre.blit(PionBlanc2, (100, 600))

	TourBlanche = image.load("Interface/Pièces/TourBlanche.png").convert_alpha()
	TourBlanche1 = pygame.transform.scale(TourBlanche, (100, 100))
	TourBlanche2 = pygame.transform.scale(TourBlanche, (100, 100))

	CavalierBlanc = image.load("Interface/Pièces/CavalierBlanc.png").convert_alpha()
	CavalierBlanc1 = pygame.transform.scale(CavalierBlanc, (100, 100))
	CavalierBlanc2 = pygame.transform.scale(CavalierBlanc, (100, 100))

	FouBlanc = image.load("Interface/Pièces/FouBlanc.png").convert_alpha()
	FouBlanc1 = pygame.transform.scale(FouBlanc, (100, 100))
	FouBlanc2 = pygame.transform.scale(FouBlanc, (100, 100))

	RoiBlanc = image.load("Interface/Pièces/RoiBlanc.png").convert_alpha()
	RoiBlanc = pygame.transform.scale(RoiBlanc, (100, 100))
	RoiBlanc_x = 200
	RoiBlanc_y = 200
	fenetre.blit(RoiBlanc,(RoiBlanc_x, RoiBlanc_y))

	ReineBlanche = image.load("Interface/Pièces/ReineBlanche.png").convert_alpha()
	ReineBlanche = pygame.transform.scale(ReineBlanche, (100,100))

	pygame.display.flip()

	while True:
		for event in pygame.event.get():    #On parcours la liste de tous les événements reçus
			if event.type == QUIT:    	 	#Si un de ces événements est de type QUIT
				pygame.quit()     			#On arrête le programme
				MenuStart()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:	#Si clic gauche
					RoiBlanc_x = int(event.pos[0]/100)*100
					RoiBlanc_y = int(event.pos[1]/100)*100

	#Re-collage
		fenetre.blit(Damier, (0,0))	
		fenetre.blit(RoiBlanc, (RoiBlanc_x, RoiBlanc_y))
		fenetre.blit(TourBlanche1, (200,300))
		fenetre.blit(PionBlanc1, (0, 600))
		fenetre.blit(PionBlanc2, (100, 600))
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