from Chess import *
import copy

Plateau = {(0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): '', (0, 7): '',
           (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): '', (1, 7): '',
           (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): '', (2, 7): '',
           (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): '', (3, 7): '',
           (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (4, 7): '',
           (5, 0): '', (5, 1): '', (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (5, 7): '',
           (6, 0): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): '', (6, 7): '',
           (7, 0): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (7, 7): ''}


def case_color(x, y, plateau):
    if case_libre(x, y, plateau) == False:
        return plateau[(x, y)].Color


def case_libre(x, y, plateau):  # fonction qui dit si une case est libre
    if plateau[(x, y)] == '':
        return True
    else:
        return False


# Renvoie une liste de coup possible d'un pion donné
def mvt_possible_pion(pion, plateau):
    mvt_possible = []
    if pion.Color == 'White':  # Si le pion est blanc
        if pion.Pos_X != 0:  # verifie si il peut manger une piece en haut a gauche si le pion n'est pas tout a gauche
            if case_libre(pion.Pos_X - 1, pion.Pos_Y + 1, plateau) == False:
                if case_color(pion.Pos_X - 1, pion.Pos_Y + 1, plateau) == 'Black':
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X - 1, pion.Pos_Y + 1)]
        if pion.Pos_X != 7:  # verifie si il peut manger une piece en haut a droite si le pion n'est pas tout a droite
            if case_libre(pion.Pos_X + 1, pion.Pos_Y + 1, plateau) == False:
                if case_color(pion.Pos_X + 1, pion.Pos_Y + 1, plateau) == 'Black':
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X + 1, pion.Pos_Y + 1)]
        # verifie si le pion peut avancer de 2 si il n'a pas encore bougé
        if pion.Pos_Y == 1 and case_libre(pion.Pos_X, pion.Pos_Y+1, plateau) and case_libre(pion.Pos_X, pion.Pos_Y + 2, plateau):
            mvt_possible = mvt_possible + [(pion.Pos_X, pion.Pos_Y+2)]
        # verifie si le pion peut avancer de 1
        if case_libre(pion.Pos_X, pion.Pos_Y+1, plateau):
            mvt_possible = mvt_possible + [(pion.Pos_X, pion.Pos_Y+1)]
    if pion.Color == 'Black':  # si le pion est noir
        if pion.Pos_X != 0:  # verifie si le pion peut manger à sa droite
            if case_libre(pion.Pos_X - 1, pion.Pos_Y - 1, plateau):
                if case_color(pion.Pos_X - 1, pion.Pos_Y - 1, plateau):
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X - 1, pion.Pos_Y - 1)]
        if pion.Pos_X != 7:  # verifie si le pion peut manger à sa gauche
            if case_libre(pion.Pos_X + 1, pion.Pos_Y - 1, plateau):
                if case_color(pion.Pos_X + 1, pion.Pos_Y - 1, plateau):
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X + 1, pion.Pos_Y - 1)]
        # verifie si le pion peut avancer de 2 si il n'a pas encore bougé
        if pion.Pos_Y == 6 and case_libre(pion.Pos_X, pion.Pos_Y - 1, plateau) and case_libre(pion.Pos_X, pion.Pos_Y - 2, plateau):
            mvt_possible = mvt_possible + [(pion.Pos_X, pion.Pos_Y - 2)]
        # verifie si le pion peut avancer de 1
        if case_libre(pion.Pos_X, pion.Pos_Y - 1, plateau):
            mvt_possible = mvt_possible + [(pion.Pos_X, pion.Pos_Y - 1)]
    return mvt_possible


