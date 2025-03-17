"""Implémentation de la classe Carte."""

class Carte:
    """Definition d'une carte d'un jeu de 52 cartes.

    Cette classe permet de gérer une collection de cartes, avec des fonctionnalités pour
     - afficher une carte (officiel et print).
     - tester l'égalité de deux cartes.
     - hasher une carte.

    Parameters
    ----------
        valeur (str) : valeur de la carte
          2,3,4,5,6,7,8,9,10,V,D,R,AS
        couleur (str) : couleur de la carte
          Pique, Coeur, Carreau, Trêfle

    Raises :
    ---------
        TypeError : Si l'argument valeur ou couleur n'est pas une chaîne de caractères.
        ValueError : Si l'argument valeur n'appartient pas à la liste de chaine
         de caracteur VALEUR
        ValueError : Si l'argument couleur n'appartient pas à la liste de chaine
         de caracteur COULEUR


    Attributes
    ----------
        VALEURS : liste des valeurs possibles
            ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        COULEURS : liste des couleurs possibles
            ["Pique", "Coeur", "Carreau", "Trêfle"]
        ORDRE : dictionnaire de l'ordre des cartes (l'as est initialisé à 1)
            {"As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "10": 10, "Valet": 11, "Dame": 12, "Roi": 13}
        POINT : dictionnaire des points de chaque cartes (l'as est initialisé à 11)
            {"As": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "10": 10, "Valet": 11, "Dame": 11, "Roi": 11}
    """

    def __init__(self, valeur, couleur):
        """ Initialise une nouvelle instance de Carte. """
        if not isinstance(valeur, str):
            raise TypeError(f"Le type de la valeur : {valeur} n'est pas correct")
        if not isinstance(couleur, str):
            raise TypeError(f"Le type de la couleur : {couleur} n'est pas correct")
        if valeur not in Carte.VALEURS():
            raise ValueError(f"La valeur {valeur} n'est pas correcte")
        if couleur not in Carte.COULEURS():
            raise ValueError(f"La couleur {couleur} n'est pas correcte")
        self.__couleur = couleur
        self.__valeur = valeur

    @classmethod
    def VALEURS(cls):
        """ Retourne un tuple des valeurs valides pour une carte.

        Returns:
        ----------
            tuple(str): Un tuple contenant les valeurs valides
            ("As", "2", "3", ..., "Roi").
        """
        return ("As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Valet", "Dame", "Roi")

    @classmethod
    def COULEURS(cls):
        """ Retourne un tuple des couleurs valides pour une carte.

        Returns:
        -----------
            tuple(str): Un tuple contenant les couleurs valides
            ("Pique", "Coeur", "Carreau", "Trèfle").
        """
        return ("Pique", "Coeur", "Carreau", "Trêfle")

    # Méthode ordre pour traiter la combinaison séquence
    @classmethod
    def ORDRE(cls):
        """ Retourne un dictionnaire définissant l'ordre des cartes.

        L'As a la valeur 1, le 2 la valeur 2, ..., le Roi la valeur 13.

        Returns:
        ------------
            dict{str, int}: Un dictionnaire où les clés sont les valeurs des
            cartes et les valeurs l'ordre de ces cartes.
        """
        return {"As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "10": 10, "Valet": 11, "Dame": 12, "Roi": 13}

    # Méthode point pour déterminer les points dans combinaison
    @classmethod
    def POINT(cls):
        """ Retourne un dictionnaire définissant le nombre de point de chaque carte.

        L'As et les figures valent 11 points et les cartes de 2 à 10 valent leur valeur
         nominale.

        Returns:
        ----------
            dict{str, int}: Un dictionnaire où les clés sont les valeurs des cartes
             et les valeurs le nombre de points de ces cartes.
        """
        return {"As": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "10": 10, "Valet": 11, "Dame": 11, "Roi": 11}

    @property
    def valeur(self):
        """Retourne la valeur de la carte.

        Cette propriété est en lecture seule.

        Returns:
        ---------
            str: La valeur de la carte (par exemple, "As", "2", "Roi").
        """
        return self.__valeur

    @property
    def couleur(self):
        """Retourne la couleur de la carte.

        Cette propriété est en lecture seule.

        Returns:
        -----------
            str: La couleur de la carte (par exemple, "Pique", "Coeur").
        """
        return self.__couleur

    def __repr__(self):
        """Retourne une représentation officielle d'une carte.

        Returns :
        ---------
            str: Une chaîne de caractères représentant la carte.

        Examples :
        ---------
        >>> carte = Carte("6","Pique")
        >>> print(carte.__repr__())
        Carte(6,Pique)
        """
        return f"Carte({self.__valeur},{self.__couleur})"

    def __str__(self):
        """Retourne une représentation en chaîne de caractères d'une carte.

        Returns :
        -------
            str : chaîne de caractères représentant une carte.

        Examples :
        ---------
        >>> carte = Carte("6","Pique")
        >>> print(carte)
        6 de pique
        """
        return f"{self.__valeur} de {self.__couleur.lower()}"

    def __eq__(self, other):
        """Vérifie si deux cartes sont égales.

        Deux cartes sont considérées comme égales si elles ont la même valeur et la même couleur.

        Parameters:
        ----------
            other (Carte): L'autre carte à comparer.

        Returns:
        --------
            bool: True si les deux cartes sont égales, False sinon.

        Examples :
        ---------
        >>> carte1 = Carte("As","Coeur")
        >>> carte2 = Carte("As","Coeur")
        >>> carte3 = Carte("Roi","Pique")
        >>> print(carte1 == carte2)
        True
        >>> print(carte1 == carte3)
        False
        >>> print(carte1 == "As de Coeur")
        False
        """
        if isinstance(other, Carte):
            return self.valeur == other.valeur and self.couleur == other.couleur
        return False

    def __hash__(self):
        """Retourne la valeur de hachage de la carte.

        Le hash est calculé à partir de la valeur et de la couleur de la carte,
        permettant ainsi de comparer facilement des cartes dans des structures
        de données comme les dictionnaires ou les ensembles.

        Returns:
        ---------
            int: La valeur de hachage de la carte.

        Examples :
        ---------
        >>> carte1 = Carte("As", "Coeur")
        >>> carte2 = Carte("As", "Coeur")
        >>> carte3 = Carte("Roi", "Pique")
        >>> print(hash(carte1) == hash(carte2))
        True
        >>> print(hash(carte1) == hash(carte3))
        False
        """
        return hash(repr(self))
