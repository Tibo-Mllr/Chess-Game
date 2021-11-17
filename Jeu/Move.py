from Chess import *
import copy

plateau = {(0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): '', (0, 7): '', (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): '', (1, 7): '', (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): '', (2, 7): '', (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): '', (3, 7): '', (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (4, 7): '', (5, 0): '', (5, 1): '', (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (5, 7): '', (6, 0): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): '', (6, 7): '', (7, 0): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (7, 7): ''}


def case_color(x, y):
    if case_libre(x, y) == False:
        return plateau[(x, y)].Color


def case_libre(x, y):  # fonction qui dit si une case est libre
    if plateau[(x, y)] == '':
        return True
    else:
        return False


def mvt_possible_pion(pion):  # Renvoie une liste de coup possible d'un pion donné
    mvt_possible = []
    if pion.Color == 'White':  # Si le pion est blanc
        if pion.Pos_Y != 0:  # verifie si il peut manger une piece en haut a gauche si le pion n'est pas tout a gauche
            if case_libre(pion.Pos_X + 1, pion.Pos_Y - 1) == False:
                if case_color(pion.Pos_X + 1, pion.Pos_Y - 1) == 'Black':
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X + 1, pion.Pos_Y - 1)]
        if pion.Pos_Y != 7:  # verifie si il peut manger une piece en haut a droite si le pion n'est pas tout a droite
            if case_libre(pion.Pos_X + 1, pion.Pos_Y + 1) == False:
                if case_color(pion.Pos_X + 1, pion.Pos_Y - 1) == 'Black':
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X + 1, pion.Pos_Y + 1)]
        # verifie si le pion peut avancer de 2 si il n'a pas encore bougé
        if pion.Pos_X == 1 and case_libre(pion.Pos_X + 1, pion.Pos_Y) and case_libre(pion.Pos_X + 2, pion.Pos_Y):
            mvt_possible = mvt_possible + [(pion.Pos_X + 2, pion.Pos_Y)]
        if case_libre(pion.Pos_X + 1, pion.Pos_Y):  # verifie si le pion peut avancer de 1
            mvt_possible = mvt_possible + [(pion.Pos_X + 1, pion.Pos_Y)]
    if pion.Color == 'Black':  # si le pion est noir
        if pion.Pos_Y != 0:  # verifie si le pion peut manger à sa droite
            if case_libre(pion.Pos_X - 1, pion.Pos_Y - 1):
                if case_color(pion.Pos_X - 1, pion.Pos_Y - 1):
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X - 1, pion.Pos_Y - 1)]
        if pion.Pos_Y != 7:  # verifie si le pion peut manger à sa gauche
            if case_libre(pion.Pos_X - 1, pion.Pos_Y + 1):
                if case_color(pion.Pos_X - 1, pion.Pos_Y + 1):
                    mvt_possible = mvt_possible + [(pion.Pos_X - 1, pion.Pos_Y + 1)]
        if pion.Pos_X == 6 and case_libre(pion.Pos_X - 1 , pion.Pos_Y) and case_libre(pion.Pos_X - 2 , pion.Pos_Y): #verifie si le pion peut avancé de 2 si il n'a pas encore bougé
            mvt_possible = mvt_possible + [(pion.Pos_X - 2 , pion.Pos_Y)]
        if case_libre(pion.Pos_X - 1 , pion.Pos_Y): #verifie si le pion peut avancer de 1
            mvt_possible = mvt_possible + [(pion.Pos_X - 1 , pion.Pos_Y)]
    return mvt_possible


