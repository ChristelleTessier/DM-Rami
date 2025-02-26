"""Implémentation de la classe Main."""

from carte import Carte
from base import _ListeCartes
from reserve import Reserve
from defausse import Defausse


class Main(_ListeCartes):
    """ """
    def __init__(self, cartes = []):
        """ Constructeur """
        super().__init__(cartes) # Utiliser le constructeur de la classe mère (_ListeCartes)
        self.__cartes = cartes

    def __eq__(self,other : _ListeCartes):
        "Test d'égalité sans ordre"
        if not isinstance(other,_ListeCartes):
            raise TypeError("On ne peut tester l'égalité que de deux mains")
        if len(self)!=len(other):
            return False
        else:
            for carte in self.cartes:
                if carte not in other.cartes:
                    return False
        return True

    def piocher(self, reserve):
        if not isinstance(reserve, Reserve):
            raise TypeError("reserve représente la reserve de carte")
        self.ajouter_carte(reserve.retirer_carte())

    def jeter(self, indice, defausse):
        if not isinstance(indice, int):
            raise TypeError("Indice doit etre un entier compris entre 0 et "
                            f"{len(self)-1}, {indice} n'est pas valide")
        if indice < 0 or indice > len(self):
            raise ValueError("Indice doit etre un entier compris entre 0 et "
                            f"{len(self)-1}, {indice} n'est pas valide")
        if not isinstance(defausse,Defausse):
            raise TypeError("defausse représente la defausse de carte")
        carte = self.retirer_carte(indice)
        defausse.ajouter_carte(carte)

    def poser(self, indices_combinaison, premiere_pose):
        if not isinstance(indices_combinaison,list):
            raise TypeError("indices_combinaison doit être une liste de liste d'entier")
        ensemble_indice = set()
        nb_indice = 0
        for combinaison in indices_combinaison:
            if not isinstance(combinaison,list):
                raise TypeError(
                    "indices_combinaison doit être une liste de liste d'entier")
            for indice in combinaison:
                if not isinstance(indice,int):
                    raise TypeError(
                        "les indices doivent être des nombres entiers compris entre 0 "
                        f"et {len(self)-1}")
                if indice < 0 or indice > len(self):
                    raise ValueError(
                        "les indices doivent être des nombres entiers compris entre 0 "
                        f"et {len(self)-1}")
                ensemble_indice.append(indice)
                nb_indice += 1
        if len(ensemble_indice) != nb_indice:
            raise ValueError("Tous les indices doivent être différent")
        if not isinstance(premiere_pose, bool):
            raise TypeError("Premiere_pose doit être un booléen")


        return 1
