from chess.py import *

plateau = {(0,0):'' , (0,1):'' , (0,2):'' , (0,3):'' , (0,4):'' , (0,5):'' , (0,6):'' , (0,7):'' , (1,0):'' , (1,1):'' , (1,2):'' , (1,3):'' , (1,4):'' , (1,5):'' , (1,6):'' , (1,7):'' , (2,0):'' , (2,1):'' , (2,2):'' , (2,3):'' , (2,4):'' , (2,5):'' , (2,6):'' , (2,7):'' , (3,0):'' , (3,1):'' , (3,2):'' , (3,3):'' , (3,4):'' , (3,5):'' , (3,6):'' , (3,7):'' , (4,0):'' , (4,1):'' , (4,2):'' , (4,3):'' , (4,4):'' , (4,5):'' , (4,6):'' , (4,7):'' , (5,0):'' , (5,1):'' , (5,2):'' , (5,3):'' , (5,4):'' , (5,5):'' , (5,6):'' , (5,7):'' , (6,0):'' , (6,1):'' , (6,2):'' , (6,3):'' , (6,4):'' , (6,5):'' , (6,6):'' , (6,7):'' , (7,0):'' , (7,1):'' , (7,2):'' , (7,3):'' , (7,4):'' , (7,5):'' , (7,6):'' , (7,7):''}

def case_color(x,y):
    if case_libre(x,y) == False:
        return plateau[(x,y)].Color

def case_libre(x,y): #fonction qui dit si une case est libre
    if plateau[(x,y)] == '':
        return True
    else:
        return False



def mvt_possible_pion(pion): #Renvoie une liste de coup possible d'un pion donné
    mvt_possible = []
    if pion.Color == 'White':
        if pion.Pos_Y != 0: #verifie si il peut manger une piece en haut a gauche si le pion n'est pas tout a gauche
            if case_libre(pion.Pos_X + 1 , pion.Pos_Y - 1) == False: 
                if case_color == 'Black':
                    mvt_possible = mvt_possible + [(pion.Pos_X + 1 , pion.Pos_Y - 1)]
        if pion.Pos_Y != 7: #verifie si il peut manger une piece en haut a droite si le pion n'est pas tout a droite
            if case_libre(pion.Pos_X + 1 , pion.Pos_Y + 1) == False: 
                if case_color == 'Black':
                    mvt_possible = mvt_possible + [(pion.Pos_X + 1 , pion.Pos_Y + 1)]
        if pion.Moved == False and case_libre(pion.Pos_X + 1 , pion.Pos_Y) and case_libre(pion.Pos_X + 2 , pion.Pos_Y): #verifie si le pion peut avancer de 2 si il n'a pas encore bougé
            mvt_possible = mvt_possible + [(pion.Pos_X + 2 , pion.Pos_Y)]
        if case_libre(pion.Pos_X + 1 , pion.Pos_Y): #verifie si le pion peut avancer de 1
            mvt_possible = mvt_possible + [(pion.Pos_X + 1 , pion.Pos_Y)]
    if pion.Color == 'Black':