def mvt_possible_tour(tour):  # nouvelle fonction de deplacement possible de la tour
    mvt_possible = []
    finhaut = False  # variables qui determineront quand s'arrete la boucle for
    finbas = False
    fingauche = False
    findroite = False
    if tour.Pos_X != 7:  # on verifie les deplacements en haut et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, 8 - tour.Pos_X):
            if finhaut == False:
                if case_libre(tour.Pos_X + i, tour.Pos_y):
                    mvt_possible = mvt_possible + \
                        [(tour.Pos_X + i, tour.Pos_y)]
                else:
                    finhaut = True
                    if case_color(tour.Pos_X + i, tour.Pos_y) != tour.Color:
                        mvt_possible = mvt_possible + \
                            [(tour.Pos_X + i, tour.Pos_y)]
    if tour.Pos_Y != 0:  # on verifie les deplacements en bas et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, tour.Pos_X + 1):
            if finbas == False:
                if case_libre(tour.Pos_X - i, tour.Pos_Y):
                    mvt_possible = mvt_possible + \
                        [(tour.Pos_X - i, tour.Pos_Y)]
                else:
                    finbas = True
                    if case_color(tour.Pos_X - i, tour.Pos_Y) != tour.Color:
                        mvt_possible = mvt_possible + \
                            [(tour.Pos_X - i, tour.Pos_Y)]
    if tour.Pos_Y != 0:  # on verifie les deplacements a gauche et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, tour.Pos_Y + 1):
            if fingauche == False:
                if case_libre(tour.Pos_X, tour.Pos_Y - i):
                    mvt_possible = mvt_possible + \
                        [(tour.Pos_X, tour.Pos_Y - i)]
                else:
                    fingauche = True
                    if case_color(tour.Pos_X, tour.Pos_Y - i) != tour.Color:
                        mvt_possible = mvt_possible + \
                            [(tour.Pos_X, tour.Pos_Y - i)]
    if tour.Pos_Y != 8:  # on verifie les deplacements a droite et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, 8-tour.Pos_Y):
            if findroite == False:
                if case_libre(tour.Pos_X, tour.PosY + i):
                    mvt_possible = mvt_possible + [(tour.Pos_X, tour.PosY + i)]
                else:
                    findroite = True
                    if case_color(tour.Pos_X, tour.PosY + i):
                        mvt_possible = mvt_possible + \
                            [(tour.Pos_X, tour.PosY + i)]
    return mvt_possible


def mvt_possible_fou(fou):
    mvt_possible = []
    finhautgauche = False
    finbasgauche = False
    finhautdroite = False
    finbasdroite = False
    if fou.Pos_X != 8 and fou.Pos_Y != 0:
        for i in range(1, min(8-fou.Pos_X, 1 + fou.Pos_Y)):
            if finhautgauche == False:
                if case_libre(fou.Pos_X + i, fou.Pos_Y - i):
                    mvt_possible = mvt_possible + \
                        [(fou.Pos_X + i, fou.Pos_Y - i)]
                else:
                    finhautgauche = True
                    if case_color(fou.Pos_X + i, fou.Pos_Y - i) != fou.Color:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X + i, fou.Pos_Y - i)]
    if fou.Pos_X != 0 and fou.Pos_Y != 0:
        for i in range(1, min(1 + fou.Pos_X, 1 + fou.Pos_Y)):
            if finbasgauche == False:
                if case_libre(fou.Pos_X - i, fou.Pos_Y - i):
                    mvt_possible = mvt_possible + \
                        [(fou.Pos_X - i, fou.Pos_Y - i)]
                else:
                    finbasgauche = True
                    if case_color(fou.Pos_X - i, fou.Pos_Y - i) != fou.Color:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X - i, fou.Pos_Y - i)]
    if fou.Pos_X != 8 and fou.Pos_Y != 8:
        for i in range(1, min(8-fou.Pos_X, 8-fou.Pos_Y)):
            if finhautdroite == False:
                if case_libre(fou.Pos_X + i, fou.Pos_Y + i):
                    mvt_possible = mvt_possible + \
                        (fou.Pos_X + i, fou.Pos_Y + i)
                else:
                    finhautdroite = True
                    if case_color(fou.Pos_X + i, fou.Pos_Y + i) != fou.Color:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X + i, fou.Pos_Y + i)]
    if fou.Pos_X != 0 and fou.Pos_Y != 8:
        for i in range(1, min(1 + fou.Pos_X, 8 - fou.Pos_Y)):
            if finbasdroite == False:
                if case_libre(fou.Pos_X - i, fou.Pos_X + i):
                    mvt_possible = mvt_possible + \
                        [(fou.Pos_X - i, fou.Pos_X + i)]
                else:
                    finbasdroite = True
                    if case_color(fou.Pos_X - i, fou.Pos_X + i) != 0:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X - i, fou.Pos_X + i)]
    return mvt_possible


