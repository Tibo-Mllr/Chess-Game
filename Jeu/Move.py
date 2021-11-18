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
    """Renvoie la couleur de la pièce sur la case

        Arguments
        ---------
        x : abcisse de la case (entre 0 et 7)
        y : ordonnée de la case (entre 0 et 7)
        plateau : dictionnaire

        Sortie
        ------
        Chaîne de caractère ('White' ou 'Black')
        """
    if case_libre(x, y, plateau) == False:
        return plateau[(x, y)].Color


def case_libre(x, y, plateau):
    """Renvoie si une case est occupée par une pièce ou non

        Arguments
        ---------
        x : abcisse de la case (entre 0 et 7)
        y : ordonnée de la case (entre 0 et 7)
        plateau : dictionnaire

        Sortie
        ------
        booléen
        """
    if plateau[(x, y)] == '':
        return True
    else:
        return False


def mvt_possible_pion(pion, plateau):
    """Renvoie la liste de coups possible pour un pion donné

        Arguments
        ---------
        pion : Classe 
        plateau : dictionnaire

        Sortie
        ------
        liste
    """
    mvt_possible = []
    if pion.Color == 'White' and pion.Pos_Y != 7:  # Si le pion est blanc
        # verifie si il peut manger une piece en haut a gauche si le pion n'est pas tout a gauche
        if pion.Pos_X != 0:
            if case_libre(pion.Pos_X - 1, pion.Pos_Y + 1, plateau) == False:
                if case_color(pion.Pos_X - 1, pion.Pos_Y + 1, plateau) == 'Black':
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X - 1, pion.Pos_Y + 1)]
        # verifie si il peut manger une piece en haut a droite si le pion n'est pas tout a droite
        if pion.Pos_X != 7:
            if case_libre(pion.Pos_X + 1, pion.Pos_Y + 1, plateau) == False:
                if case_color(pion.Pos_X + 1, pion.Pos_Y + 1, plateau) == 'Black':
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X + 1, pion.Pos_Y + 1)]
        # verifie si le pion peut avancer de 2 si il n'a pas encore bougé
        if not pion.Moved and case_libre(pion.Pos_X, pion.Pos_Y+1, plateau) and case_libre(pion.Pos_X, pion.Pos_Y + 2, plateau):
            mvt_possible = mvt_possible + [(pion.Pos_X, pion.Pos_Y+2)]
        # verifie si le pion peut avancer de 1
        if case_libre(pion.Pos_X, pion.Pos_Y+1, plateau):
            mvt_possible = mvt_possible + [(pion.Pos_X, pion.Pos_Y+1)]
    if pion.Color == 'Black' and pion.Pos_Y != 0:  # si le pion est noir
        if pion.Pos_X != 0:  # verifie si le pion peut manger à sa droite
            if case_libre(pion.Pos_X - 1, pion.Pos_Y - 1, plateau) == False:
                if case_color(pion.Pos_X - 1, pion.Pos_Y - 1, plateau) == 'White':
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X - 1, pion.Pos_Y - 1)]
        if pion.Pos_X != 7:  # verifie si le pion peut manger à sa gauche
            if case_libre(pion.Pos_X + 1, pion.Pos_Y - 1, plateau) == False:
                if case_color(pion.Pos_X + 1, pion.Pos_Y - 1, plateau) == 'White':
                    mvt_possible = mvt_possible + \
                        [(pion.Pos_X + 1, pion.Pos_Y - 1)]
        # verifie si le pion peut avancer de 2 si il n'a pas encore bougé
        if not pion.Moved and case_libre(pion.Pos_X, pion.Pos_Y - 1, plateau) and case_libre(pion.Pos_X, pion.Pos_Y - 2, plateau):
            mvt_possible = mvt_possible + [(pion.Pos_X, pion.Pos_Y - 2)]
        # verifie si le pion peut avancer de 1
        if case_libre(pion.Pos_X, pion.Pos_Y - 1, plateau):
            mvt_possible = mvt_possible + [(pion.Pos_X, pion.Pos_Y - 1)]
    return mvt_possible


# nouvelle fonction de deplacement possible de la tour
def mvt_possible_tour(tour, plateau):
    """Renvoie la liste de coups possible pour une tour donnée

        Arguments
        ---------
        tour : Classe 
        plateau : dictionnaire

        Sortie
        ------
        liste
    """
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
    """Renvoie la liste de coups possible pour un fou donné

        Arguments
        ---------
        fou : Classe 
        plateau : dictionnaire

        Sortie
        ------
        liste
    """
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
                        [(fou.Pos_X + i, fou.Pos_Y - i)]
                else:
                    finbasdroite = True
                    if case_color(fou.Pos_X + i, fou.Pos_Y - i, plateau) != fou.Color:
                        mvt_possible = mvt_possible + \
                            [(fou.Pos_X + i, fou.Pos_Y - i)]
    return mvt_possible


