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
        """Vide la défausse et transfère les cartes dans la réserve."""
        print(f"Avant vidage: {len(self.cartes)} cartes dans la défausse")
        if not self.cartes:
            # Vérifie si la défausse est vide
            return False

            

        self.melanger()
        for carte in self.cartes[:]:
            # Copie pour éviter les modifications pendant l'itération
            reserve.ajouter_carte(carte)

        self.reinitialiser()  # Vider la défausse
        print(f"Après vidage: {len(self.cartes)} cartes dans la défausse")  # Devrait être 0

        return True

    def reinitialiser(self):
       print(f"Avant vidage: {len(self.cartes)} cartes")  # Debug
       if isinstance(self.cartes, list):
           self._ListeCartes__cartes.clear()
       else:
           print("Attention: self.cartes n'est pas une liste mutable !")
       print(f"Après vidage: {len(self.cartes)} cartes")  # Devrait être 0

    def __str__(self):
        """Affichage de la défausse sous forme de chaîne."""
        return f"Défausse: [{', '.join(str(carte) for carte in self.cartes)}]"
