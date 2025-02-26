"""Implémentation de la classe Carte."""

class Carte:
    """Definition d'une carte d'un jeu de 52 cartes.

    Parameters
    ----------
    valeur : 2,3,4,5,6,7,8,9,10,V,D,R,1
        valeur de la carte
    couleur : Pique, Coeur, Carreau, Trêfle
        couleur de la carte

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

    Examples
    --------
    Exemple d'utilisation
    >>> carte = Carte("2","Carreau")
    >>> print(carte)
    2 de carreau

    """


    def __init__(self, valeur, couleur):
        """Constructeur"""
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
        return ("As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "Valet", "Dame", "Roi")

    @classmethod
    def COULEURS(cls):
        return ("Pique", "Coeur", "Carreau", "Trêfle")

    # Méthode ordre pour traiter la combinaison séquence
    @classmethod
    def ORDRE(cls):
        return {"As": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "10": 10, "Valet": 11, "Dame": 12, "Roi": 13}

    # Méthode point pour déterminer les points dans combinaison et ...
    @classmethod
    def POINT(cls):
        return {"As": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                "9": 9, "10": 10, "Valet": 11, "Dame": 11, "Roi": 11}

    @property
    def valeur(self):
        """Retourne la valeur de la carte (lecture seule)."""
        return self.__valeur

    @property
    def couleur(self):
        """Retourne la couleur de la carte (lecture seule)."""
        return self.__couleur

    def __repr__(self):
        """Représentation officiel"""
        return f"Carte({self.__valeur},{self.__couleur})"

    def __str__(self):
        """Convertion en chaine de caractère"""
        return f"{self.__valeur} de {self.__couleur.lower()}"

    def __eq__(self, other):
        """Vérifie si deux cartes sont égales."""
        if isinstance(other, Carte):
            return self.valeur == other.valeur and self.couleur == other.couleur
        return False

    def __hash__(self):
        """Retourne un hash basé sur la représentation officielle de la carte."""
        return hash(repr(self))