def mvt_possible_dame(dame, plateau):
    """Renvoie la liste de coups possible pour une dame donnée

        Arguments
        ---------
        dame : Classe 
        plateau : dictionnaire

        Sortie
        ------
        liste
    """
    mvt_possible = []

    mvt_possible = mvt_possible + mvt_possible_tour(dame, plateau)
    mvt_possible = mvt_possible + mvt_possible_fou(dame, plateau)

    return mvt_possible


def mvt_possible_cavalier(cavalier, plateau):
    """Renvoie la liste de coups possible pour un cavalier donné

        Arguments
        ---------
        cavalier : Classe 
        plateau : dictionnaire

        Sortie
        ------
        liste
    """
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
    """Renvoie la liste de coups possible pour une pièce donnée

        Arguments
        ---------
        piece : Classe 
        plateau : dictionnaire

        Sortie
        ------
        liste
    """
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
    """Renvoie si un roi donné est en echec ou non 

        Arguments
        ---------
        roi : Classe 
        plateau : dictionnaire

        Sortie
        ------
        booléen
    """
    echec = False
    for piece in plateau.values():
        if piece != '' and piece.Color != roi.Color and (roi.Pos_X, roi.Pos_Y) in mvt_possible_gen(piece, plateau):
            echec = True
            roi.Checked = True
    return echec


def echec_si_mouvement_du_roi(roi, x, y, plateau):
    """Renvoie si le roi peut se déplacer sur une case sans se mettre en échec

        Arguments
        ---------
        roi : Classe 
        x : abcisse de la case de destination (entre 0 et 7)
        y : ordonnée de la case de destination (entre 0 et 7)
        plateau : dictionnaire

        Sortie
        ------
        booléen
    """
    newplateau = copy.deepcopy(plateau)
    newplateau[(roi.Pos_X, roi.Pos_Y)] = ''
    newplateau[(x, y)] = roi
    echec_si_mvt = False
    for piece in newplateau.values():
        if piece != '' and piece != roi and piece.Color != roi.Color:
            if (x, y) in mvt_possible_gen(piece, newplateau):
                echec_si_mvt = True
    return echec_si_mvt


def mvt_possible_roi(roi, plateau):
    """Renvoie la liste de coups possible pour un roi donné

        Arguments
        ---------
        roi : Classe 
        plateau : dictionnaire

        Sortie
        ------
        liste
    """
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
    """Renvoie si une pièce met en échec le roi adverse
    
        Arguments
        ---------
        piece : Classe 
        x : abcisse de la case de destination (entre 0 et 7)
        y : ordonnée de la case de destination (entre 0 et 7)
        plateau : dictionnaire

        Sortie
        ------
        booléen
    """
    newplateau = copy.deepcopy(plateau)
    newplateau[(piece.Pos_X, piece.Pos_Y)] = ''
    newplateau[(x, y)] = piece

    for element in newplateau:
        if newplateau[element] != '' and newplateau[element].name == 'roi' and newplateau[element].Color == 'White':
            RoiBlanc = newplateau[element]
        if newplateau[element] != '' and newplateau[element].name == 'roi' and newplateau[element].Color == 'Black':
            RoiNoir = newplateau[element]

    if piece.Color == 'White':
        echec_blanc = False
        for i in newplateau.values():
            if i != '' and i.Color == 'Black':
                if (RoiBlanc.Pos_X, RoiBlanc.Pos_Y) in mvt_possible_gen(i, newplateau):
                    echec_blanc = True
        return echec_blanc

    if piece.Color == 'Black':
        echec_noir = False
        for i in newplateau.values():
            if i != '' and i.Color == 'White':
                if (RoiNoir.Pos_X, RoiNoir.Pos_Y) in mvt_possible_gen(i, newplateau):
                    echec_noir = True
        return echec_noir


def mvt_final(piece, plateau):
    """Liste les mouvements faisables par une pièce (sans mettre son propre roi en échec)

        Arguments
        ---------
        piece : classe
        plateau : dictionnaire

        Sortie
        ------
        liste
        """
    mvt = []
    if piece.name == 'roi':
        if piece.Color == 'White' and petit_roque(piece, plateau):
            mvt = mvt + [(6, 0)]
        if piece.Color == 'White' and grand_roque(piece, plateau):
            print("Etape5")
            mvt = mvt + [(2, 0)]
        if piece.Color == 'Black' and petit_roque(piece, plateau):
            mvt = mvt + [(6, 7)]
        if piece.Color == 'Black' and grand_roque(piece, plateau):
