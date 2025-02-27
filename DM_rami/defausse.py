"""Implémentation de la classe Defausse."""
import random
from base import _ListeCartes
from carte import Carte

class Defausse(_ListeCartes):
    def __init__(self, cartes=None):
        """Initialise la défausse."""
        if cartes is None:
            cartes = []  # Initialise avec une liste vide si aucun paramètre n'est donné
        elif not isinstance(cartes, list):
            raise ValueError("L'argument 'cartes' doit être une liste.")
        super().__init__(cartes)  # Appelle le constructeur de _ListeCartes
    
    def vider(self, reserve):
        """Méthode qui vide la défausse dans la réserve."""
        if not self.cartes:  # Utilisation du getter `cartes` pour accéder à la liste
            return False  # Si la défausse est vide, retourne False
        
        # Mélange et ajoute les cartes à la réserve
        self.melanger()
        for carte in self.cartes:
            reserve.ajouter_carte(carte)
        
        # Réinitialise la défausse (vide les cartes) en utilisant la méthode de la classe parente
        self.reinitialiser()  # Appel d'une méthode publique pour vider la défausse
        return True
    
    def reinitialiser(self):
        """Vider toutes les cartes de la défausse."""
        self.cartes.clear()  # Cela vide effectivement la liste des cartes

    def __str__(self):
        """Affichage de la défausse sous forme de chaîne."""
        return f"Défausse: [{', '.join(str(carte) for carte in self.cartes)}]"
