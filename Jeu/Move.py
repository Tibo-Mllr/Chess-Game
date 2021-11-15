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
    if pion.Color == 'White': #Si le pion est blanc
        if pion.Pos_Y != 0: #verifie si il peut manger une piece en haut a gauche si le pion n'est pas tout a gauche
            if case_libre(pion.Pos_X + 1 , pion.Pos_Y - 1) == False: 
                if case_color(pion.Pos_X + 1 , pion.Pos_Y - 1) == 'Black':
                    mvt_possible = mvt_possible + [(pion.Pos_X + 1 , pion.Pos_Y - 1)]
        if pion.Pos_Y != 7: #verifie si il peut manger une piece en haut a droite si le pion n'est pas tout a droite
            if case_libre(pion.Pos_X + 1 , pion.Pos_Y + 1) == False: 
                if case_color(pion.Pos_X + 1 , pion.Pos_Y - 1) == 'Black':
                    mvt_possible = mvt_possible + [(pion.Pos_X + 1 , pion.Pos_Y + 1)]
        if pion.Moved == False and case_libre(pion.Pos_X + 1 , pion.Pos_Y) and case_libre(pion.Pos_X + 2 , pion.Pos_Y): #verifie si le pion peut avancer de 2 si il n'a pas encore bougé
            mvt_possible = mvt_possible + [(pion.Pos_X + 2 , pion.Pos_Y)]
        if case_libre(pion.Pos_X + 1 , pion.Pos_Y): #verifie si le pion peut avancer de 1
            mvt_possible = mvt_possible + [(pion.Pos_X + 1 , pion.Pos_Y)]
    if pion.Color == 'Black': # si le pion est noir
        if pion.Pos_Y != 0: #verifie si le pion peut manger à sa droite
            if case_libre(pion.Pos_X - 1, pion.Pos_Y - 1):
                if case_color(pion.Pos_X - 1, pion.Pos_Y - 1):
                    mvt_possible = mvt_possible + [(pion.Pos_X - 1, pion.Pos_Y - 1)]
        if pion.Pos_Y != 7: #verifie si le pion peut manger à sa gauche
            if case_libre(pion.Pos_X - 1, pion.Pos_Y + 1):
                if case_color(pion.Pos_X - 1, pion.Pos_Y + 1):
                    mvt_possible = mvt_possible + [(pion.Pos_X - 1, pion.Pos_Y + 1)]
        if pion.Pos_X == 6 and case_libre(pion.Pos_X - 1 , pion.Pos_Y) and case_libre(pion.Pos_X - 2 , pion.Pos_Y): #verifie si le pion peut avancé de 2 si il n'a pas encore bougé
            mvt_possible = mvt_possible + [(pion.Pos_X - 2 , pion.Pos_Y)]
        if case_libre(pion.Pos_X - 1 , pion.Pos_Y): #verifie si le pion peut avancer de 1
            mvt_possible = mvt_possible + [(pion.Pos_X - 1 , pion.Pos_Y)]
    return mvt_possible

