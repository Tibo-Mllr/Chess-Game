class Pion:
    def __init__(self, X, color):
        """Définit le pion

        Arguments
        ---------
        X : entier
            Abscisse du pion : de 0 à 7
        color : chaîne de caratères
            Couleur du pion : 'White' ou 'Black'

        Sortie
        ------
        L'entité Pion
        """

        self.Pos_X = X

        if color == 'White':
            self.Pos_Y = 1
        if color == 'Black':
            self.Pos_Y = 6

        self.Color = color
        self.Moved = False
        self.name = 'pion'

    def move(self, c):
        """Déplace le pion

        Arguments
        ---------
        c : entier
            valeur de la quelle vous voulez avancer : 1 ou 2

        Sortie
        ------
        Aucune
        """

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

    def eat(self, d):
        """Mange un eautre pièce en diagonale

        Arguments
        ---------
        d : chaîne de caratère
            direction : 'd' ou 'g'


        Sortie
        ------
        Aucune
        """

        self.move(1)
        if d == 'R':
            self.Pos_X += 1
        else:
            self.Pos_X -= 1

    def change(self, choice):
        """Transforme le pion arrivé au bout

        Arguments
        ---------
        choice : classe
            classe en la quelle il se transforme : Dame, Tour, Fou ou Cavalier

        Sortie
        ------
        L'objet désiré
        """

        if self.Y_Pos in [7, 0]:
            # ATTENTION : Concordance à vérifier
            self = choice(self.Color, 'g', True, self.Pos_X, self.Pos_Y)


class Roi:
    def __init__(self, color):
        """Définit le roi

        Arguments
        ---------
        color : chaîne de caracères
            Couleur du roi : 'White' ou 'Black'

        Sortie
        ------
        L'entité du Roi
        """

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
        """Action

        Arguments
        ---------
        d : chaîne de caractères
            Définit les mouvements du roi : 'd', 'g', 'h', 'b' ou *_d , *_g si diagonal

        Sortie
        ------
        Aucune
        """

        # Mouvements normaux
        if d[0] == 'd':
            self.Pos_X += 1

        elif d[0] == 'g':
            self.Pos_X -= 1

        elif d[0] == 'h':
            self.Pos_Y += 1

        elif d[0] == 'b':
            self.Pos_Y -= 1

        # Puis mouvements diagonaux
        # Par convention si deux mouvements : 'h' ou 'b' PUIS '_' PUIS 'd' ou 'g'
        if len(d) == 3:
            if d[2] == 'd':
                self.Pos_X += 1
            elif d[2] == 'g':
                self.Pos_X -= 1

        self.Moved = True

    def rock(self, d):
        """Rock du roi

        Arguments
        ---------
        d : chaîne de caractères
            Direction du rock : 'd' ou 'g'

        Sortie
        ------
        Aucune
        """

        if not self.Checked and not self.Moved:
            if d == 'd':
                self.Pos_X += 2
            elif d == 'g':
                self.Pos_X -= 2


class Tour:

    # cote = d ou g, color = White ou Black
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        """Définit la tour

        Arguments
        ---------
        cote : chaîne de caractères
            côté de la tour : 'g' ou 'd'
        color : chaîne de caractères
            Couleur de la tour : 'White' ou 'Black'
        Change : booléen
            True si vient d'une transformation d'un pion
        X : entier
            Position du pion transformé
        Y : entier
            Position du pion transformé

        Sortie
        ------
        L'entité Tour
        """

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
        """Petit rock de la tour

        Arguments
        ---------
        Aucun

        Sortie
        ------
        Aucune
        """

        if self.Moved == False:  # and Condition roi pas mis en échec et pas de pièce sur le chemin
            self.Pos_X = 5
            self.Moved = True

    def grand_rock(self):
        """Grand rock de la tour

        Arguments
        ---------
        Aucun

        Sortie
        ------
        Aucune
        """

        if self.Moved == False:  # and Condition roi pas mis en échec et pas de pièce sur le chemin
            self.Pos_X = 3
            self.Moved = True

    # longueur dans [|-7;7|], direction = horizontale ou verticale
    def move(self, valeur, direction):
        """Déplace la tour

        Arguments
        ---------
        valeur : entier
            nombre de case duquel on veut se déplacer : de 0 à 7
        direction : chaîne de caractères
            Direction algébrique du déplacement : 'horizontale' ou 'verticale'

        Sortie
        ------
        Aucune
        """

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