def mvt_possible_dame(dame):
    mvt_possible = []
    finhaut = False  # variables qui determineront quand s'arrete la boucle for
    finbas = False
    fingauche = False
    findroite = False
    if dame.Pos_X != 7:  # on verifie les deplacements en haut et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, 8 - dame.Pos_X):
            if finhaut == False:
                if case_libre(dame.Pos_X + i, dame.Pos_y):
                    mvt_possible = mvt_possible + \
                        [(dame.Pos_X + i, dame.Pos_y)]
                else:
                    finhaut = True
                    if case_color(dame.Pos_X + i, dame.Pos_y) != dame.Color:
                        mvt_possible = mvt_possible + \
                            [(dame.Pos_X + i, dame.Pos_y)]
    if dame.Pos_Y != 0:  # on verifie les deplacements en bas et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, dame.Pos_X + 1):
            if finbas == False:
                if case_libre(dame.Pos_X - i, dame.Pos_Y):
                    mvt_possible = mvt_possible + \
                        [(dame.Pos_X - i, dame.Pos_Y)]
                else:
                    finbas = True
                    if case_color(dame.Pos_X - i, dame.Pos_Y) != dame.Color:
                        mvt_possible = mvt_possible + \
                            [(dame.Pos_X - i, dame.Pos_Y)]
    if dame.Pos_Y != 0:  # on verifie les deplacements a gauche et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, dame.Pos_Y + 1):
            if fingauche == False:
                if case_libre(dame.Pos_X, dame.Pos_Y - i):
                    mvt_possible = mvt_possible + \
                        [(dame.Pos_X, dame.Pos_Y - i)]
                else:
                    fingauche = True
                    if case_color(dame.Pos_X, dame.Pos_Y - i) != dame.Color:
                        mvt_possible = mvt_possible + \
                            [(dame.Pos_X, dame.Pos_Y - i)]
    if dame.Pos_Y != 8:  # on verifie les deplacements a droite et on s'arrete quand on bute sur une piece et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, 8-dame.Pos_Y):
            if findroite == False:
                if case_libre(dame.Pos_X, dame.PosY + i):
                    mvt_possible = mvt_possible + [(dame.Pos_X, dame.PosY + i)]
                else:
                    findroite = True
                    if case_color(dame.Pos_X, dame.PosY + i):
                        mvt_possible = mvt_possible + \
                            [(dame.Pos_X, dame.PosY + i)]
    finhautgauche = False
    finbasgauche = False
    finhautdroite = False
    finbasdroite = False
    if dame.Pos_X != 8 and dame.Pos_Y != 0:
        for i in range(1, min(8-dame.Pos_X, 1 + dame.Pos_Y)):
            if finhautgauche == False:
                if case_libre(dame.Pos_X + i, dame.Pos_Y - i):
                    mvt_possible = mvt_possible + \
                        [(dame.Pos_X + i, dame.Pos_Y - i)]
                else:
                    finhautgauche = True
                    if case_color(dame.Pos_X + i, dame.Pos_Y - i) != dame.Color:
                        mvt_possible = mvt_possible + \
                            [(dame.Pos_X + i, dame.Pos_Y - i)]
    if dame.Pos_X != 0 and dame.Pos_Y != 0:
        for i in range(1, min(1 + dame.Pos_X, 1 + dame.Pos_Y)):
            if finbasgauche == False:
                if case_libre(dame.Pos_X - i, dame.Pos_Y - i):
                    mvt_possible = mvt_possible + \
                        [(dame.Pos_X - i, dame.Pos_Y - i)]
                else:
                    finbasgauche = True
                    if case_color(dame.Pos_X - i, dame.Pos_Y - i) != dame.Color:
                        mvt_possible = mvt_possible + \
                            [(dame.Pos_X - i, dame.Pos_Y - i)]
    if dame.Pos_X != 8 and dame.Pos_Y != 8:
        for i in range(1, min(8-dame.Pos_X, 8-dame.Pos_Y)):
            if finhautdroite == False:
                if case_libre(dame.Pos_X + i, dame.Pos_Y + i):
                    mvt_possible = mvt_possible + \
                        (dame.Pos_X + i, dame.Pos_Y + i)
                else:
                    finhautdroite = True
                    if case_color(dame.Pos_X + i, dame.Pos_Y + i) != dame.Color:
                        mvt_possible = mvt_possible + \
                            [(dame.Pos_X + i, dame.Pos_Y + i)]
    if dame.Pos_X != 0 and dame.Pos_Y != 8:
        for i in range(1, min(1 + dame.Pos_X, 8 - dame.Pos_Y)):
            if finbasdroite == False:
                if case_libre(dame.Pos_X - i, dame.Pos_X + i):
                    mvt_possible = mvt_possible + \
                        [(dame.Pos_X - i, dame.Pos_X + i)]
                else:
                    finbasdroite = True
                    if case_color(dame.Pos_X - i, dame.Pos_X + i) != 0:
                        mvt_possible = mvt_possible + \
                            [(dame.Pos_X - i, dame.Pos_X + i)]
    return mvt_possible


