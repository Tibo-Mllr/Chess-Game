import pygame
from pygame import image
from pygame.locals import *
from pygame.constants import RESIZABLE
import sys

pygame.init()

def Echiquier():
	#Création de la fenêtre
	fenetre = pygame.display.set_mode((800, 800), RESIZABLE)

	#Importation du fond
	Damier = image.load("Damier.png").convert()
	Damier = pygame.transform.scale(Damier, (800, 800))
	fenetre.blit(Damier, (0,0))

	#Importation des poèces
	#Importation des pièces blanches
	PionBlanc = image.load("Pièces/PionBlanc.png").convert_alpha()
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

	TourBlanche = image.load("Pièces/TourBlanche.png").convert_alpha()
	TourBlanche1 = pygame.transform.scale(TourBlanche, (100, 100))
	TourBlanche2 = pygame.transform.scale(TourBlanche, (100, 100))

	CavalierBlanc = image.load("Pièces/CavalierBlanc.png").convert_alpha()
	CavalierBlanc1 = pygame.transform.scale(CavalierBlanc, (100, 100))
	CavalierBlanc2 = pygame.transform.scale(CavalierBlanc, (100, 100))

	FouBlanc = image.load("Pièces/FouBlanc.png").convert_alpha()
	FouBlanc1 = pygame.transform.scale(FouBlanc, (100, 100))
	FouBlanc2 = pygame.transform.scale(FouBlanc, (100, 100))

	RoiBlanc = image.load("Pièces/RoiBlanc.png").convert_alpha()
	RoiBlanc = pygame.transform.scale(RoiBlanc, (100, 100))
	RoiBlanc_x = 200
	RoiBlanc_y = 200
	fenetre.blit(RoiBlanc,(RoiBlanc_x, RoiBlanc_y))

	ReineBlanche = image.load("Pièces/ReineBlanche.png").convert_alpha()
	ReineBlanche = pygame.transform.scale(ReineBlanche, (100,100))

	pygame.display.flip()

	while True:
		for event in pygame.event.get():    #On parcours la liste de tous les événements reçus
			if event.type == QUIT:    	 	#Si un de ces événements est de type QUIT
				pygame.quit()     			#On arrête le programme
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


def MenuStart():

	Menu = pygame.display.set_mode((500, 500), RESIZABLE)