# nouvelle fonction de deplacement possible de la tour
def mvt_possible_tour(tour, plateau):
    mvt_possible = []
    finhaut = False  # variables qui determineront quand s'arrete la boucle for
    finbas = False
    fingauche = False
    findroite = False
    if tour.Pos_Y != 7:
        # on verifie les deplacements en haut et on s'arrete quand on bute sur une piece
        # et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, 8 - tour.Pos_Y):
            if finhaut == False:
                if case_libre(tour.Pos_X, tour.Pos_Y + i, plateau):
                    mvt_possible = mvt_possible + \
                        [(tour.Pos_X, tour.Pos_Y + i)]
                else:
                    finhaut = True
                    if case_color(tour.Pos_X, tour.Pos_Y + i, plateau) != tour.Color:
                        mvt_possible = mvt_possible + \
                            [(tour.Pos_X, tour.Pos_Y + i)]
    if tour.Pos_Y != 0:
        # on verifie les deplacements en bas et on s'arrete quand on bute sur une piece
        # et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, tour.Pos_Y + 1):
            if finbas == False:
                if case_libre(tour.Pos_X, tour.Pos_Y - i, plateau):
                    mvt_possible = mvt_possible + \
                        [(tour.Pos_X, tour.Pos_Y - i)]
                else:
                    finbas = True
                    if case_color(tour.Pos_X, tour.Pos_Y - i, plateau) != tour.Color:
                        mvt_possible = mvt_possible + \
                            [(tour.Pos_X, tour.Pos_Y - i)]
    if tour.Pos_X != 0:
        # on verifie les deplacements a gauche et on s'arrete quand on bute sur une piece
        # et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, tour.Pos_X + 1):
            if fingauche == False:
                if case_libre(tour.Pos_X - i, tour.Pos_Y, plateau):
                    mvt_possible = mvt_possible + \
                        [(tour.Pos_X - i, tour.Pos_Y)]
                else:
                    fingauche = True
                    if case_color(tour.Pos_X - i, tour.Pos_Y, plateau) != tour.Color:
                        mvt_possible = mvt_possible + \
                            [(tour.Pos_X - i, tour.Pos_Y)]
    if tour.Pos_X != 7:
        # on verifie les deplacements a droite et on s'arrete quand on bute sur une piece
        # et en ajoutant les coordonnées de celle-ci si on peut la manger
        for i in range(1, 8-tour.Pos_X):
            if findroite == False:
                if case_libre(tour.Pos_X + i, tour.Pos_Y, plateau):
                    mvt_possible = mvt_possible + \
                        [(tour.Pos_X + i, tour.Pos_Y)]
                else:
                    findroite = True
                    if case_color(tour.Pos_X + i, tour.Pos_Y, plateau) != tour.Color:
                        mvt_possible = mvt_possible + \
                            [(tour.Pos_X + i, tour.Pos_Y)]
    return mvt_possible


def mvt_possible_fou(fou, plateau):
    mvt_possible = []
    finhautgauche = False
    finbasgauche = False
    finhautdroite = False
    finbasdroite = False
    if fou.Pos_X != 0 and fou.Pos_Y != 7:
        for i in range(1, min(8 - fou.Pos_Y, 1 + fou.Pos_X)):
            if finhautgauche == False:
                if case_libre(fou.Pos_X - i, fou.Pos_Y + i, plateau):
                    mvt_possible = mvt_possible + \
                        [(fou.Pos_X - i, fou.Pos_Y + i)]
                else:
                    finhautgauche = True
                    if case_color(fou.Pos_X - i, fou.Pos_Y + i, plateau) != fou.Color:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X - i, fou.Pos_Y + i)]

    if fou.Pos_X != 0 and fou.Pos_Y != 0:
        for i in range(1, min(1 + fou.Pos_X, 1 + fou.Pos_Y)):
            if finbasgauche == False:
                if case_libre(fou.Pos_X - i, fou.Pos_Y - i, plateau):
                    mvt_possible = mvt_possible + \
                        [(fou.Pos_X - i, fou.Pos_Y - i)]
                else:
                    finbasgauche = True
                    if case_color(fou.Pos_X - i, fou.Pos_Y - i, plateau) != fou.Color:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X - i, fou.Pos_Y - i)]

    if fou.Pos_X != 7 and fou.Pos_Y != 7:
        for i in range(1, min(8-fou.Pos_X, 8-fou.Pos_Y)):
            if finhautdroite == False:
                if case_libre(fou.Pos_X + i, fou.Pos_Y + i, plateau):
                    mvt_possible = mvt_possible + \
                        [(fou.Pos_X + i, fou.Pos_Y + i)]
                else:
                    finhautdroite = True
                    if case_color(fou.Pos_X + i, fou.Pos_Y + i, plateau) != fou.Color:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X + i, fou.Pos_Y + i)]

    if fou.Pos_X != 7 and fou.Pos_Y != 0:
        for i in range(1, min(1 + fou.Pos_Y, 8 - fou.Pos_X)):
            if finbasdroite == False:
                if case_libre(fou.Pos_X + i, fou.Pos_Y - i, plateau):
                    mvt_possible = mvt_possible + \
                        [(fou.Pos_X + i, fou.Pos_X - i)]
                else:
                    finbasdroite = True
                    if case_color(fou.Pos_X + i, fou.Pos_Y - i, plateau) != 0:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X + i, fou.Pos_X - i)]
    return mvt_possible


