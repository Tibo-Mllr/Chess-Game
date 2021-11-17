from Tests.tests_classes import *
from Tests.tests_mouvements import *

if __name__ == "__main__":
    # Test des pièces
    test_Pion()
    test_Roi()
    test_Tour()
    test_Dame()
    test_Fou()
    test_Cavalier()

    # Test des mouvements
    test_mvt_pion()
