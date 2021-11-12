class Tour:
    
    def __init__(self,cote,color): #cote = d ou g, color = White ou Black
        if cote == 'g' :   
            self.Pos_X=0
        if cote == 'd' :
            self.Pos_X=7
        if color == 'White':
            self.Pos_Y=0
        if color == 'Black':
            self.Pos_Y=7
        self.Moved=False

    def petit_rock(self):
        if self.Moved==False : #and Condition roi pas mis en échec et pas de pièce sur le chemin
            self.Pos_X=5
    
    def grand_rock(self):
        if self.Moved==False : #and Condition roi pas mis en échec et pas de pièce sur le chemin
            self.Pos_X=3
    
    def move(self,valeur,direction): #longueur dans [|-7;7|], direction = horizontale ou verticale
        if direction=='horizontale' :#and pas de pièce en chemin
            self.Pos_X+=valeur
        elif direction=='verticale': #and pas de pièce en chemin
            self.Pos_Y+=valeur 
        self.Moved=True
    
class Dame:
   
    def __init__(self,color): #color = White ou Black
        if color == 'White':
            self.Pos_Y=0
        else:
            self.Pos_Y=7
        self.Pos_X=3
    
    def move_normal(self,valeur,direction): #longueur dans [|-7;7|], direction = horizontale ou verticale
        if direction=='horizontale' :#and pas de pièce en chemin
            self.Pos_X+=valeur
        elif direction=='verticale': #and pas de pièce en chemin
            self.Pos_Y+=valeur
    
    def move_diagonal(self,valeur,direction): #direction =h_d ou h_g ou b_d ou b_g
        if direction=='h_d': #and pas de pièce en chemin
            self.Pos_X+=valeur
            self.Pos_Y+=valeur
        
        elif direction=='h_g': #and pas de pièce en chemin
            self.Pos_X-=valeur
            self.Pos_Y+=valeur
        
        if direction=='b_d': #and pas de pièce en chemin
            self.Pos_X+=valeur
            self.Pos_Y-=valeur
        if direction=='b_g': #and pas de pièce en chemin
            self.Pos_X-=valeur
            self.Pos_Y-=valeur

        


    
        
    