def mvt_possible_dame(dame, plateau):
    mvt_possible = []

    mvt_possible = mvt_possible + mvt_possible_tour(dame, plateau)
    mvt_possible = mvt_possible + mvt_possible_fou(dame, plateau)

    return mvt_possible


def mvt_possible_cavalier(cavalier, plateau):
    mvt_possible = []
    if cavalier.Pos_X < 6:
        if cavalier.Pos_Y != 0:
            if case_libre(cavalier.Pos_X + 2, cavalier.Pos_Y - 1, plateau):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X + 2, cavalier.Pos_Y - 1)]
            else:
                if case_color(cavalier.Pos_X + 2, cavalier.Pos_Y - 1, plateau) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X + 2, cavalier.Pos_Y - 1)]
        if cavalier.Pos_Y != 7:
            if case_libre(cavalier.Pos_X + 2, cavalier.Pos_Y + 1, plateau):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X + 2, cavalier.Pos_Y + 1)]
            else:
                if case_color(cavalier.Pos_X + 2, cavalier.Pos_Y + 1, plateau) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X + 2, cavalier.Pos_Y + 1)]
    if cavalier.Pos_X > 1:
        if cavalier.Pos_Y != 0:
            if case_libre(cavalier.Pos_X - 2, cavalier.Pos_Y - 1, plateau):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X - 2, cavalier.Pos_Y - 1)]
            else:
                if case_color(cavalier.Pos_X - 2, cavalier.Pos_Y - 1, plateau) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X - 2, cavalier.Pos_Y - 1)]
        if cavalier.Pos_Y != 7:
            if case_libre(cavalier.Pos_X - 2, cavalier.Pos_Y + 1, plateau):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X - 2, cavalier.Pos_Y + 1)]
            else:
                if case_color(cavalier.Pos_X - 2, cavalier.Pos_Y + 1, plateau) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X - 2, cavalier.Pos_Y + 1)]
    if cavalier.Pos_Y < 6:
        if cavalier.Pos_X != 0:
            if case_libre(cavalier.Pos_X - 1, cavalier.Pos_Y + 2, plateau):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X - 1, cavalier.Pos_Y + 2)]
            else:
                if case_color(cavalier.Pos_X - 1, cavalier.Pos_Y + 2, plateau) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X - 1, cavalier.Pos_Y + 2)]
        if cavalier.Pos_X != 7:
            if case_libre(cavalier.Pos_X + 1, cavalier.Pos_Y + 2, plateau):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X + 1, cavalier.Pos_Y + 2)]
            else:
                if case_color(cavalier.Pos_X + 1, cavalier.Pos_Y + 2, plateau) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X + 1, cavalier.Pos_Y + 2)]
    if cavalier.Pos_Y > 1:
        if cavalier.Pos_X != 0:
            if case_libre(cavalier.Pos_X - 1, cavalier.Pos_Y - 2, plateau):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X - 1, cavalier.Pos_Y - 2)]
            else:
                if case_color(cavalier.Pos_X - 1, cavalier.Pos_Y - 2, plateau) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X - 1, cavalier.Pos_Y - 2)]
        if cavalier.Pos_X != 7:
            if case_libre(cavalier.Pos_X + 1, cavalier.Pos_Y - 2, plateau):
                mvt_possible = mvt_possible + \
                    [(cavalier.Pos_X + 1, cavalier.Pos_Y - 2)]
            else:
                if case_color(cavalier.Pos_X + 1, cavalier.Pos_Y - 2, plateau) != cavalier.Color:
                    mvt_possible = mvt_possible + \
                        [(cavalier.Pos_X + 1, cavalier.Pos_Y - 2)]
    return mvt_possible


