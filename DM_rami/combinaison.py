"""Implémentation de la classe Combinaison."""


from base import _ListeCartes
from carte import Carte


class Combinaison(_ListeCartes):
    """Figure du rami (brelan, carré, suite).

    Sous classe de Main,
    Méthodes héritées : ajouter_carte, retirer_carte

    Parameters
    ----------


    Attributes
    ----------
    ordre : dictionnaire donnant l'ordre de chaque carte en fonction de sa valeur
    ordre = {"1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
              "9" : 9, "10" : 10, "V" : 11, "D" : 12, "R" : 13}
    Examples
    --------
    Exemple d'utilisation

    """
    def __init__(self,cartes = []):
        self.__cartes = cartes

    @property
    def Carte(self):
        """Retourne la carte (lecture seule)."""
        return self.__carte

    def __eq__(self,cartes):
        return True

    def __str__(self):
        return 1

    def __len__(self):
        return 1

    def est_brelan(self):
        return 1

    def est_carre(self):
        return 1

    def est_sequence(self):
        return 1

    def est_valide(self):
        return 1

    def calcule_nombre_points(self):
        return 1
