from Classes.Pieces import Pion, Tour
from Move import roi_en_echec,mvt_possible_roi,mvt_possible_gen
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






