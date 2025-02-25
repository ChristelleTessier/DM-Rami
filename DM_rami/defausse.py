"""Implémentation de la classe Defausse."""


from base import _ListeCartes
from carte import Carte


class Defausse(_ListeCartes):
    """ """
    def __init__(self,cartes):
        self.__cartes = cartes

    def vider(self):
        return 1
