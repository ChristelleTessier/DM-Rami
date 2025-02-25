"""Implémentation de la classe _ListeCartes."""
import copy
import random

from carte import Carte


class _ListeCartes():
    """ Représente une liste de carte

    Cette classe permet de gérer une collection de cartes, avec des fonctionnalités
    pour l'initialisation, la manipulation (ajout, retrait), le mélange, et la comparaison
    de listes de cartes.
    """

    def __init__(self, cartes=None):
        """
        Initialise une nouvelle instance de _ListeCartes.

        Args:
            cartes (list[Carte], optional): Une liste de cartes pour initialiser la liste.
                Si None, un jeu de 104 cartes est créé (deux jeux de 52 cartes).
                Si une Carte est passé seul, une ValueError est levée.
                Si un element de la listes n'est pas une instance de Carte, une ValueError est levée.

        Raises:
            ValueError: Si l'argument 'cartes' n'est pas None ou une liste de cartes, ou si un element de la liste n'est pas une instance de Carte.
        """
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
        return copy.deepcopy(self.__cartes)

    def __repr__(self):
        if not self.__cartes:
            return "ListeCartes[]"
        cartes_repr = [carte.__repr__() for carte in self.__cartes]
        return "ListeCartes[" + ", ".join(cartes_repr) + "]"

    def __str__(self):
        cartes_str = [carte.__str__() for carte in self.__cartes]
        return "[" + ", ".join(cartes_str) + "]"

    def __eq__(self, other):
        if not isinstance(other, _ListeCartes):
            return False
        return self.cartes == other.cartes

    def __len__(self):
        return len(self.__cartes)

    def melanger(self):
        """Mélange les cartes dans la liste."""
        random.shuffle(self.__cartes)

    def ajouter_carte(self, carte):
        """
        Ajoute une carte à la liste.

        Args:
            carte (Carte): La carte à ajouter.

        Raises:
            TypeError: Si l'argument 'carte' n'est pas une instance de Carte.
        """
        if not isinstance(carte, Carte):
            raise TypeError("L'argument 'carte' doit être une instance de Carte.")
        self.__cartes.append(carte)

    def retirer_carte(self, indice):
        """
        Retire une carte de la liste à un indice donné.

        Args:
            indice (int): L'indice de la carte à retirer.

        Returns:
            Carte: La carte retirée.

        Raises:
            Exception: Si la liste est vide.
            ValueError: Si l'indice n'est pas valide.
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