def mvt_possible_cavalier(cavalier):
    mvt_possible = []
    if cavalier.Pos_X < 6:
        if cavalier.Pos_Y != 0:
            if case_libre(cavalier.Pos_X + 2, cavalier.Pos_Y - 1):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X + 2, cavalier.Pos_Y - 1)]
            else:
                if case_color(cavalier.Pos_X + 2, cavalier.Pos_Y - 1) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X + 2, cavalier.Pos_Y - 1)]
        if cavalier.Pos_Y != 7:
            if case_libre(cavalier.Pos_X + 2, cavalier.Pos_Y + 1):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X + 2, cavalier.Pos_Y + 1)]
            else:
                if case_color(cavalier.Pos_X + 2, cavalier.Pos_Y + 1) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X + 2, cavalier.Pos_Y + 1)]
    if cavalier.Pos_X > 1:
        if cavalier.Pos_Y != 0:
            if case_libre(cavalier.Pos_X - 2, cavalier.Pos_Y - 1):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X - 2, cavalier.Pos_Y - 1)]
            else:
                if case_color(cavalier.Pos_X - 2, cavalier.Pos_Y - 1) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X - 2, cavalier.Pos_Y - 1)]
        if cavalier.Pos_Y != 7:
            if case_libre(cavalier.Pos_X - 2, cavalier.Pos_Y + 1):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X - 2, cavalier.Pos_Y + 1)]
            else:
                if case_color(cavalier.Pos_X - 2, cavalier.Pos_Y + 1) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X - 2, cavalier.Pos_Y + 1)]
    if cavalier.Pos_Y < 6:
        if cavalier.Pos_X != 0:
            if case_libre(cavalier.Pos_X - 1, cavalier.Pos_Y + 2):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X - 1, cavalier.Pos_Y + 2)]
            else:
                if case_color(cavalier.Pos_X - 1, cavalier.Pos_Y + 2) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X - 1, cavalier.Pos_Y + 2)]
        if cavalier.Pos_X != 7:
            if case_libre(cavalier.Pos_X + 1, cavalier.Pos_Y + 2):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X + 1, cavalier.Pos_Y + 2)]
            else:
                if case_color(cavalier.Pos_X + 1, cavalier.Pos_Y + 2) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X + 1, cavalier.Pos_Y + 2)]
    if cavalier.Pos_Y > 1:
        if cavalier.Pos_X != 0:
            if case_libre(cavalier.Pos_X - 1, cavalier.Pos_Y - 2):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X - 1, cavalier.Pos_Y - 2)]
            else:
                if case_color(cavalier.Pos_X - 1, cavalier.Pos_Y - 2) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X - 1, cavalier.Pos_Y - 2)]
        if cavalier.Pos_X != 7:
            if case_libre(cavalier.Pos_X + 1, cavalier.Pos_Y - 2):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X + 1, cavalier.Pos_Y - 2)]
            else:
                if case_color(cavalier.Pos_X + 1, cavalier.Pos_Y - 2) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X + 1, cavalier.Pos_Y - 2)]
    return mvt_possible


