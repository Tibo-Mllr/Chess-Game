from Move import *
from Classes.Pieces import *
from Interface.Graphique import *


def egalite(roi,plateau):
    if mvt_possible_roi(roi,plateau)==[] and not roi_en_echec(roi,plateau):
        mvt_possible_autres_pièces=[]
        for i in [Pion,Tour,Fou,Dame,Cavalier]:
            mvt_possible_autres_pièces+=mvt_possible_gen(i,plateau)
        if mvt_possible_autres_pièces==[]:
            print  ("it's a draw")


def victoire(roi,plateau):
    if mvt_possible_roi(roi,plateau)==[] and roi_en_echec(roi,plateau):
        couleur_gagnant=["White","Black"]
        couleur_gagnant.remove(roi.Color)
        print(couleur_gagnant[0] + "Win !")







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


if __name__ == "__main__":
    print(grid_to_string(Plateau))
