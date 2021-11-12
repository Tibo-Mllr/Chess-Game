class Pion:
    def __init__(self, X, color):  # Initialisation du pion
        self.Pos_X = X

        if color == 'White':
            self.Pos_Y = 1
        if color == 'Black':
            self.Pos_Y = 6

        self.Color = color
        self.Moved = False

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
            self = choice(self.X_pos, self.Y_pos, self.Color)


class Roi:
    # Initialisation du Roi
    def __init__(self, color):
        self.Pos_X = 4

        if color == 'White':
            self.Pos_Y = 0
        if color == 'Black':
            self.Pos_y = 7

        self.Moved = False
        self.Checked = False
        self.Color = color

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