def mvt_possible_gen(piece):
    if piece.name == 'cavalier':
        return mvt_possible_cavalier(piece)
    if piece.name == 'roi':
        return mvt_possible_roi(piece)
    if piece.name == 'dame':
        return mvt_possible_dame(piece)
    if piece.name == 'fou':
        return mvt_possible_fou(piece)
    if piece.name == 'tour':
        return mvt_possible_tour(piece)
    if piece.name == 'pion':
        return mvt_possible_pion(piece)


def roi_en_echec(roi):
    echec = False
    for piece in plateau.values():
        if (roi.Pos_X , roi.Pos_Y) in mvt_possible_gen(piece):
            echec = True
    return echec


def echec_si_mouvement_du_roi(roi, x, y):  # a revoir
    newplateau = copy.deepcopy(plateau)
    newplateau((roi.Pos_X, roi.Pos_Y)) = ''
    newplateau((x, y)) = roi
    echec_si_mvt = False
    for piece in newplateau.values():
        if piece != '':
            if (x , y) in mvt_possible_gen(piece):
                echec = True
    return echec_si_mvt


def mvt_possible_roi(roi):
    mvt_possible = []
    if roi.Pos_X != 0:
        if case_libre(roi.Pos_X - 1, roi.Pos_Y) and not echec_si_mouvement_du_roi(roi.Pos_X - 1, roi.Pos_Y):
            mvt_possible = mvt_possible + [(roi.Pos_X - 1, roi.Pos_Y)]
        else:
            if case_color(roi.Pos_X - 1, roi.Pos_Y) != roi.Color and not echec_si_mouvement_du_roi(roi.Pos_X - 1, roi.Pos_Y):
                mvt_possible = mvt_possible + [(roi.Pos_X - 1, roi.Pos_Y)]
        if roi.Pos_Y != 0:
            if case_libre(roi.Pos_X - 1, roi.Pos_Y - 1) and not echec_si_mouvement_du_roi(roi.Pos_X - 1, roi.Pos_Y - 1):
                mvt_possible = mvt_possible + [(roi.Pos_X - 1, roi.Pos_Y - 1)]
            else:
                if case_color(roi.Pos_X - 1, roi.Pos_Y - 1) != roi.Color and not echec_si_mouvement_du_roi(roi.Pos_X - 1, roi.Pos_Y - 1):
                    mvt_possible = mvt_possible + \
                        [(roi.Pos_X - 1, roi.Pos_Y - 1)]
        if roi.Pos_Y != 7:
            if case_libre(roi.Pos_X - 1, roi.Pos_Y + 1) and not echec_si_mouvement_du_roi(roi.Pos_X - 1, roi.Pos_Y + 1):
                mvt_possible = mvt_possible + [(roi.Pos_X - 1, roi.Pos_Y + 1)]
            else:
                if case_color(roi.Pos_X - 1, roi.Pos_Y + 1) != roi.Color and not echec_si_mouvement_du_roi(roi.Pos_X - 1, roi.Pos_Y + 1):
                    mvt_possible = mvt_possible + \
                        [(roi.Pos_X - 1, roi.Pos_Y + 1)]
    if roi.Pos_X != 7:
        if case_libre(roi.Pos_X + 1, roi.Pos_Y) and not echec_si_mouvement_du_roi(roi.Pos_X + 1, roi.Pos_Y):
            mvt_possible = mvt_possible + [(roi.Pos_X + 1, roi.Pos_Y)]
        else:
            if case_color(roi.Pos_X + 1, roi.Pos_Y) != roi.Color and not echec_si_mouvement_du_roi(roi.Pos_X + 1, roi.Pos_Y):
                mvt_possible = mvt_possible + [(roi.Pos_X + 1, roi.Pos_Y)]
        if roi.Pos_Y != 0:
            if case_libre(roi.Pos_X + 1, roi.Pos_Y - 1) and not echec_si_mouvement_du_roi(roi.Pos_X + 1, roi.Pos_Y - 1):
                mvt_possible = mvt_possible + [(roi.Pos_X + 1, roi.Pos_Y - 1)]
            else:
                if case_color(roi.Pos_X + 1, roi.Pos_Y - 1) != roi.Color and not echec_si_mouvement_du_roi(roi.Pos_X - 1, roi.Pos_Y - 1):
                    mvt_possible = mvt_possible + \
                        [(roi.Pos_X + 1, roi.Pos_Y - 1)]
        if roi.Pos_Y != 7:
            if case_libre(roi.Pos_X + 1, roi.Pos_Y + 1) and not echec_si_mouvement_du_roi(roi.Pos_X + 1, roi.Pos_Y + 1):
                mvt_possible = mvt_possible + [(roi.Pos_X + 1, roi.Pos_Y + 1)]
            else:
                if case_color(roi.Pos_X + 1, roi.Pos_Y + 1) != roi.Color and not echec_si_mouvement_du_roi(roi.Pos_X + 1, roi.Pos_Y + 1):
                    mvt_possible = mvt_possible + \
                        [(roi.Pos_X + 1, roi.Pos_Y + 1)]
    if roi.Pos_Y != 0:
        if case_libre(roi.Pos_X, roi.Pos_Y - 1) and not echec_si_mouvement_du_roi(roi.Pos_X, roi.Pos_Y - 1):
            mvt_possible = mvt_possible + [(roi.Pos_X, roi.Pos_Y - 1)]
        else:
            if case_color(roi.Pos_X, roi.Pos_Y - 1) != roi.color and not echec_si_mouvement_du_roi(roi.Pos_X, roi.Pos_Y - 1):
                mvt_possible = mvt_possible + [(roi.Pos_X, roi.Pos_Y - 1)]
    if roi.Pos_Y != 7:
        if case_libre(roi.Pos_X, roi.Pos_Y + 1) and not echec_si_mouvement_du_roi(roi.Pos_X, roi.Pos_Y + 1):
            mvt_possible = mvt_possible + [(roi.Pos_X, roi.Pos_Y + 1)]
        else:
            if case_color(roi.Pos_X, roi.Pos_Y + 1) != roi.color and not echec_si_mouvement_du_roi(roi.Pos_X, roi.Pos_Y + 1):
                mvt_possible = mvt_possible + [(roi.Pos_X, roi.Pos_Y + 1)]


