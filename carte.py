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
    valeurs : liste des valeurs possibles
    ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
    couleurs : liste des couleurs possibles
    ["Pique", "Coeur", "Carreau", "Trêfle"]
    Examples
    --------
    Exemple d'utilisation
    >>> carte = Carte("2","Carreau")
    >>> print(carte)
    2 de carreau

    """

    def __init__(self, valeur, couleur):
        """Constructeur"""
        if not isinstance(valeur,str):
            raise TypeError(f"Le type de la valeur : {valeur} n'est pas correct")
        if not isinstance(couleur,str):
            raise TypeError(f"Le type de la couleur : {couleur} n'est pas correct")
        if valeur not in Carte.VALEURS():
            raise ValueError(f"La valeur {valeur} n'est pas correcte")
        if couleur not in Carte.COULEURS():
            raise ValueError(f"La couleur {couleur} n'est pas correcte")
        self.__couleur = couleur
        self.__valeur = valeur

    @staticmethod
    def VALEURS():
        return ("As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                           "Valet", "Dame", "Roi")

    @staticmethod
    def COULEURS():
        return ("Pique", "Coeur", "Carreau", "Trêfle")

    def __repr__(self):
        """Représentation officiel"""
        return f"Carte({self.__valeur},{self.__couleur})"

    def __str__(self):
        """Convertion en chaine de caractère"""
        return f"{self.__valeur} de {self.__couleur.lower()}"