def mvt_possible_gen(piece, plateau):
    if piece.name == 'cavalier':
        return mvt_possible_cavalier(piece, plateau)
    if piece.name == 'roi':
        return mvt_possible_roi(piece, plateau)
    if piece.name == 'dame':
        return mvt_possible_dame(piece, plateau)
    if piece.name == 'fou':
        return mvt_possible_fou(piece, plateau)
    if piece.name == 'tour':
        return mvt_possible_tour(piece, plateau)
    if piece.name == 'pion':
        return mvt_possible_pion(piece, plateau)


def roi_en_echec(roi, plateau):
    echec = False
    for piece in plateau.values():
        if piece != '' and (roi.Pos_X, roi.Pos_Y) in mvt_possible_gen(piece, plateau):
            echec = True
    return echec


def echec_si_mouvement_du_roi(roi, x, y, plateau):  # a revoir
    newplateau = copy.deepcopy(plateau)
    newplateau[(roi.Pos_X, roi.Pos_Y)] = ''
    newplateau[(x, y)] = roi
    echec_si_mvt = False
    for piece in newplateau.values():
        if piece != '' and piece != roi:
            if (x, y) in mvt_possible_gen(piece, plateau):
                echec_si_mvt = True
    return echec_si_mvt


def mvt_possible_roi(roi, plateau):
    mvt_possible = []
    if roi.Pos_X != 0:
        if case_libre(roi.Pos_X - 1, roi.Pos_Y, plateau) and not echec_si_mouvement_du_roi(roi, roi.Pos_X - 1, roi.Pos_Y, plateau):
            mvt_possible = mvt_possible + [(roi.Pos_X - 1, roi.Pos_Y)]
        else:
            if case_color(roi.Pos_X - 1, roi.Pos_Y, plateau) != roi.Color and not echec_si_mouvement_du_roi(roi, roi.Pos_X - 1, roi.Pos_Y, plateau):
                mvt_possible = mvt_possible + [(roi.Pos_X - 1, roi.Pos_Y)]
        if roi.Pos_Y != 0:
            if case_libre(roi.Pos_X - 1, roi.Pos_Y - 1, plateau) and not echec_si_mouvement_du_roi(roi, roi.Pos_X - 1, roi.Pos_Y - 1, plateau):
                mvt_possible = mvt_possible + [(roi.Pos_X - 1, roi.Pos_Y - 1)]
            else:
                if case_color(roi.Pos_X - 1, roi.Pos_Y - 1, plateau) != roi.Color and not echec_si_mouvement_du_roi(roi, roi.Pos_X - 1, roi.Pos_Y - 1, plateau):
                    mvt_possible = mvt_possible + \
                        [(roi.Pos_X - 1, roi.Pos_Y - 1)]
        if roi.Pos_Y != 7:
            if case_libre(roi.Pos_X - 1, roi.Pos_Y + 1, plateau) and not echec_si_mouvement_du_roi(roi, roi.Pos_X - 1, roi.Pos_Y + 1, plateau):
                mvt_possible = mvt_possible + [(roi.Pos_X - 1, roi.Pos_Y + 1)]
            else:
                if case_color(roi.Pos_X - 1, roi.Pos_Y + 1, plateau) != roi.Color and not echec_si_mouvement_du_roi(roi, roi.Pos_X - 1, roi.Pos_Y + 1, plateau):
                    mvt_possible = mvt_possible + \
                        [(roi.Pos_X - 1, roi.Pos_Y + 1)]
    if roi.Pos_X != 7:
        if case_libre(roi.Pos_X + 1, roi.Pos_Y, plateau) and not echec_si_mouvement_du_roi(roi, roi.Pos_X + 1, roi.Pos_Y, plateau):
            mvt_possible = mvt_possible + [(roi.Pos_X + 1, roi.Pos_Y)]
        else:
            if case_color(roi.Pos_X + 1, roi.Pos_Y, plateau) != roi.Color and not echec_si_mouvement_du_roi(roi, roi.Pos_X + 1, roi.Pos_Y, plateau):
                mvt_possible = mvt_possible + [(roi.Pos_X + 1, roi.Pos_Y)]
        if roi.Pos_Y != 0:
            if case_libre(roi.Pos_X + 1, roi.Pos_Y - 1, plateau) and not echec_si_mouvement_du_roi(roi, roi.Pos_X + 1, roi.Pos_Y - 1, plateau):
                mvt_possible = mvt_possible + [(roi.Pos_X + 1, roi.Pos_Y - 1)]
            else:
                if case_color(roi.Pos_X + 1, roi.Pos_Y - 1, plateau) != roi.Color and not echec_si_mouvement_du_roi(roi, roi.Pos_X - 1, roi.Pos_Y - 1, plateau):
                    mvt_possible = mvt_possible + \
                        [(roi.Pos_X + 1, roi.Pos_Y - 1)]
        if roi.Pos_Y != 7:
            if case_libre(roi.Pos_X + 1, roi.Pos_Y + 1, plateau) and not echec_si_mouvement_du_roi(roi, roi.Pos_X + 1, roi.Pos_Y + 1, plateau):
                mvt_possible = mvt_possible + [(roi.Pos_X + 1, roi.Pos_Y + 1)]
            else:
                if case_color(roi.Pos_X + 1, roi.Pos_Y + 1, plateau) != roi.Color and not echec_si_mouvement_du_roi(roi, roi.Pos_X + 1, roi.Pos_Y + 1, plateau):
                    mvt_possible = mvt_possible + \
                        [(roi.Pos_X + 1, roi.Pos_Y + 1)]
    if roi.Pos_Y != 0:
        if case_libre(roi.Pos_X, roi.Pos_Y - 1, plateau) and not echec_si_mouvement_du_roi(roi, roi.Pos_X, roi.Pos_Y - 1, plateau):
            mvt_possible = mvt_possible + [(roi.Pos_X, roi.Pos_Y - 1)]
        else:
            if case_color(roi.Pos_X, roi.Pos_Y - 1, plateau) != roi.Color and not echec_si_mouvement_du_roi(roi, roi.Pos_X, roi.Pos_Y - 1, plateau):
                mvt_possible = mvt_possible + [(roi.Pos_X, roi.Pos_Y - 1)]
    if roi.Pos_Y != 7:
        if case_libre(roi.Pos_X, roi.Pos_Y + 1, plateau) and not echec_si_mouvement_du_roi(roi, roi.Pos_X, roi.Pos_Y + 1, plateau):
            mvt_possible = mvt_possible + [(roi.Pos_X, roi.Pos_Y + 1)]
        else:
            if case_color(roi.Pos_X, roi.Pos_Y + 1, plateau) != roi.Color and not echec_si_mouvement_du_roi(roi, roi.Pos_X, roi.Pos_Y + 1, plateau):
                mvt_possible = mvt_possible + [(roi.Pos_X, roi.Pos_Y + 1)]
    return mvt_possible


