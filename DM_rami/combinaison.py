"""Implémentation de la classe Combinaison."""
import copy
from carte import Carte


class Combinaison():
    """Figure du rami (brelan, carré, suite).

    Cette classe permet de gérer une combinaison de cartes, avec des fonctionnalités pour
     - l'affichage
     - le test d'égalité
     - vérifier si brelan, carré ou suite.
     - vérifier si combinaison valide.
     - le nombre de points.

    Parameters
    ----------
        __cartes (tuple(Carte)) : Tuple contenant les cartes de la combinaison.

    Raises :
    ---------
        TypeError : Si l'argument 'cartes' n'est pas un tuple
        TypeError : Si chaque element du tuple n'est pas une instance de Carte
    """

    def __init__(self, cartes):
        """Constructeur de la classe Combinaison."""
        if not isinstance(cartes, tuple):
            raise TypeError("L'argument 'cartes' doit être un tuple de carte.")
        for carte in cartes:
            if not isinstance(carte, Carte):
                raise TypeError("L'argument 'cartes' doit être un tuple de carte.")
        self.__cartes = cartes

    @property
    def cartes(self):
        """Retourne une copie profonde du tuple de cartes.

        Returns
        -------
            tuple(Carte) : Un nouveau tuple contenant une copie profonde des cartes
             de la combinaison.
        """
        return copy.deepcopy(self.__cartes)

    def __eq__(self, other):
        """Vérifie si deux combinaisons sont égales.

        Deux combinaisons sont égales si elles contiennent les mêmes cartes,
        sans tenir compte de l'ordre.

        Parameters
        ----------
            other (Combinaison): L'autre combinaison à comparer.

        Returns
        -------
            bool: True si les deux combinaisons sont égales, False sinon.

        Examples
        -------
        >>> c1 = Carte("As", "Pique")
        >>> c2 = Carte("Roi", "Pique")
        >>> c3 = Carte("Dame", "Pique")
        >>> combi1 = Combinaison((c1,c2,c3))
        >>> combi2 = Combinaison((c3,c2,c1))
        >>> print(combi1 == combi2)
        True
        >>> print(combi1 == "As de pique")
        False
        """
        if isinstance(other, Combinaison):
            if len(self) != len(other):
                return False
            else:
                for carte in self.__cartes:
                    if carte not in other.cartes:
                        return False
                return True
        else:
            return False

    def __repr__(self):
        """Retourne une représentation officielle de la combinaison.

        Returns
        -------
            str : Une chaîne de caractères représentant la combinaison.

        Examples
        -------
        >>> c1 = Carte("As", "Pique")
        >>> c2 = Carte("Roi", "Pique")
        >>> c3 = Carte("Dame", "Pique")
        >>> combi1 = Combinaison((c1,c2,c3))
        >>> print(combi1.__repr__())
        Combinaison(Carte(As,Pique), Carte(Roi,Pique), Carte(Dame,Pique))
        """
        cartes_repr = [carte.__repr__() for carte in self.__cartes]
        return "Combinaison(" + ", ".join(cartes_repr) + ")"

    def __str__(self):
        """Convertit la combinaison en une chaîne de caractères.

        Returns
        -------
            str : Une chaîne de caractères représentant la combinaison.

        Examples
        -------
        >>> c1 = Carte("As", "Pique")
        >>> c2 = Carte("Roi", "Pique")
        >>> c3 = Carte("Dame", "Pique")
        >>> combi = Combinaison((c1,c2,c3))
        >>> print(combi)
        (As de pique, Roi de pique, Dame de pique)
        """
        cartes_str = [carte.__str__() for carte in self.__cartes]
        return "(" + ", ".join(cartes_str) + ")"

    def __len__(self):
        """Retourne le nombre de cartes dans la combinaison.

        Returns
        -------
            int : Le nombre de cartes dans la combinaison.

        Examples
        -------
        >>> c1 = Carte("As", "Pique")
        >>> c2 = Carte("Roi", "Pique")
        >>> c3 = Carte("Dame", "Pique")
        >>> combi1 = Combinaison((c1,c2,c3))
        >>> print(len(combi1))
        3
        """
        return len(self.__cartes)

    def est_brelan(self):
        """Vérifie si la combinaison est un brelan.

        Un brelan est une combinaison de 3 cartes de même valeur et de couleurs différentes.

        Returns
        -------
            bool : True si la combinaison est un brelan, False sinon.

        Examples
        -------
        >>> c1 = Carte("As", "Pique")
        >>> c2 = Carte("As", "Coeur")
        >>> c3 = Carte("As", "Carreau")
        >>> combi1 = Combinaison((c1,c2,c3))
        >>> print(combi1.est_brelan())
        True
        >>> c4 = Carte("Roi", "Pique")
        >>> combi2 = Combinaison((c1,c2,c4))
        >>> print(combi2.est_brelan())
        False
        """
        if len(self) != 3:
            return False
        valeurs = set([carte.valeur for carte in self.__cartes])
        couleurs = set([carte.couleur for carte in self.__cartes])
        if len(valeurs) == 1 and len(couleurs) == 3:
            return True
        else:
            return False

    def est_carre(self):
        """Vérifie si la combinaison est un carré.

        Un carré est une combinaison de 4 cartes de même valeur et de couleurs différentes.

        Returns
        -------
            bool : True si la combinaison est un carré, False sinon.

        Examples
        -------
        >>> c1 = Carte("As", "Pique")
        >>> c2 = Carte("As", "Coeur")
        >>> c3 = Carte("As", "Carreau")
        >>> c4 = Carte("As", "Trêfle")
        >>> combi1 = Combinaison((c1,c2,c3,c4))
        >>> print(combi1.est_carre())
        True
        >>> c5 = Carte("Roi", "Pique")
        >>> combi2 = Combinaison((c1,c2,c3,c5))
        >>> print(combi2.est_carre())
        False
        """
        if len(self) != 4:
            return False
        valeurs = set([carte.valeur for carte in self.cartes])
        couleurs = set([carte.couleur for carte in self.__cartes])
        if len(valeurs) == 1 and len(couleurs) == 4:
            return True
        else:
            return False

    def est_sequence(self):
        """Vérifie si la combinaison est une suite.

        Une suite est une combinaison d'au moins 3 cartes de même couleur
        dont les valeurs se suivent.

        Returns
        -------
            bool : True si la combinaison est une suite, False sinon.

        Examples
        -------
        >>> c1 = Carte("Dame", "Pique")
        >>> c2 = Carte("Roi", "Pique")
        >>> c3 = Carte("As", "Pique")
        >>> combi1 = Combinaison((c2,c1,c3))
        >>> print(combi1.est_sequence())
        True
        """
        if len(self) < 3:
            return False
        couleurs = set([carte.couleur for carte in self.cartes])
        if len(couleurs) != 1:
            return False

        valeurs = [Carte.ORDRE()[carte.valeur] for carte in self.cartes]
        valeurs.sort()

        # Cas particulier de la suite D, R, As
        if valeurs == [1, 12, 13]: # correct ici
            return True

        prec = valeurs[0]
        for valeur in valeurs[1:]:
            if valeur - prec != 1:
                return False
            prec = valeur

        return True

    def est_valide(self):
        """Vérifie si la combinaison est valide.

        Une combinaison est valide si elle est un brelan, un carré ou une suite.

        Returns
        -------
            bool : True si la combinaison est valide, False sinon.

        Examples
        -------
        >>> c1 = Carte("As", "Pique")
        >>> c2 = Carte("As", "Coeur")
        >>> c3 = Carte("As", "Carreau")
        >>> combi_brelan = Combinaison((c1,c2,c3))
        >>> print(combi_brelan.est_valide())
        True
        >>> c4 = Carte("As", "Trêfle")
        >>> combi_carre = Combinaison((c1,c2,c3,c4))
        >>> print(combi_carre.est_valide())
        True
        >>> c5 = Carte("Roi", "Pique")
        >>> combi_invalide = Combinaison((c1,c2,c5))
        >>> print(combi_invalide.est_valide())
        False
        """
        return self.est_brelan() or self.est_carre() or self.est_sequence()

    def calcule_nombre_points(self):
        """Calcule le nombre de points de la combinaison.

        Le nombre de points est calculé en additionnant les points de chaque carte.
        Dans une suite As, 2, 3 l'as vaut 1
        Dans une suite Dame, Roi, As l'as vaut 11

        Returns
        -------
            int : Le nombre de points de la combinaison.

        Examples
        -------
        >>> c1 = Carte("As", "Pique")
        >>> c2 = Carte("As", "Coeur")
        >>> c3 = Carte("As", "Carreau")
        >>> combi_brelan = Combinaison((c1,c2,c3))
        >>> print(combi_brelan.calcule_nombre_points())
        33
        """
        if self.est_valide():
            valeurs = [Carte.ORDRE()[carte.valeur] for carte in self.cartes]
            points = [Carte.POINT()[carte.valeur] for carte in self.cartes]
            point = sum(points)
            if self.est_sequence() and 1 in valeurs and 2 in valeurs:
                point -= 10
            return point
        return 0
