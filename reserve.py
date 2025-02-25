"""Implémentation de la classe Reserve."""


from base import _ListeCartes
from carte import Carte

class Reserve(_ListeCartes):
    """  """
    def __init__(self, cartes = []):
        self.__cartes = cartes

    def distribuer(self):
        return 1
