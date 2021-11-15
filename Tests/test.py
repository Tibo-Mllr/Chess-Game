from ..Classes.Pieces import *


def test_Pion():
    Pion1 = Pion(0, 'White')
    Pion1.move(2)
    assert Pion1.Pos_Y == 3

    Pion1.move(2)
    assert Pion1.Pos_Y == 4


if __name__ == '__main__':
    test_Pion()