"""
def mvt_possible_tour(tour):
    mvt_possible = []
    ihaut = 1
    finhaut = 1
    ibas = -1
    finbas = 1
    igauche = -1
    fingauche = 1
    idroite = 1
    findroite = 1
    
    il va falloir rajouter des if au cas ou la piece est sur une extremité pour eviter d"appliquer la fction case_libre sur un couple de coordonnées en dehors de la grille
    VOIR COMMENTAIRES FOU

    on va plutot regarder la position de base de la tour puis on va deteermineer le nombr d cxase maximum d dplacemeent ^possibl en
    considérant le plateau vide et on aura juste a implémenterr unee variable fin au cas ou ca bute sur quelque chose
    Comme ça pas de while juste un for avec une verification de la variable de fin
    plus facile a implémenter
    
    while case_libre(tour.Pos_X + ihaut , tour.Pos_Y) and tour.Pos_X+ihaut < 8: #répertorie les deplacements possibles vers le haut
        mvt_possible = mvt_possible + [(tour.Pos_X + ihaut , tour.Pos_Y)] #rajoute les cases libres une à une tant qu'elles sont vides
        ihaut = ihaut + 1
    if tour.Pos_X + ihaut < 8:
        if case_libre(tour.Pos_X + ihaut , tour.Pos_Y) == False: #si on bute sur une piece verifie la couleur et rajoute la case si on peut la manger
            if case_color(tour.Pos_X + ihaut , tour.Pos_Y) != tour.Color:
                mvt_possible = mvt_possible + [(tour.Pos_X + ihaut , tour.Pos_Y)]
    while case_libre(tour.Pos_X + ibas , tour.Pos_Y) and tour.Pos_X+ibas >= 0: #répertorie les deplacements possibles vers le bas
        mvt_possible = mvt_possible + [(tour.Pos_X + ibas , tour.Pos_Y)] #rajoute les cases libres une à une tant qu'elles sont vides
        ibas = ibas - 1
    if tour.Pos_X + ibas >= 0:
        if case_libre(tour.Pos_X + ibas , tour.Pos_Y) == False: #si on bute sur une piece verifie la couleur et rajoute la case si on peut la manger
            if case_color(tour.Pos_X + ihaut , tour.Pos_Y) != tour.Color:
                mvt_possible = mvt_possible + [(tour.Pos_X + ibas , tour.Pos_Y)]
    while case_libre(tour.Pos_X , tour.Pos_Y + idroite) and tour.Pos_Y+idroite < 8: #repertorie les deplacements à droite
        mvt_possible = mvt_possible + [(tour.Pos_X , tour.Pos_Y + idroite)] #rajoute les cases libres une à une tant qu'elles sont vides
        idroite = idroite + 1
    if tour.Pos_Y + idroite < 8:
        if case_libre(tour.Pos_X , tour.Pos_Y + idroite) == False: #si on bute sur une piece verifie la couleur et rajoute la case si on peut la manger
            if case_color(tour.Pos_X , tour.Pos_Y + idroite) != tour.Color:
                mvt_possible = mvt_possible + [(tour.Pos_X , tour.Pos_Y + idroite)]
    while case_libre(tour.Pos_X , tour.Pos_Y + igauche) and tour.Pos_Y+igauche >= 0: #repertorie les deplacements à droite
        mvt_possible = mvt_possible + [(tour.Pos_X , tour.Pos_Y + igauche)] #rajoute les cases libres une à une tant qu'elles sont vides
        igauche = igauche + 1
    if tour.Pos_Y + igauche >=0:
        if case_libre(tour.Pos_X , tour.Pos_Y + igauche) == False: #si on bute sur une piece verifie la couleur et rajoute la case si on peut la manger
            if case_color(tour.Pos_X , tour.Pos_Y + igauche) != tour.Color:
                mvt_possible = mvt_possible + [(tour.Pos_X , tour.Pos_Y + igauche)]

    return mvt_possible

""" 

def mvt_possible_tour(tour): #nouvelle fonction de deplacement possible de la tour
    mvt_possible = []
    finhaut = False #variables qui determineront quand s'arrete la boucle for
    finbas = False
    fingauche = False
    findroite = False
    if tour.Pos_X != 7: #on verifie les deplacements en haut et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1,8 - tour.Pos_X ):
            if finhaut == False:
                if case_libre(tour.Pos_X + i , tour.Pos_y):
                    mvt_possible = mvt_possible + [(tour.Pos_X + i , tour.Pos_y)]
                else:
                    finhaut = True
                    if case_color(tour.Pos_X + i , tour.Pos_y) != tour.Color:
                        mvt_possible = mvt_possible + [(tour.Pos_X + i , tour.Pos_y)]
    if tour.Pos_Y != 0: #on verifie les deplacements en bas et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1 , tour.Pos_X + 1):
            if finbas == False:
                if case_libre(tour.Pos_X - i , tour.Pos_Y):
                    mvt_possible = mvt_possible + [(tour.Pos_X - i , tour.Pos_Y)]
                else:
                    finbas = True
                    if case_color(tour.Pos_X - i , tour.Pos_Y) != tour.Color:
                        mvt_possible = mvt_possible + [(tour.Pos_X - i , tour.Pos_Y)]
    if tour.Pos_Y != 0:  #on verifie les deplacements a gauche et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, tour.Pos_Y + 1):
            if fingauche == False:
                if case_libre(tour.Pos_X , tour.Pos_Y - i):
                    mvt_possible = mvt_possible + [(tour.Pos_X , tour.Pos_Y - i)]
                else:
                    fingauche = True
                    if case_color(tour.Pos_X , tour.Pos_Y - i) != tour.Color:
                        mvt_possible = mvt_possible + [(tour.Pos_X , tour.Pos_Y - i)]
    if tour.Pos_Y != 8:  #on verifie les deplacements a droite et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1 , 8-tour.Pos_Y ):
            if findroite == False:
                if case_libre(tour.Pos_X , Tour.PosY + i):
                    mvt_possible = mvt_possible + [(tour.Pos_X , Tour.PosY + i)]
                else:
                    findroite = True
                    if case_color(tour.Pos_X , Tour.PosY + i):
                        mvt_possible = mvt_possible + [(tour.Pos_X , Tour.PosY + i)]
    return mvt_possible






