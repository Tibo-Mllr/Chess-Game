class Pion:
    def __init__(self, X, color):  # Initialisation du pion
        self.Pos_X = X

        if color == 'White':
            self.Pos_Y = 1
        if color == 'Black':
            self.Pos_Y = 6

        self.Color = color
        self.Moved = False
        self.name = 'pion'

    def move(self, c):
        # Peut bouger de 2 SI ET SEULEMENT SI il n'a pas bougé
        if not self.Moved:
            if self.Color == 'White':
                self.Pos_Y += min(c, 2)
            else:
                self.Pos_Y -= min(c, 2)

            self.Moved = True

        else:
            if self.Color == 'White':
                self.Pos_Y += 1
            else:
                self.Pos_Y -= 1

    # Mouvement spécial pour manger
    def eat(self, d):
        self.move(1)
        if d == 'R':
            self.Pos_X += 1
        else:
            self.Pos_X -= 1

    # Changement en une autre pièce une fois arrivé au bout
    def change(self, choice):
        if self.Y_Pos in [7, 0]:
            # ATTENTION : Concordance à vérifier
            self = choice(self.Color, 'g', True, self.Pos_X, self.Pos_Y)


class Roi:
    # Initialisation du Roi
    def __init__(self, color):
        self.Pos_X = 4

        if color == 'White':
            self.Pos_Y = 0
        if color == 'Black':
            self.Pos_Y = 7

        self.Moved = False
        self.Checked = False
        self.Color = color
        self.name = 'roi'

    def move(self, d):

        # Mouvements normaux
        if d[0] == 'd':
            self.Pos_X -= 1

        elif d[0] == 'g':
            self.Pos_X += 1

        elif d[0] == 'h':
            self.Pos_Y += 1

        else:
            self.Pos_Y -= 1

        # Puis mouvements diagonaux
        # Par convention si deux mouvements : 'g' ou 'd' PUIS '_' PUIS 'h' ou 'b'
        if len(d) == 3:
            if d[2] == 'h':
                self.Pos_Y += 1
            else:
                self.Pos_Y -= 1

        self.Moved = True

    def rock(self, d):
        if not self.Checked and not self.Moved:
            if d == 'd':
                self.Pos_X += 2
            else:
                self.Pos_X -= 2


class Tour:

    # cote = d ou g, color = White ou Black
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        if not Change:
            if cote == 'g':
                self.Pos_X = 0
            if cote == 'd':
                self.Pos_X = 7
            if color == 'White':
                self.Pos_Y = 0
            if color == 'Black':
                self.Pos_Y = 7
        if Change:  # Au cas où ce soit une transformation de pion
            self.Pos_X = X
            self.Pos_Y = Y
            self.Color = color
        self.Color = color
        self.Moved = False
        self.name = 'tour'

    def petit_rock(self):
        if self.Moved == False:  # and Condition roi pas mis en échec et pas de pièce sur le chemin
            self.Pos_X = 5
            self.Moved = True

    def grand_rock(self):
        if self.Moved == False:  # and Condition roi pas mis en échec et pas de pièce sur le chemin
            self.Pos_X = 3
            self.Moved = True

    # longueur dans [|-7;7|], direction = horizontale ou verticale
    def move(self, valeur, direction):
        if direction == 'horizontale':  # and pas de pièce en chemin
            self.Pos_X += valeur
        elif direction == 'verticale':  # and pas de pièce en chemin
            self.Pos_Y += valeur
        self.Moved = True


class Dame:

    # color = White ou Black et on met l'argument cote pour homogénéiser entre les différentes fonctions
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        if not Change:
            if color == 'White':
                self.Pos_Y = 0
            else:
                self.Pos_Y = 7
            self.Pos_X = 3
        if Change:  # Au cas où ce soit une transformation de pion
            self.Pos_X = X
            self.Pos_Y = Y
        self.Color = color
        self.name = 'dame'

    # longueur dans [|-7;7|], direction = horizontale ou verticale
    def move_normal(self, valeur, direction):
        if direction == 'horizontale':  # and pas de pièce en chemin
            self.Pos_X += valeur
        elif direction == 'verticale':  # and pas de pièce en chemin
            self.Pos_Y += valeur

    def move_diagonal(self, valeur, direction):  # direction =h_d ou h_g ou b_d ou b_g
        if direction == 'h_d':  # and pas de pièce en chemin
            self.Pos_X += valeur
            self.Pos_Y += valeur

        elif direction == 'h_g':  # and pas de pièce en chemin
            self.Pos_X -= valeur
            self.Pos_Y += valeur

        elif direction == 'b_d':  # and pas de pièce en chemin
            self.Pos_X += valeur
            self.Pos_Y -= valeur
        elif direction == 'b_g':  # and pas de pièce en chemin
            self.Pos_X -= valeur
            self.Pos_Y -= valeur


class Fou:

    # cote = d ou g, color = White ou Black
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        if not Change:
            if cote == 'g':
                self.Pos_X = 2
            if cote == 'd':
                self.Pos_X = 5
            if color == 'White':
                self.Pos_Y = 0
            if color == 'Black':
                self.Pos_Y = 7
        if Change:  # Au cas où ce soit une transformation de pion
            self.Pos_X = X
            self.Pos_Y = Y
        self.Color = color
        self.name = 'fou'

    def move(self, valeur, direction):  # direction =h_d ou h_g ou b_d ou b_g
        if direction == 'h_d':  # and pas de pièce en chemin
            self.Pos_X += valeur
            self.Pos_Y += valeur

        elif direction == 'h_g':  # and pas de pièce en chemin
            self.Pos_X -= valeur
            self.Pos_Y += valeur

        elif direction == 'b_d':  # and pas de pièce en chemin
            self.Pos_X += valeur
            self.Pos_Y -= valeur
        elif direction == 'b_g':  # and pas de pièce en chemin
            self.Pos_X -= valeur
            self.Pos_Y -= valeur


class Cavalier:

    # cote = d ou g, color = White ou Black
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        if not Change:
            if cote == 'g':
                self.Pos_X = 1
            if cote == 'd':
                self.Pos_X = 6
            if color == 'White':
                self.Pos_Y = 0
            if color == 'Black':
                self.Pos_Y = 7
        if Change:  # Au cas où ce soit une transformation de pion
            self.Pos_X = X
            self.Pos_Y = Y
        self.Color = color
        self.name = 'cavalier'

    # direction =h_d_d ou h_g_g ou h_h_g ou h_h_d ou b_d_d ou b_g_g ou b_b_g ou b_b_d
    def move(self, valeur, direction):

        if direction == 'h_d_d':
            self.Pos_X += 2
            self.Pos_Y += 1
        elif direction == 'h_g_g':
            self.Pos_X -= 2
            self.Pos_Y += 1
        elif direction == 'h_h_g':
            self.Pos_X -= 1
            self.Pos_Y += 2
        elif direction == 'h_h_d':
            self.Pos_X += 1
            self.Pos_Y += 2
        elif direction == 'b_d_d':
            self.Pos_X += 2
            self.Pos_Y -= 1
        elif direction == 'b_g_g':
            self.Pos_X -= 2
            self.Pos_Y -= 1
        elif direction == 'b_b_g':
            self.Pos_X -= 1
            self.Pos_Y -= 2
        elif direction == 'b_b_d':
            self.Pos_X += 1
            self.Pos_Y -= 2
