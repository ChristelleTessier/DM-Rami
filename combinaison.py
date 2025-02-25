"""Implémentation de la classe Combinaison."""


from base import _ListeCartes
from carte import Carte


class Combinaison(_ListeCartes):
    """ """
    def __init__(self,cartes = []):
        self.__cartes = cartes

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