def echec_si_mvt(piece, x, y):
    newplateau = copy.deepcopy(plateau)
    newplateau((piece.Pos_X , piece.Pos_Y)) = ''
    newplateau((x,y)) = piece
    if piece.color == 'White':
        echec_blanc = False
        for i in newplateau.values():
                if i != '':
                    if (roiblanc.Pos_X , roiblanc.Pos_Y) in mvt_possible_gen(i): #REVOIR LE NOM DU ROI BLANC
                        echec_blanc = True
        return echec_blanc
    if piece.color == 'Black':
        echec_noir = False
        for i in newplateau.values():
            if i != '':
                if (roinoir.Pos_X , roinoir.Pos_Y) in mvt_possible_gen(i): #REVOIR LE NOM DU ROI BLANC
                    echec_noir = True
        return echec_noir
"""
def mvt_final_pion(pion):
    mvt_final = []
    for (x,y) in mvt_possible_pion(pion):
        if echec_si_mvt(pion , x, y) == False:
            mvt_final = mvt_final + [(x,y)]
    return mvt_final

def mvt_final_tour(tour):
    mvt_final = []
    for (x,y) in mvt_possible_tour(tour):
        if echec_si_mvt(tour , x, y) == False:
            mvt_final = mvt_final + [(x,y)]
    return mvt_final

def mvt_final_dame(dame):
    mvt_final = []
    for (x,y) in mvt_possible_dame(dame):
        if echec_si_mvt(dame , x, y) == False:
            mvt_final = mvt_final + [(x,y)]
    return mvt_final

def mvt_final_fou(fou):
    mvt_final = []
    for (x,y) in mvt_possible_fou(fou):
        if echec_si_mvt(fou , x, y) == False:
            mvt_final = mvt_final + [(x,y)]
    return mvt_final
"""