def mvt_possible_fou(fou):
    mvt_possible = []
    finhautgauche = False
    finbasgauche = False
    finhautdroite = False
    finbasdroite = False
    if fou.Pos_X != 8 and fou.Pos_Y != 0: 
        for i in range( 1 , min(8-fou.Pos_X , 1+ fou.Pos_Y)):
             if finhautgauche == False:
                if case_libre(fou.Pos_X + i , fou.Pos_Y - i):
                    mvt_possible = mvt_possible + [(fou.Pos_X + i , fou.Pos_Y - i)]
                else:
                    finhautgauche = True
                    if case_color(fou.Pos_X + i , fou.Pos_Y - i) != fou.Color:
                        mvt_possible = mvt_possible + [(fou.Pos_X + i , fou.Pos_Y - i)]
    if fou.Pos_X != 0 and fou.Pos_Y != 0:
        for i in range( 1 , min (1+ fou.Pos_X, 1+ fou.Pos_Y)):
            if finbasgauche == False:
                if case_libre(fou.Pos_X - i , fou.Pos_Y - i):
                    mvt_possible = mvt_possible + [(fou.Pos_X - i , fou.Pos_Y - i)]
                else:
                    finbasgauche = True
                    if case_color(fou.Pos_X - i , fou.Pos_Y - i) != fou.Color:
                        mvt_possible = mvt_possible + [(fou.Pos_X - i , fou.Pos_Y - i)]
    if fou.Pos_X != 8 and fou.Pos_Y != 8:
        for i in range ( 1 , min(8-fou.Pos_X , 8-fou.Pos_Y)):
            if finhautdroite == False:
                if case_libre(fou.Pos_X + i , fou.Pos_Y + i):
                    mvt_possible = mvt_possible + (fou.Pos_X + i , fou.Pos_Y + i)
                else:
                    finhautdroite = True
                    if case_color(fou.Pos_X + i , fou.Pos_Y + i) != fou.Color:
                        mvt_possible = mvt_possible + [(fou.Pos_X + i , fou.Pos_Y + i)]
    if fou.Pos_X != 0 and fou.Pos_Y != 8:
        for i in range ( 1 , min(1 + fou.Pos_X , 8 - fou.Pos_Y)):
            if finbasdroite == False:
                if case_libre(fou.Pos_X - i , fou.Pos_X + i):
                    mvt_possible = mvt_possible + [(fou.Pos_X - i , fou.Pos_X + i)]
                else:
                    finbasdroite = True
                    if case_color(fou.Pos_X - i , fou.Pos_X + i) != 0:
                        mvt_possible = mvt_possible + [(fou.Pos_X - i , fou.Pos_X + i)]
    return mvt_possible
    


    """if fou.pos_X < 8 and fou.Pos_Y >= 0:
        while fou.Pos_X + ihautgauche < 8 and fou.Pos_Y - ihautgauche >=0 and case_libre(fou.Pos_X + ihautgauche , fou.Pos_Y - ihautgauche):
            mvt_possible = mvt_possible + (fou.Pos_X + ihautgauche , fou.Pos_Y - ihautgauche)
            a revoir toujours le meme oprobleme qu'avant mais sur la suite des etapes de la boucle
            en ajoutant un test qui met fin au while si on touche le bord de la grille a la fin ce serait cool
            ou en ajoutant une constante qui dit si on doit s"arreter comme ca la boucle continue mais on ajoute plus rien c'est pas opti mais a voir
            en ajoutant cette constante et en la mettant dans le while ca marcherait sans pour autant faire des boucles while pour rien
            
            il faut faire le meme changement chez la tour
            """




"""ce serait bien de sauver l'historique des mvts
ca eviterait d'implementer plein de variables poursavoir si le roi a deja bougé pour pouvoir faire un roque
chaque mouvement est un objet dans l'historique
genre une liste qui donne les coups effectués

en plus ca permettrait de rejouer la partie a partir d'une certaine etape"""