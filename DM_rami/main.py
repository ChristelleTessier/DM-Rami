"""Implémentation de la classe Main."""

from carte import Carte
from base import _ListeCartes
from reserve import Reserve
from defausse import Defausse
from combinaison import Combinaison


class Main(_ListeCartes):
    """Représente la main d'un joueur au Rami.

    Cette classe hérite de _ListeCartes et représente la main d'un joueur,
    c'est-à-dire l'ensemble des cartes qu'il a en sa possession.

    Elle récupère les méthodes héritées de _ListeCartes
     - afficher une liste de carte (print).
     - calculer la longueur d'une liste de carte
     - mélanger une liste de carte.
     - ajouter une carte à une liste de carte.
     - retiter une carte d'une liste de carte.

    Elle propose des fonctionnalités supplémentaires pour :
     - tester l'égalité entre deux mains.
     - piocher une carte dans la réserve.
     - jeter une carte dans la défausse.
     - poser une ou plusieurs combinaisons de cartes sur la table.

    Attributes
    ----------
        __cartes (list[Carte]) : La liste des cartes dans la main.

    Raises (Hérité de _ListeCartes)
    ------
        TypeError
            Si l'argument cartes n'est pas une liste ou qu'un élement de la liste n'est
            pas une instance de Carte.
    """
    def __init__(self, cartes = []):
        """ Constructeur """
        super().__init__(cartes) # Utiliser le constructeur de la classe mère (_ListeCartes)
        self.__cartes = cartes

    def __eq__(self,other : _ListeCartes):
        """Vérifie si deux mains sont égales (contiennent les mêmes cartes, sans tenir
        compte de l'ordre).

        Parameters
        ----------
            other (Main): L'autre main à comparer.

        Returns
        -------
            bool: True si les deux mains contiennent les mêmes cartes, False sinon.

        Examples
        --------
        >>> main1 = Main([Carte("As", "Pique"), Carte("Roi", "Coeur")])
        >>> main2 = Main([Carte("Roi", "Coeur"), Carte("As", "Pique")])
        >>> print(main1 == main2)
        True
        >>> main3 = Main([Carte("As", "Pique")])
        >>> print(main1 == main3)
        False
        """
        if isinstance(other,Main):
            if len(self) != len(other):
                return False
            else:
                for carte in self.__cartes:
                    if carte not in other.cartes:
                        return False
                return True
        else :
            return False

    def piocher(self, reserve):
        """Pioche une carte dans la réserve et l'ajoute à la main.

        Parameters
        ----------
            reserve (Reserve): La réserve dans laquelle piocher.

        Raises
        -------
            TypeError: Si l'argument reserve n'est pas une instance de Reserve.

        Examples
        --------
        >>> reserve = Reserve([Carte("As", "Pique")])
        >>> main = Main()
        >>> main.piocher(reserve)
        >>> print(main)
        [As de pique]
        """
        if not isinstance(reserve, Reserve):
            raise TypeError("reserve représente la reserve de carte")
        self.ajouter_carte(reserve.retirer_carte(len(reserve)-1))

    def jeter(self, indice, defausse):
        """Jette une carte de la main dans la défausse.

        Parameters
        ----------
            indice (int): L'indice de la carte à jeter dans la main (0 à len(main) - 1).
            defausse (Defausse): La défausse dans laquelle jeter la carte.

        Raises
        -------
            TypeError: Si l'argument indice n'est pas un entier ou l'argument
                defausse n'est pas une instance de Defausse.
            ValueError: Si l'argument indice n'est pas compris entre 0 et len(self) - 1.

        Examples
        --------
        >>> defausse = Defausse()
        >>> main = Main([Carte("As", "Pique"), Carte("Roi", "Coeur")])
        >>> main.jeter(0, defausse)
        >>> print(main)
        [Roi de coeur]
        >>> print(defausse)
        Défausse: [As de pique]
        """
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
        """Pose une ou plusieurs combinaisons de cartes sur la table.

        Cette méthode permet de poser une ou plusieurs combinaisons de cartes
        (brelan, carré, suite) de la main sur la table. La méthode vérifie si les
        combinaisons sont valides. Pour une premiere pose le nombre de point doit être
        supérieur à 51

        Parameters
        ----------
            indices_combinaison (list[list[int]]): Une liste de listes d'indices.
                Chaque sous-liste représente une combinaison et contient les indices
                des cartes de la main qui la composent.
            premiere_pose (bool): True si c'est la première fois que le joueur
                pose des cartes, False sinon.

        Returns
        -------
            tuple(list[Combinaison],int): Une liste de Combinaison correspondant aux
                combinaisons posées et le nombre de points des combinaisons.

        Raises
        -------
            TypeError: Si l'argument indices_combinaison n'est pas une liste
                de liste d'entiers, ou si l'argument premiere_pose n'est pas un
                booléen.
            ValueError: Si les indices ne sont pas valides (hors limites, doublons),
                si les combinaisons ne sont pas valides (pas un brelan, un carré ou
                une suite), ou si la première pose ne respecte pas les règles
                (pas de suite ou moins de 52 points).

        Examples
        --------
        >>> main = Main([Carte("As", "Pique"), Carte("As", "Coeur"), Carte("As", "Carreau"), Carte("Valet", "Pique"), Carte("Dame", "Pique"), Carte("Roi", "Pique")])
        >>> pose, points = main.poser([[0, 1, 2], [3, 4, 5]], True)
        >>> print(main)
        []
        >>> print([str(comb) for comb in pose])
        ['(As de pique, As de coeur, As de carreau)', '(Valet de pique, Dame de pique, Roi de pique)']
        >>> print(points)
        66
        """
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
