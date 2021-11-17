from Jeu.Chess import *

Plateau = {(0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): '', (0, 7): '',
           (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): '', (1, 7): '',
           (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): '', (2, 7): '',
           (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): '', (3, 7): '',
           (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (4, 7): '',
           (5, 0): '', (5, 1): '', (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (5, 7): '',
           (6, 0): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): '', (6, 7): '',
           (7, 0): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (7, 7): ''}


def jeu_init():
    # Pions blancs
    PionBlanc0 = Pion(0, 'White')
    Plateau[PionBlanc0.Pos_X, PionBlanc0.Pos_Y] = PionBlanc0

    PionBlanc1 = Pion(1, 'White')
    Plateau[PionBlanc1.Pos_X, PionBlanc1.Pos_Y] = PionBlanc1

    PionBlanc2 = Pion(2, 'White')
    Plateau[PionBlanc2.Pos_X, PionBlanc2.Pos_Y] = PionBlanc2

    PionBlanc3 = Pion(3, 'White')
    Plateau[PionBlanc3.Pos_X, PionBlanc3.Pos_Y] = PionBlanc3

    PionBlanc4 = Pion(4, 'White')
    Plateau[PionBlanc4.Pos_X, PionBlanc4.Pos_Y] = PionBlanc4

    PionBlanc5 = Pion(5, 'White')
    Plateau[PionBlanc5.Pos_X, PionBlanc5.Pos_Y] = PionBlanc5

    PionBlanc6 = Pion(6, 'White')
    Plateau[PionBlanc6.Pos_X, PionBlanc6.Pos_Y] = PionBlanc6

    PionBlanc7 = Pion(7, 'White')
    Plateau[PionBlanc7.Pos_X, PionBlanc7.Pos_Y] = PionBlanc7

    # Roi Blanc
    RoiBlanc = Roi('White')
    Plateau[RoiBlanc.Pos_X, RoiBlanc.Pos_Y] = RoiBlanc

    # Tours Blanches
    TourBlanche1 = Tour('g', 'White')
    Plateau[TourBlanche1.Pos_X, TourBlanche1.Pos_Y] = TourBlanche1

    TourBlanche2 = Tour('d', 'White')
    Plateau[TourBlanche2.Pos_X, TourBlanche2.Pos_Y] = TourBlanche2

    # Fous blancs
    FouBlanc1 = Fou('g', 'White')
    Plateau[FouBlanc1.Pos_X, FouBlanc1.Pos_Y] = FouBlanc1

    FouBlanc2 = Fou('d', 'White')
    Plateau[FouBlanc2.Pos_X, FouBlanc2.Pos_Y] = FouBlanc2

    # Dame Blanche
    DameBlanche = Dame('g', 'White')
    Plateau[DameBlanche.Pos_X, DameBlanche.Pos_Y] = DameBlanche

    # Cavaliers Blancs
    CavalierBlanc1 = Cavalier('g', 'White')
    Plateau[CavalierBlanc1.Pos_X, CavalierBlanc1.Pos_Y] = CavalierBlanc1

    CavalierBlanc2 = Cavalier('d', 'White')
    Plateau[CavalierBlanc2.Pos_X, CavalierBlanc2.Pos_Y] = CavalierBlanc2

    # Pions noirs
    PionNoir0 = Pion(0, 'Black')
    Plateau[PionNoir0.Pos_X, PionNoir0.Pos_Y] = PionNoir0

    PionNoir1 = Pion(1, 'Black')
    Plateau[PionNoir1.Pos_X, PionNoir1.Pos_Y] = PionNoir1

    PionNoir2 = Pion(2, 'Black')
    Plateau[PionNoir2.Pos_X, PionNoir2.Pos_Y] = PionNoir2

    PionNoir3 = Pion(3, 'Black')
    Plateau[PionNoir3.Pos_X, PionNoir3.Pos_Y] = PionNoir3

    PionNoir4 = Pion(4, 'Black')
    Plateau[PionNoir4.Pos_X, PionNoir4.Pos_Y] = PionNoir4

    PionNoir5 = Pion(5, 'Black')
    Plateau[PionNoir5.Pos_X, PionNoir5.Pos_Y] = PionNoir5

    PionNoir6 = Pion(6, 'Black')
    Plateau[PionNoir6.Pos_X, PionNoir6.Pos_Y] = PionNoir6

    PionNoir7 = Pion(7, 'Black')
    Plateau[PionNoir7.Pos_X, PionNoir7.Pos_Y] = PionNoir7

    # Roi Noir
    RoiNoir = Roi('Black')
    Plateau[RoiNoir.Pos_X, RoiNoir.Pos_Y] = RoiNoir

    # Tours Noires
    TourNoire1 = Tour('g', 'Black')
    Plateau[TourNoire1.Pos_X, TourNoire1.Pos_Y] = TourNoire1

    TourNoire2 = Tour('d', 'Black')
    Plateau[TourNoire2.Pos_X, TourNoire2.Pos_Y] = TourNoire2

    # Fous Noirs
    FouNoir1 = Fou('g', 'Black')
    Plateau[FouNoir1.Pos_X, FouNoir1.Pos_Y] = FouNoir1

    FouNoir2 = Fou('d', 'Black')
    Plateau[FouNoir2.Pos_X, FouNoir2.Pos_Y] = FouNoir2

    # Dame Noire
    DameNoire = Dame('g', 'Black')
    Plateau[DameNoire.Pos_X, DameNoire.Pos_Y] = DameNoire

    # Cavaliers Noirs
    CavalierNoir1 = Cavalier('g', 'Black')
    Plateau[CavalierNoir1.Pos_X, CavalierNoir1.Pos_Y] = CavalierNoir1

    CavalierNoir2 = Cavalier('d', 'Black')
    Plateau[CavalierNoir2.Pos_X, CavalierNoir2.Pos_Y] = CavalierNoir2


def jeu():
    Fin = False
    print(grid_to_string(Plateau))

    while not Fin:
        x = input("Entrez l'abscisse de la pièce que vous voulez déplacer : ")
        y = input("Entrez l'ordonnée de la pièce que vous voulez déplacer : ")
        Dep = input("Décrivez le déplacement voulu : ")
        L = input("Entrez la longueur du déplacement : ")

        X = int(x)
        Y = int(y)

        Plateau[(X, Y)].move(int(L), Dep)
        Plateau[Plateau[(X, Y)].Pos_X, Plateau[(X, Y)].Pos_Y] = Plateau[(X, Y)]
        Plateau[(X, Y)] = ''
        print(grid_to_string(Plateau))


if __name__ == "__main__":
    jeu_init()
    jeu()