def echec_si_mvt(piece, x, y, plateau):
    newplateau = copy.deepcopy(plateau)
    newplateau[(piece.Pos_X, piece.Pos_Y)] = ''
    newplateau[(x, y)] = piece

    for element in plateau:
        if plateau[element] != '' and plateau[element].name == 'roi' and plateau[element].Color == 'White':
            RoiBlanc = plateau[element]
        if plateau[element] != '' and plateau[element].name == 'roi' and plateau[element].Color == 'Black':
            RoiNoir = plateau[element]

    if piece.Color == 'White':
        echec_blanc = False
        for i in newplateau.values():
            if i != '':
                if (RoiBlanc.Pos_X, RoiBlanc.Pos_Y) in mvt_possible_gen(i, plateau):
                    echec_blanc = True
                    RoiBlanc.Checked = True
        return echec_blanc

    if piece.Color == 'Black':
        echec_noir = False
        for i in newplateau.values():
            if i != '':
                if (RoiNoir.Pos_X, RoiNoir.Pos_Y) in mvt_possible_gen(i, plateau):
                    echec_noir = True
                    RoiNoir.Checked = True
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


def mvt_final(piece, plateau):
    mvt = []
    if piece.name == 'roi':
        return mvt_possible_roi(piece, plateau)
    else:
        for (x, y) in mvt_possible_gen(piece, plateau):
            if echec_si_mvt(piece, x, y, plateau) == False:
                mvt = mvt + [(x, y)]
        return mvt


