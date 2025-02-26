"""Implémentation de la classe Defausse."""


import random
from base import _ListeCartes
from carte import Carte

class Defausse(_ListeCartes):
    """Classe Defausse modélisant la liste des cartes jetées."""

    def __init__(self, cartes=None):
        """
        Initialise la défausse en appelant le constructeur de _ListeCartes.
        :param cartes: Liste de cartes initiales (par défaut vide).
        """
        if cartes is None:
            cartes = []  # Éviter l'utilisation d'une liste mutable comme valeur par défaut
        super().__init__(cartes)  # Utilisation correcte du constructeur parent

    def vider(self, reserve):
        """
        Mélange la défausse et l'ajoute à la fin de la réserve.
        :param reserve: Instance de la classe Réserve.
        """
        if not self._cartes:  # Vérifie si la défausse est vide
            return False
        
        random.shuffle(self._cartes)  # Mélange les cartes
        reserve._cartes.extend(self._cartes)  # Ajoute les cartes mélangées à la réserve
        self._cartes.clear()  # Vide la défausse
        return True  # Indique que l'opération a réussi

    def __str__(self):
        """Affichage de la défausse sous forme de chaîne."""
        return f"Défausse: [{', '.join(str(carte) for carte in self._cartes)}]"

  
