from Jeu.Move import *
from Classes.Pieces import *


def egalite(plateau):
    """Définit s'il y a égalité

        Argument
        ---------
        plateau : dictionnaire

        Sortie
        ------
        booléen
        """

    for pièce in plateau.values():
        if pièce != '' and pièce.name == 'roi' and pièce.Color == 'White':
            RoiBlanc = pièce
        if pièce != '' and pièce.name == 'roi' and pièce.Color == 'Black':
            RoiNoir = pièce

    if mvt_final(RoiBlanc, plateau) == [] and not roi_en_echec(RoiBlanc, plateau):
        for pièce in plateau.values():
            if pièce != '' and pièce.Color == 'White' and mvt_final(pièce, plateau) != []:
                return False
        print("Pat")
        return True

    if mvt_final(RoiNoir, plateau) == [] and not roi_en_echec(RoiNoir, plateau):
        for pièce in plateau.values():
            if pièce != '' and pièce.Color == 'Black' and mvt_final(pièce, plateau) != []:
                return False
        print("Pat")
        return True

    return False


def echec_et_mat(plateau):
    """Définit s'il y a échec et mat

        Argument
        ---------
        plateau : dictionnaire

        Sortie
        ------
        booléen
        """

    mvt_possible_blanc = []
    mvt_possible_noir = []
    for element in plateau:
        if plateau[element] != '' and plateau[element].name == 'roi' and plateau[element].Color == 'White':
            RoiBlanc = plateau[element]
        if plateau[element] != '' and plateau[element].name == 'roi' and plateau[element].Color == 'Black':
            RoiNoir = plateau[element]

    if roi_en_echec(RoiBlanc, plateau) or roi_en_echec(RoiNoir, plateau):
        for piece in plateau.values():
            if piece != '':
                if piece.Color == 'White':
                    mvt_possible_blanc += mvt_final(piece, plateau)
                else:
                    mvt_possible_noir += mvt_final(piece, plateau)
        if mvt_final(RoiBlanc, plateau) == [] and roi_en_echec(RoiBlanc, plateau) and mvt_possible_blanc == []:
            return (True, "Echec et mat ! Victoire des noirs")
        if mvt_final(RoiNoir, plateau) == [] and roi_en_echec(RoiNoir, plateau) and mvt_possible_noir == []:
            return (True, "Echec et mat ! Victoire des blancs.")
        return (False, '')
    return (False, '')


Plateau = {(0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): '', (0, 7): '',
           (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): '', (1, 7): '',
           (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): '', (2, 7): '',
           (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): '', (3, 7): '',
           (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (4, 7): '',
           (5, 0): '', (5, 1): '', (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (5, 7): '',
           (6, 0): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): '', (6, 7): '',
           (7, 0): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (7, 7): ''}


def long_name(plateau):
    n = 0
    for piece in plateau:
        (x, y) = piece
        long = len(plateau_get_name(plateau, x, y))
        if n < long:
            n = long
    return n


def plateau_get_name(plateau, x, y):
    if plateau[(x, y)] == '':
        return ''
    return plateau[(x, y)].name


def plateau_get_couleur(plateau, x, y):
    if plateau[(x, y)] == '':
        return ''
    return plateau[(x, y)].Color


def grid_to_string(plateau):
    n = 8
    Max = long_name(plateau) + 6
    L = """"""
    for i in range(n):
        # Ligne déco 1
        for j in range(n):
            L += """ """
            for k in range(Max + 2):
                L += """="""
            L += """ """
        L += """
"""

        # Ligne nombres
        for j in range(n):
            L += """| """
            nom = plateau_get_name(plateau, j, 7-i)

            if nom != '':
                long = len(nom)
                vide = Max - 6 - long
                for k in range(vide // 2):
                    L += """ """

                L += nom
                L += """ """
                L += plateau_get_couleur(plateau, j, 7-i)

                for k in range(Max - 6 - vide // 2 - long):
                    L += """ """

            else:
                for k in range(Max):
                    L += """ """
            L += """ |"""
        L += """
"""

        # Ligne déco 2
        for j in range(n):
            L += """ """
            for k in range(Max + 2):
                L += """="""
            L += """ """
        if i != n-1:
            L += """
"""

    return L


def change(piece):
    if piece.name == 'pion':
        if (piece.Color == 'White' and piece.Pos_Y == 7) or (piece.Color == 'Black' and piece.Pos_Y == 0):
            choice = input("Veuillez entrer la pièce que vous voulez : ")
            if choice.lower() == 'dame':
                Changement = Dame('g', piece.Color, True,
                                  piece.Pos_X, piece.Pos_Y)

            elif choice.lower() == 'fou':
                Changement = Fou('g', piece.Color, True,
                                 piece.Pos_X, piece.Pos_Y)

            elif choice.lower() == 'tour':
                Changement = Tour('g', piece.Color, True,
                                  piece.Pos_X, piece.Pos_Y)

            elif choice.lower() in ['cavalier', 'cheval']:
                Changement = Cavalier('g', piece.Color, True,
                                      piece.Pos_X, piece.Pos_Y)
            else:
                print("Ce choix n'est pas supporté")
                return change(piece)
            return Changement
    return piece


if __name__ == "__main__":
    print(grid_to_string(Plateau))
