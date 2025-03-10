import random
from base import _ListeCartes
from carte import Carte

class Defausse(_ListeCartes):
    """Initialise la défausse.

    La classe Defausse permet de modéliser la défausse, c’est-à-dire la liste des cartes jetées.

  
    
    Attributes
    ----------
    __cartes (list[Carte]) : La liste des cartes dans la défausse.

    Raises (Hérité de _ListeCartes)
    ------
    TypeError
    L'argument 'cartes' doit être une liste.
    
    """
    
    def __init__(self, cartes=None):
        

        if cartes is None:
            cartes = []  # Initialise avec une liste vide si aucun paramètre n'est donné
        elif not isinstance(cartes, list):
            raise ValueError("L'argument 'cartes' doit être une liste.")
        super().__init__(cartes)  # Appelle le constructeur de _ListeCartes
    
    def vider(self, reserve):
        """Vide la défausse et transfère les cartes dans la réserve.
        
        Attributes
        ----------
        reserve(list[Carte]) : La liste des cartes dans la défausse.
        
        Examples :
        ---------
        >>> liste_cartes = _ListeCartes([Carte("As","Coeur"), Carte("6","Pique")])
        >>> defausse = Defausse(liste_cartes)
        >>> reserve = Reserve([])
        >>> defausse.vider(reserve)
        >>> print(len(defausse.liste_cartes)) # on vérifie que la défausse est vide
        >>> print(len(reserve.liste_cartes)) # on vérifie que la réserve n'est pas vide vide
        
        """
        
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
        """ """
        print(f"Avant vidage: {len(self.cartes)} cartes")  # Debug
        if isinstance(self.cartes, list):
           self._ListeCartes__cartes.clear()
        else:
           print("Attention: self.cartes n'est pas une liste mutable !")
        print(f"Après vidage: {len(self.cartes)} cartes")  # Devrait être 0

    def __str__(self):
        """Affichage de la défausse sous forme de chaîne."""
        return f"Défausse: [{', '.join(str(carte) for carte in self.cartes)}]"