<<<<<<< HEAD
            mvt = mvt + [(2,7)]
        return mvt + mvt_possible_roi(piece,plateau)
=======
            mvt = mvt + [(2, 7)]
        return mvt + mvt_possible_roi(piece, plateau)
>>>>>>> 1f8409163da4ade86fcec37e576ae9712d078e72
    else:
        mvt = mvt_possible_gen(piece, plateau)
        for (x, y) in mvt:
            if echec_si_mvt(piece, x, y, plateau) == False:
                mvt = mvt + [(x, y)]
        return mvt


def petit_roque(roi, plateau):
    """Renvoie si le petit roque est possible

        Arguments
        ---------
        roi : classe
        plateau : dictionnaire

        Sortie
        ------
        booléen
    """
    petit_roque_possible = False
    if roi.Color == 'White' and roi.Moved == False and case_libre(5, 0, plateau) and case_libre(6, 0, plateau) and not roi_en_echec(roi, plateau):
        if not case_libre(7, 0, plateau):
            if plateau[(7, 0)].name == 'tour' and plateau[(7, 0)].Moved == False:
                if not echec_si_mouvement_du_roi(roi, 5, 0, plateau) and not echec_si_mouvement_du_roi(roi, 6, 0, plateau):
                    petit_roque_possible == True
    if roi.Color == 'Black' and roi.Moved == False and case_libre(5, 7, plateau) and case_libre(6, 7, plateau) and not roi_en_echec(roi, plateau):
        if not case_libre(7, 0, plateau):
            if plateau[(7, 7)].name == 'tour' and plateau[(7, 7)].Moved == False:
                if not echec_si_mouvement_du_roi(roi, 5, 7, plateau) and not echec_si_mouvement_du_roi(roi, 6, 7, plateau):
                    petit_roque_possible == True
    return petit_roque_possible


def grand_roque(roi, plateau):
    grand_roque_possible = False
    if roi.Color == 'White' and roi.Moved == False and case_libre(3, 0, plateau) and case_libre(2, 0, plateau) and case_libre(1, 0, plateau) and not roi_en_echec(roi, plateau):
        print("Etape1")
        if not case_libre(0, 0, plateau):
            print("Etape2")
            if plateau[(0, 0)].name == 'tour' and plateau[(0, 0)].Moved == False:
                print("Etape3")
                if not echec_si_mouvement_du_roi(roi, 3, 0, plateau) and not echec_si_mouvement_du_roi(roi, 2, 0, plateau):
                    print("Etape4")
                    grand_roque_possible == True
    if roi.Color == 'Black' and roi.Moved == False and case_libre(3, 7, plateau) and case_libre(2, 7, plateau) and case_libre(1, 7, plateau) and not roi_en_echec(roi, plateau):
        if not case_libre(7, 0, plateau):
            if plateau[(7, 7)].name == 'tour' and plateau[(7, 7)].Moved == False:
                if not echec_si_mouvement_du_roi(roi, 3, 7, plateau) and not echec_si_mouvement_du_roi(roi, 2, 7, plateau):
                    grand_roque_possible == True
    return grand_roque_possible


def roque(piece, x, plateau):
    if piece.name == 'roi':
        if (piece.Color == 'White' and x-piece.Pos_X in [2, -2]) or (piece.Color == 'Black' and x-piece.Pos_X in [2, -2]):
            if x-piece.Pos_X == 2 and petit_roque(piece, plateau):
                Tour = plateau[(7, piece.Pos_Y)]
                Tour.move(5, piece.Pos_Y)
                piece.move(6, piece.Pos_Y)
                plateau[(5, piece.Pos_Y)], plateau[(7, piece.Pos_Y)], plateau[(
                    6, piece.Pos_Y)], plateau[(5, piece.Pos_Y)] = '', '', piece, Tour

            if x-piece.Pos_X == -2 and grand_roque(piece, plateau):
                Tour = plateau[(0, piece.Pos_Y)]
                Tour.move(3, piece.Pos_Y)
                piece.move(2, piece.Pos_Y)
                plateau[(5, piece.Pos_Y)], plateau[(0, piece.Pos_Y)], plateau[(
                    2, piece.Pos_Y)], plateau[(3, piece.Pos_Y)] = '', '', piece, Tour


# a ajouter dans les fonctions de mouvements des pieces


# reste promotion pion
# reste roque


# reste nul en cas de match nul
# reste victoire

"""
ce serait bien de sauver l'historique des mvts
en plus ca permettrait de rejouer la partie a partir d'une certaine etape
"""


# roi peut pasmanger la piece qui le met en echec
