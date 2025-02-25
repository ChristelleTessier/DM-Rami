"""Implémentation de la classe _ListeCartes."""


from carte import Carte


class _ListeCartes():
    """ """
    def __init__(self, cartes = None):
        if cartes is not None:
            if isinstance(cartes,list):
                TypeError(f"Le type de cartes doit être une liste")
            for carte in cartes:
                if isinstance(carte, Carte):
                    TypeError(f"Chaque élément de cartes doit être une carte")
        self.__cartes = cartes

    def __repr__(self):
        return 1

    def __str__(self):
        return 1

    def __eq__(self):
        return True

    def __len__(self):
        return 1

    def melanger(self):
        return 1

    def ajouter_carte(self,carte):
        return 1

    def retirer_carte(self,carte):
        return 1
