"""Implémentation de la classe Main."""

from carte import Carte
from base import _ListeCartes
from reserve import Reserve
from defausse import Defausse
from combinaison import Combinaison


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
            for carte in self.__cartes:
                if carte not in other.cartes:
                    return False
        return True

    def piocher(self, reserve):
        if not isinstance(reserve, Reserve):
            raise TypeError("reserve représente la reserve de carte")
        self.ajouter_carte(reserve.retirer_carte(len(self)-1))

    def jeter(self, indice, defausse):
        if not isinstance(indice, int):
            raise TypeError("Indice doit etre un entier compris entre 0 et "
                            f"{len(self)-1}")
        if indice < 0 or indice >= len(self):
            raise ValueError("Indice doit etre un entier compris entre 0 et "
                            f"{len(self)-1}")
        if not isinstance(defausse,Defausse):
            raise TypeError("defausse représente la defausse de carte")
        carte = self.retirer_carte(indice)
        defausse.ajouter_carte(carte)

    def poser(self, indices_combinaison, premiere_pose):
        # Lève l'erreur de type indices_combinaison
        if not isinstance(indices_combinaison,list):
            raise TypeError("indices_combinaison doit être une liste de liste d'entier")
        ensemble_indice = set()
        nb_indice = 0
        for combinaison in indices_combinaison:
            # Lève l'erreur de type indices_combinaison
            if not isinstance(combinaison,list):
                raise TypeError(
                    "indices_combinaison doit être une liste de liste d'entier")
            # Lève l'erreur de type/Valeurs indices
            for indice in combinaison:
                if not isinstance(indice,int):
                    raise TypeError(
                        "les indices doivent être des nombres entiers compris entre 0 "
                        f"et {len(self)-1}")
                if indice < 0 or indice > len(self):
                    raise ValueError(
                        "les indices doivent être des nombres entiers compris entre 0 "
                        f"et {len(self)-1}")
                ensemble_indice.add(indice)
                nb_indice += 1
        # Lève l'erreur de valeur indices tous différent
        if len(ensemble_indice) != nb_indice:
            raise ValueError("Tous les indices doivent être différent")
        # Lève l'erreur de type premiere_pose
        if not isinstance(premiere_pose, bool):
            raise TypeError("Premiere_pose doit être un booléen")
        # Lève l'erreur si au moins une combinaison pas valable et ou pas de suite ou
        # pas assez de point
        val_sequ = 0
        nb_point = 0
        list_comb = []
        for combinaison in indices_combinaison:
            comb_liste = _ListeCartes([])
            # Récupérer toutes les cartes de la combinaison sans les retirer de la main
            # et en faire un tuple
            for indice in combinaison:
                comb_liste.ajouter_carte(self.cartes[indice])
            # Transformation en tuple
            comb = Combinaison(tuple(comb_liste.cartes))
            if not comb.est_valide():
                raise ValueError(f"{comb.__str__()} n'est pas une combinaison valide")
            if comb.est_sequence():
                val_sequ = 1
            nb_point += comb.calcule_nombre_points()
            list_comb.append(comb)
        if premiere_pose:
            if val_sequ == 0:
                raise ValueError("Il n'y a pas de suite")
            if nb_point < 52:
                raise ValueError("Pour la 1ere pose il faut au moins 51 points pour poser")

        # On retire les cartes d'indice données
        # Transformation de l'ensemble d'indice en tableau d'indice trier dans l'ordre
        # décroissant
        ensemble_indice = list(ensemble_indice)
        ensemble_indice.sort(reverse = True)
        for indice in ensemble_indice:
            self.retirer_carte(indice)

        # Pour première pose si il ne reste plus de carte -> les points calculer pour
        # les adversaire seront doublé

        return list_comb, nb_point
