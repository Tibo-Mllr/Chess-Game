from Classes.Pieces import *
from Jeu.Move import *

plateau = {(0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '', (0, 5): '', (0, 6): '', (0, 7): '',
           (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '', (1, 5): '', (1, 6): '', (1, 7): '',
           (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '', (2, 5): '', (2, 6): '', (2, 7): '',
           (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '', (3, 5): '', (3, 6): '', (3, 7): '',
           (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '', (4, 5): '', (4, 6): '', (4, 7): '',
           (5, 0): '', (5, 1): '', (5, 2): '', (5, 3): '', (5, 4): '', (5, 5): '', (5, 6): '', (5, 7): '',
           (6, 0): '', (6, 1): '', (6, 2): '', (6, 3): '', (6, 4): '', (6, 5): '', (6, 6): '', (6, 7): '',
           (7, 0): '', (7, 1): '', (7, 2): '', (7, 3): '', (7, 4): '', (7, 5): '', (7, 6): '', (7, 7): ''}


def test_mvt_Pion():
    Pion1 = Pion(1, 'White')
    plateau[(Pion1.Pos_X, Pion1.Pos_Y)] = Pion1
    assert len(mvt_possible_pion(Pion1, plateau)) == 2
    assert mvt_possible_pion(Pion1, plateau) == [(
        1, 2), (1, 3)] or mvt_possible_pion(Pion1, plateau) == [(1, 3), (1, 2)]


def test_mvt_Roi():
    Roi1 = Roi('White')
    plateau[(Roi1.Pos_X, Roi1.Pos_Y)] = Roi1
    """
    print(mvt_possible_roi(Roi1, plateau))
    assert len(mvt_possible_pion(Roi1, plateau)) == 5
    for i in range(5):
        assert mvt_possible_roi(Roi1, plateau)[i] in [
            (3, 0), (5, 0), (3, 1), (4, 1), (5, 1)]"""


def test_mvt_Tour():
    Tour1 = Tour('g', 'White')
    plateau[(Tour1.Pos_X, Tour1.Pos_Y)] = Tour1
    assert len(mvt_possible_tour(Tour1, plateau)) == 10
    for i in range(10):
        assert mvt_possible_tour(Tour1, plateau)[i] in [(
            0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0)]


def test_mvt_Fou():
    Fou1 = Fou('g', 'White')
    plateau[(Fou1.Pos_X, Fou1.Pos_Y)] = Fou1
    assert len(mvt_possible_fou(Fou1, plateau)) == 5
    for i in range(5):
        assert mvt_possible_fou(Fou1, plateau)[i] in [
            (3, 1), (4, 2), (5, 3), (6, 4), (7, 5)]


def test_mvt_Dame():
    Dame1 = Dame('g', 'White')
    plateau[(Dame1.Pos_X, Dame1.Pos_Y)] = Dame1
    assert len(mvt_possible_dame(Dame1, plateau)) == 14
    for i in range(14):
        assert mvt_possible_dame(Dame1, plateau)[i] in [(3, 1), (3, 2), (3, 3), (3, 4), (
            3, 5), (3, 6), (3, 7), (2, 1), (1, 2), (0, 3), (4, 1), (5, 2), (6, 3), (7, 4)]


def test_mvt_Cavalier():
    Cavalier1 = Cavalier('g', 'White')
    plateau[(Cavalier1.Pos_X, Cavalier1.Pos_Y)] = Cavalier1
    assert len(mvt_possible_cavalier(Cavalier1, plateau)) == 3
    for i in range(3):
        assert mvt_possible_cavalier(Cavalier1, plateau)[i] in [
            (3, 1), (0, 2), (2, 2)]
