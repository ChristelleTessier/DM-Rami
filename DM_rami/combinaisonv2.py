"""Implémentation de la classe Combinaison."""
import copy
from carte import Carte


class Combinaison():
    """Figure du rami (brelan, carré, suite).

    Méthodes héritées : ajouter_carte, retirer_carte

    Parameters
    ----------
    cartes : tuple de Carte
        Tuple contenant les cartes de la combinaison.
        Si cartes = None : genere 2 jeux de 52 cartes

    Examples
    --------
    >>> c1 = Carte("As","Pique")
    >>> c2 = Carte("Roi","Pique")
    >>> c3 = Carte("Dame","Pique")
    >>> l1 = Combinaison((c1, c2, c3))
    >>> print(l1)
    (2 de pique, Roi de pique, Dame de pique)
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
        """Retourne une copie profonde du tuple de cartes."""
        return copy.deepcopy(self.__cartes)

    def __eq__(self, other):
        """Vérifie si deux combinaisons sont égales."""
        # 1. Prend en compte l'ordre (tester avec ordre différent renvoie False)
        # 2. Pour moi la combinaison ne peut pas être vide -> a vérifier
        # 3. Pas besoin de self.__cartes = orther.__cartes
        # car on a créer la propiété cartes juste au dessus
        if not isinstance(other.cartes, tuple):
            return False
        if len(other)==0 and len(self)==0:
            return True
        return self.cartes == other.cartes

    def __repr__(self):
        """Représentation officielle de la combinaison."""
        cartes_repr = [carte.__repr__() for carte in self.__cartes]
        return "Combinaison(" + ", ".join(cartes_repr) + ")"

    def __str__(self):
        """Convertit la combinaison en une chaîne de caractères."""
        cartes_str = [carte.__str__() for carte in self.__cartes]
        return "(" + ", ".join(cartes_str) + ")"

    def __len__(self):
        """Retourne le nombre de cartes dans la combinaison."""
        return len(self.__cartes)

    def est_brelan(self):
        """Vérifie si la combinaison est un brelan."""
        if len(self) != 3:
            return False
        valeurs = set([carte.valeur for carte in self.__cartes])
        couleurs = set([carte.couleur for carte in self.__cartes])
        if len(valeurs) == 1 and len(couleurs) == 3:
            return True
        else:
            return False

    def est_carre(self):
        """Vérifie si la combinaison est un carre."""
        if len(self) != 4:
            return False
        valeurs = set([carte.valeur for carte in self.cartes])
        couleurs = set([carte.couleur for carte in self.__cartes])
        if len(valeurs) == 1 and len(couleurs) == 4:
            return True
        else:
            return False

    def est_sequence(self):
        """Vérifie si la combinaison est une suite."""
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
        """Vérifie si la combinaison est valide (brelan, carré ou suitee)."""
        return self.est_brelan() or self.est_carre() or self.est_sequence()

    def calcule_nombre_points(self):
        """Calcule le nombre de points de la combinaison."""
        if self.est_valide():
            valeurs = [Carte.ORDRE()[carte.valeur] for carte in self.cartes]
            points = [Carte.POINT()[carte.valeur] for carte in self.cartes]
            point = sum(points)
            if self.est_sequence() and 1 in valeurs and 2 in valeurs:
                point -= 10
            return point
        return 0
