"""Implémentation de la classe Combinaison."""
import copy

from carte import Carte


class Combinaison():
    """Figure du rami (brelan, carré, suite).

    Sous classe de Main,
    Méthodes héritées : ajouter_carte, retirer_carte

    Parameters
    ----------


    Attributes
    ----------
    ordre : dictionnaire donnant l'ordre de chaque carte en fonction de sa valeur
    ordre = {"1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
              "9" : 9, "10" : 10, "V" : 11, "D" : 12, "R" : 13}
    Examples
    --------
    Exemple d'utilisation

    """
    def __init__(self, cartes):
        if not isinstance(cartes, tuple):
                raise TypeError("L'argument 'cartes' doit être un tuple de carte.")
        for carte in cartes:
                if not isinstance(carte, Carte):
                    raise TypeError("L'argument 'cartes' doit être un tuple de carte.")
        self.__cartes = cartes

    @staticmethod
    def ORDRE():
        return {"As" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
              "9" : 9, "10" : 10, "Valet" : 11, "Dame" : 12, "Roi" : 13}

    @staticmethod
    def POINT():
        return {"As" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
              "9" : 9, "10" : 10, "Valet" : 11, "Dame" : 11, "Roi" : 11}

    @property
    def cartes(self):
        return copy.deepcopy(self.__cartes)

    def __eq__(self, other):
        if not isinstance(other, tuple):
            return False
            # pour moi il manque que si les deux combinaisons sont vides, elles sont égales:
        if not self.__cartes and not other.__cartes:
            return True
             # pour les comparer, il faut que les deux combinaison soient dans le même ordre
            #  sinon il y a des combinaisons qui vont être considérées comme non égales.
        return self.cartes == other.cartes
        #return sorted(self.cartes) == sorted(other.cartes), il ne faut pas self.__cartes et orther.__cartes?, c'est privé

    def __repr__(self):
        cartes_repr = [carte.__repr__() for carte in self.__cartes]
        return "Combinaison(" + ", ".join(cartes_repr) + ")"

    def __str__(self):
        cartes_str = [carte.__str__() for carte in self.__cartes]
        return "(" + ", ".join(cartes_str) + ")"

    def __len__(self):
        return len(self.__cartes)

    def est_brelan(self):
        if len(self) != 3:
            return False
        valeurs = set([carte.valeur for carte in self.__cartes])
        couleurs = set([carte.couleur for carte in self.__cartes])
        if len(valeurs) == 1 and len(couleurs) == 3:
            return True
        else :
            return False

    def est_carree(self):
        if len(self) != 4:
            return False
        valeurs = set([carte.valeur for carte in self.__cartes])
        couleurs = set([carte.couleur for carte in self.__cartes])
        if len(valeurs) == 1 and len(couleurs) == 4:
            return True
        else :
            return False

    def est_sequence(self):
        if len(self) < 3:
            return False
        couleurs = set([carte.couleur for carte in self.cartes])
        if len(couleurs) != 1:
            return False

        valeurs = [self.ORDRE()[carte.valeur] for carte in self.cartes]
        valeurs.sort()

        # Cas particulier de la suite D, R, As
        if valeurs == [1, 12, 13]:  # Correction ici
            return True

        prec = valeurs[0]
        for valeur in valeurs[1:]:
            if valeur - prec != 1:
                return False
            prec = valeur

        return True


    def est_valide(self):
        return self.est_brelan() or self.est_carree() or self.est_sequence()

    def calcule_nombre_points(self):
        valeurs = [self.ORDRE()[carte.valeur] for carte in self.cartes]
        points = [self.POINT()[carte.valeur] for carte in self.cartes]
        point = sum(points)
        if self.est_sequence() and 13 in valeurs:
            point += 10
        return point
