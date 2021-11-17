from Tests.tests_classes import *
from Tests.tests_mouvements import *

if __name__ == "__main__":
    # Test des pièces
    test_Pion()
    test_Roi()
    test_Tour()
    test_Fou()
    test_Dame()
    test_Cavalier()

    # Test des mouvements
    test_mvt_Pion()
    test_mvt_Roi()
    test_mvt_Tour()
    test_mvt_Fou()
    test_mvt_Dame()
    test_mvt_Cavalier()
