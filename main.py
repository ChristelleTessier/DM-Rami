"""Implémentation de la classe Main."""

from carte import Carte
from base import _ListeCartes

class Main(_ListeCartes):
    """ """
    def __init__(self, cartes = []):
        self.__cartes = cartes

    def __eq__(self,cartes):
        return 1

    def piocher(self):
        return 1

    def jeter(self):
        return 1

    def poser(self):
        return 1
