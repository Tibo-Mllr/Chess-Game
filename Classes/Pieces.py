from Jeu.Move import mvt_possible_tour


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
        self.points = 1

    def move(self, x, y):
        """Déplace le pion

        Arguments
        ---------
        x : entier
            Abscisse voulue
        y : entier
            Ordonnée voulue

        Sortie
        ------
        Aucune
        """

        # Peut bouger de 2 SI ET SEULEMENT SI il n'a pas bougé
        self.Pos_X, self.Pos_Y = x, y

        self.Moved = True

    def eat(self, d):
        """Mange un eautre pièce en diagonale

        Arguments
        ---------
        d : chaîne de caratère
            Direction : 'd' ou 'g'


        Sortie
        ------
        Aucune
        """
        self.Pos_Y += 1

        if d == 'd':
            self.Pos_X += 1
        elif d == 'g':
            self.Pos_X -= 1

    def change(self, choice):
        """Transforme le pion arrivé au bout

        Arguments
        ---------
        choice : classe
            Classe en la quelle il se transforme : Dame, Tour, Fou ou Cavalier

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

    def move(self, x, y):
        """Action

        Arguments
        ---------
        x : entier
            Abscisse voulue
        y : entier
            Ordonnée voulue

        Sortie
        ------
        Aucune
        """

        self.Pos_X, self.Pos_Y = x, y

        self.Moved = True

    def roque(self, d):
        """Roque du roi

        Arguments
        ---------
        d : chaîne de caractères
            Direction du roque : 'd' ou 'g'

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
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        """Définit la tour

        Arguments
        ---------
        cote : chaîne de caractères
            Côté de la tour : 'g' ou 'd'
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
        self.points = 5

    def petit_roque(self):
        """Petit roque de la tour

        Arguments
        ---------
        Aucun

        Sortie
        ------
        Aucune
        """

        if self.Moved == False:
            self.Pos_X = 5
            self.Moved = True

    def grand_roque(self):
        """Grand roque de la tour

        Arguments
        ---------
        Aucun

        Sortie
        ------
        Aucune
        """

        if self.Moved == False:
            self.Pos_X = 3
            self.Moved = True

    def move(self, x, y):
        """Déplace la tour

        Arguments
        ---------
        x : entier
            Abscisse voulue
        y : entier
            Ordonnée voulue

        Sortie
        ------
        Aucune
        """

        self.Pos_X, self.Pos_Y = x, y
        self.Moved = True


class Dame:
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        """Définit la dame

        Arguments
        ---------
        cote : châine de caractère
            Seulement pour normaliser avec les autres
        color : châine de caractère
            Couleur de la dame : 'White' ou 'Black'
        Change : booléen
            True si vient d'une transformation d'un pion
        X : entier
            Position du pion transformé
        Y : entier
            Position du pion transformé

        Sortie
        ------
        L'entité Dame
        """

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
        self.points = 9

    def move(self, x, y):
        """Déplace la dame

        Arguments
        ---------
        x : entier
            Abscisse voulue
        y : entier
            Ordonnée voulue

        Sortie
        ------
        Aucune
        """

        self.Pos_X, self.Pos_Y = x, y


class Fou:
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        """Définit le fou

        Arguments
        ---------
        cote : chaîne de caractères
            Coté du fou
        color :
            Couleur du fou
        Change : booléen
            True si vient d'une transformation de pion
        X : entier
            Position du pion transformé
        Y : entier
            Position du pion transformé

        Sortie
        ------
        L'entité Fou
        """

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
        self.points = 3

    def move(self, x, y):
        """Déplace le fou

        Arguments
        ---------
        x : entier
            Abscisse voulue
        y : entier
            Ordonnée voulue

        Sortie
        ------
        Aucune
        """

        self.pos_X, self.Pos_Y = x, y


class Cavalier:
    def __init__(self, cote, color, Change=False, X=3, Y=3):
        """Définit le cavalier

        Arguments
        ---------
        cote : chaîne de caractères
            Côté du cavalier : 'd' ou 'g'
        color : chaîne de caractères
            Couleur du cavalier
        Change : booléen
            True si vient d'une transformation d'un pion
        X : entier
            Position du pion transformé
        Y : entier
            Position du pion transformé

        Sortie
        ------
        L'entité Cavalier
        """

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
        self.points = 3

    def move(self, x, y):
        """Déplace le cavalier

        Arguments
        ---------
        x : entier
            Abscisse voulue
        y : entier
            Ordonnée voulue


        Sortie
        ------
        Aucune
        """

        self.Pos_X, self.Pos_Y = x, y
