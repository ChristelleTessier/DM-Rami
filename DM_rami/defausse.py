"""Implémentation de la classe Defausse."""


from base import _ListeCartes
from carte import Carte


class Defausse(_ListeCartes):
    """ """
    def __init__(self,cartes):
        self.cartes = cartes

    def vider(self):
        return 1

    def __str__(self):
        """ Affichage de la défausse """
        return f"Défausse: [{', '.join(str(carte) for carte in self.cartes)}]"
