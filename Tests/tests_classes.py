from Classes.Pieces import *


def test_Pion():
    Pion1 = Pion(0, 'White')
    Pion1.move(0, 3)
    assert Pion1.Pos_Y == 3

    Pion1.move(0, 4)
    assert Pion1.Pos_Y == 4

    Dame2 = Dame('g', 'White', True, Pion1.Pos_X, Pion1.Pos_Y)
    Dame2.move(2, 6)
    assert (Dame2.Pos_X, Dame2.Pos_Y) == (2, 6)


def test_Roi():
    Roi1 = Roi('White')
    Roi1.roque('d')
    assert (Roi1.Pos_X, Roi1.Pos_Y) == (6, 0)

    Roi1.move(6, 1)
    assert (Roi1.Pos_X, Roi1.Pos_Y) == (6, 1)

    Roi1.move(5, 1)
    assert (Roi1.Pos_X, Roi1.Pos_Y) == (5, 1)

    Roi1.move(6, 2)
    assert (Roi1.Pos_X, Roi1.Pos_Y) == (6, 2)

    Roi1.roque('g')
    assert (Roi1.Pos_X, Roi1.Pos_Y) == (6, 2)


def test_Tour():
    Tour1 = Tour('g', 'White')
    Tour1.grand_roque()
    assert(Tour1.Pos_X, Tour1.Pos_Y) == (3, 0)

    Tour1.move(7, 0)
    assert (Tour1.Pos_X, Tour1.Pos_Y) == (7, 0)

    Tour1.move(7, 5)
    assert (Tour1.Pos_X, Tour1.Pos_Y) == (7, 5)

    Tour1.move(7, 2)
    assert (Tour1.Pos_X, Tour1.Pos_Y) == (7, 2)

    Tour1.petit_roque()
    assert (Tour1.Pos_X, Tour1.Pos_Y) == (7, 2)


def test_Dame():
    Dame1 = Dame('g', 'White')
    Dame1.move(3, 4)
    assert (Dame1.Pos_X, Dame1.Pos_Y) == (3, 4)

    Dame1.move(0, 1)
    assert (Dame1.Pos_X, Dame1.Pos_Y) == (0, 1)


def test_Fou():
    Fou1 = Fou('g', 'White')
    Fou1.move(7, 5)
    assert (Fou1.Pos_X, Fou1.Pos_Y) == (7, 5)

    Fou1.move(6, 6)
    assert (Fou1.Pos_X, Fou1.Pos_Y) == (6, 6)


def test_Cavalier():
    Cavalier1 = Cavalier('g', 'White')
    Cavalier1.move(2, 2)
    assert (Cavalier1.Pos_X, Cavalier1.Pos_Y) == (2, 2)

    Cavalier1.move(1, 0)
    assert (Cavalier1.Pos_X, Cavalier1.Pos_Y) == (1, 0)