def petit_roque(roi, plateau):
    petit_roque_possible = False

    for element in plateau:
        if plateau[element] != '' and plateau[element].name == 'tour' and plateau[element].Color == 'White' and plateau[element].Pos_X == 7:
            TourBlanche2 = plateau[element]
        if plateau[element] != '' and plateau[element].name == 'tour' and plateau[element].Color == 'Black' and plateau[element].Pos_X == 0:
            TourNoire1 = plateau[element]

    if roi.Color == 'White':
        if not roi.Moved and not TourBlanche2.Moved:
            if case_libre(5, 0) and case_libre(6, 0):
                if not echec_si_mouvement_du_roi(roi, 5, 0) and not roi.Checked:
                    petit_roque_possible = True
    if roi.Color == 'Black':
        if not roi.Moved and not TourNoire1.Moved:
            if case_libre(2, 7) and case_libre(1, 7):
                if not echec_si_mouvement_du_roi(roi, 2, 7) and not roi.Checked:
                    petit_roque_possible = True
    return petit_roque_possible


def grand_roque(roi, plateau):
    for element in plateau:
        if plateau[element] != '' and plateau[element].name == 'tour' and plateau[element].Color == 'White' and plateau[element].Pos_X == 0:
            TourBlanche1 = plateau[element]
        if plateau[element] != '' and plateau[element].name == 'tour' and plateau[element].Color == 'Black' and plateau[element].Pos_X == 7:
            TourNoire2 = plateau[element]

    if roi.Color == 'White':
        grand_roque_possible = False
        if not roi.Moved and not TourBlanche1.Moved:
            if case_libre(1, 0) and case_libre(2, 0) and case_libre(3, 0):
                if not echec_si_mouvement_du_roi(roi, 2, 0) and not echec_si_mouvement_du_roi(roi, 3, 0) and not roi.Checked:
                    grand_roque_possible = True
    if roi.Color == 'Black':
        grand_roque_possible = False
        if not roi.Moved and not TourNoire2.Moved:
            if case_libre(4, 7) and case_libre(5, 7) and case_libre(6, 7):
                if not echec_si_mouvement_du_roi(roi, 4, 7) and not echec_si_mouvement_du_roi(roi, 3, 7) and not roi.Checked:
                    grand_roque_possible = True
    return grand_roque_possible
# a ajouter dans les fonctions de mouvements des pieces


# reste promotion pion
# reste roque


# reste nul en cas de match nul
# reste victoire


"""
ce serait bien de sauver l'historique des mvts
en plus ca permettrait de rejouer la partie a partir d'une certaine etape
"""
