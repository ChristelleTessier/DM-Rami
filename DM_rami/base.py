"""Implémentation de la classe _ListeCartes."""
import copy
import random

from carte import Carte


class _ListeCartes():
    """ Représente une liste de carte

    Cette classe permet de gérer une collection de cartes, avec des fonctionnalités pour
     - afficher une liste de carte (officiel et print).
     - calculer la longueur d'une liste de carte
     - tester l'égalité de deux listes de cartes.
     - mélanger une liste de carte.
     - ajouter une carte à une liste de carte.
     - retiter une carte d'une liste de carte.

    Parameters :
    ------------
        __cartes (list[Carte], optional): Une liste de cartes pour initialiser la liste.
                Si None, un jeu de 104 cartes est créé (deux jeux de 52 cartes).

    Raises :
    -------
        ValueError : Si l'argument 'cartes' n'est pas None ou une liste de cartes,
            ou si un element de la liste n'est pas une instance de Carte.

    """

    def __init__(self, cartes=None):
        """ Initialise une nouvelle instance de _ListeCartes. """
        self._cartes = []
        if cartes is not None:
            if isinstance(cartes, Carte):
                raise ValueError("L'argument 'cartes' doit être None ou une liste de cartes.")
            if not isinstance(cartes, list):
                raise ValueError("L'argument 'cartes' doit être None ou une liste de cartes.")
            for carte in cartes:
                if not isinstance(carte, Carte):
                    raise ValueError("L'argument 'cartes' doit être None ou une liste de cartes.")
            self.__cartes = cartes
        else:
            self.__cartes = [Carte(valeur, couleur) for valeur in Carte.VALEURS()
                             for couleur in Carte.COULEURS()] * 2

    @property
    def cartes(self):
        """Retourne une copie profonde de la liste des cartes.

        Returns :
        ---------
            List[Carte] : Une nouvelle liste contenant une copie profonde des cartes.
        """
        return copy.deepcopy(self.__cartes)

    def __repr__(self):
        """Retourne une représentation officielle de la liste de cartes.

        Returns :
        ---------
            str: Une chaîne de caractères représentant la liste de cartes.

        Examples :
        ---------
        >>> liste_cartes = _ListeCartes([Carte("As","Coeur"), Carte("6","Pique")])
        >>> print(liste_cartes.__repr__())
        _ListeCartes[Carte(As,Coeur), Carte(6,Pique)]
        """
        if not self.__cartes:
            return "ListeCartes[]"
        cartes_repr = [carte.__repr__() for carte in self.__cartes]
        return "_ListeCartes[" + ", ".join(cartes_repr) + "]"

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de la liste de cartes.

        Returns :
        -------
            str : chaîne de caractères représentant les cartes dans la liste.

        Examples :
        ---------
        >>> liste_cartes = _ListeCartes([Carte("As","Coeur"), Carte("6","Pique")])
        >>> print(liste_cartes)
        [As de coeur, 6 de pique]
        """
        cartes_str = [carte.__str__() for carte in self.__cartes]
        return "[" + ", ".join(cartes_str) + "]"

    def __eq__(self, other):
        """Retourne si deux listes de cartes sont identiques.

        Parameters:
        ----------
            other (_ListeCartes): L'autre liste de cartes à comparer.

        Returns:
        --------
            bool: True si les deux listes de cartes sont égales, False sinon.


        Examples :
        ---------
        >>> liste_cartes = _ListeCartes([Carte("As","Coeur"), Carte("6","Pique")])
        >>> liste_cartes2 = _ListeCartes([Carte("As","Coeur"), Carte("6","Pique")])
        >>> print(liste_cartes == liste_cartes2)
        True
        >>> liste_cartes3 = _ListeCartes([Carte("As","Coeur"), Carte("7","Pique")])
        >>> print(liste_cartes == liste_cartes3)
        False
        """
        if not isinstance(other, _ListeCartes):
            return False
        if len(self) == 0 and len(other) == 0:
            return True
        return self.cartes == other.cartes

    def __len__(self):
        """Retourne le nombre de cartes dans la liste.

        Returns
        -------
            int : Longueur de la liste de cartes.

        Examples :
        ---------
        >>> liste_cartes = _ListeCartes()
        >>> print(len(liste_cartes))
        104
        >>> liste_cartes = _ListeCartes([Carte("As","Coeur"), Carte("6","Pique")])
        >>> print(len(liste_cartes))
        2
        """
        return len(self.__cartes)

    def melanger(self):
        """ Mélange les cartes dans la liste.

        Returns :
        --------
            None
        """
        random.shuffle(self.__cartes)

    def ajouter_carte(self, carte):
        """ Ajoute une carte à la liste.

        Args :
        ----------
            carte (Carte): La carte à ajouter.

        Raises:
        ----------
            TypeError: Si l'argument 'carte' n'est pas une instance de Carte.

        Returns :
        --------
            None

        Examples :
        ---------
        >>> liste_cartes = _ListeCartes([Carte("As","Coeur")])
        >>> liste_cartes.ajouter_carte(Carte("6","Pique"))
        >>> print(liste_cartes)
        [As de coeur, 6 de pique]
        """
        if not isinstance(carte, Carte):
            raise TypeError("L'argument 'carte' doit être une instance de Carte.")
        self.__cartes.append(carte)

    def retirer_carte(self, indice):
        """ Retirer une carte de la liste à un indice donné.

        Args :
        -------
            indice (int): L'indice de la carte à retirer.

        Raises:
        --------
            Exception : Si la liste est vide.
            ValueError : Si l'indice n'est pas valide.

        Returns :
        --------
            Carte: La carte retirée.

        Examples :
        ---------
        >>> liste_cartes = _ListeCartes([Carte("As","Coeur"), Carte("6","Pique")])
        >>> carte_retire = liste_cartes.retirer_carte(1)
        >>> print(carte_retire)
        6 de pique
        >>> print(liste_cartes)
        [As de coeur]
        """
        if not self.__cartes:
            raise Exception("La liste de cartes est vide, aucune carte ne peut être retirée.")
        if not isinstance(indice, int) or indice >= len(self.__cartes) or indice < 0:
            if isinstance(indice, str):
                raise ValueError(
                    f"L'indice de la carte à retirer n'est pas valide. "
                    f"L'indice doit être un entier compris entre 0 et {len(self.__cartes) - 1} inclus, "
                    f"mais l'indice est '{indice}'."
                )
            else:
                raise ValueError(
                    f"L'indice de la carte à retirer n'est pas valide. "
                    f"L'indice doit être un entier compris entre 0 et {len(self.__cartes) - 1} inclus, "
                    f"mais l'indice est {indice}."
                )
        return self.__cartes.pop(indice)