def mvt_final(piece):
    mvt = []
    for (x,y) in mvt_possible_gen(piece):
        if echec_si_mvt(piece , x, y) == False:
            mvt = mvt + [(x,y)]
    return mvt
    
def petit_roque(roi):
    petit_roque_possible = False
    if roi.Color == 'White':
        if roi.Pos_X == 4 and roi.Pos_Y == 0:
            if tourblanche2.Pos_X == 7 and tourblanche2.Pos_X == 0:
                already_moved = False
                for coup in historique:
                    if coup[O] == roi or coup[0] == tourblanche2:
                        already_moved = True
                if case_libre(5 , 0) and case_libre(6 , 0):
                    if not echec_si_mouvement_du_roi(roi , 5 , 0) and not roi_en_echec(roi) and already_moved == False:
                        petit_roque_possible = True
    if roi.Color == 'Black':
        if roi.Pos_X == 3 and roi.Pos_Y == 7:
            if tournoire1.Pos_X == 0 and tournoire1.Pos_X == 7:
                already_moved = False
                for coup in historique:
                    if coup[O] == roi or coup[0] == tournoire1:
                        already_moved = True
                if case_libre(2 , 7) and case_libre(1 , 7):
                    if not echec_si_mouvement_du_roi(roi , 2 , 7) and not roi_en_echec(roi) and already_moved == False:
                        petit_roque_possible = True
    return petit_roque_possible

def grand_roque(roi):
    if roi.Color == 'White':
        grand_roque_possible = False
        if roi.Pos_X == 4 and roi.Pos_Y == 0:
            if tourblanche1.Pos_X == 0 and tourblanche1.Pos_X == 0:
                already_moved = False
                for coup in historique:
                    if coup[O] == roi or coup[0] == tourblanche1:
                        already_moved = True
                if case_libre(1 , 0) and case_libre(2 , 0) and case_libre(3 , 0):
                    if not echec_si_mouvement_du_roi(roi , 2 , 0) and not echec_si_mouvement_du_roi(roi , 3 , 0) and not roi_en_echec(roi) and already_moved == False:
                        grand_roque_possible = True
    if roi.Color == 'Black':
        grand_roque_possible = False
        if roi.Pos_X == 3 and roi.Pos_Y == 7:
            if tournoire2.Pos_X == 7 and tournoire2.Pos_X == 7:
                already_moved = False
                for coup in historique:
                    if coup[O] == roi or coup[0] == tournoire2:
                        already_moved = True
                if case_libre(4 , 7) and case_libre(5 , 7) and case_libre(6 , 7):
                    if not echec_si_mouvement_du_roi(roi , 4 , 7) and not echec_si_mouvement_du_roi(roi , 3 , 7) and not roi_en_echec(roi) and already_moved == False:
                        grand_roque_possible = True
    return grand_roque_possible
# a ajouter dans les fonctions de mouvements des pieces

        
#reste promotion pion
#reste roque

#reste nul en cas de match nul
#reste victoire
    



'''ce serait bien de sauver l'historique des mvts
ca eviterait d'implementer plein de variables poursavoir si le roi a deja bougé pour pouvoir faire un roque
chaque mouvement est un objet dans l'historique
genre une liste qui donne les coups effectués

en plus ca permettrait de rejouer la partie a partir d'une certaine etape
'''
