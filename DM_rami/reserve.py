"""Implémentation de la classe Reserve."""


from base import _ListeCartes
from carte import Carte

class Reserve(_ListeCartes):
    """Représente une réserve de cartes.

    Cette classe hérite de _ListeCartes et représente la reserve de cartes (pioche) du
    jeu de rami, c'est-à-dire l'ensemble des cartes qui peuvent être piochées ou
    distribuées aux joueurs.

    Elle récupère les méthodes héritées de _ListeCartes
     - afficher une liste de carte (print).
     - calculer la longueur d'une liste de carte
     - mélanger une liste de carte.
     - ajouter une carte à une liste de carte.
     - retiter une carte d'une liste de carte.

    Elle propose une fonctionnalité supplémentaire pour :
     - distribuer les cartes aux joueurs en début de partie.

    Attributes
    ----------
        __cartes (list[Carte]) : La liste des cartes dans la reserve.

    Raises (Hérité de _ListeCartes)
    ------
        TypeError
            Si l'argument cartes n'est pas une liste ou qu'un élement de la liste n'est
            pas une instance de Carte.
    """

    def __init__(self, cartes = None):
        """ Constructeur """
        super().__init__(cartes) # Utiliser le constructeur de la classe mère (_ListeCartes)
        self._cartes = cartes if cartes is not None else []

    def distribuer(self, nb_joueur, idx_premier_joueur, n_cartes = "14/15"):
        """Distribue les cartes aux joueurs.

        Cette méthode distribue un nombre spécifique de cartes à chaque joueur,
        en commençant par un joueur désigné. Une carte supplémentaire est donnée
        au joueur qui distribue.

        Parameters
        ----------
            nb_joueur (int): Le nombre de joueurs participants. Doit être un entier
                positif entre 1 et 5.
            idx_premier_joueur (int): L'indice du joueur qui commence la distribution.
                Doit être un entier positif entre 0 et nb_joueur - 1.
            n_cartes (str, optional): Une chaîne de caractères au format
                "nombre_cartes/nombre_cartes_supplementaire". Définit le nombre de
                cartes à distribuer à chaque joueur et le nombre de cartes
                supplémentaires pour le distributeur. Par défaut, "14/15".

        Returns
        -------
            list[Main]: Une liste de Main correspondant aux mains des joueurs
            (chaque élément est une liste de cartes). L'ordre des mains dans
            la liste est déterminé par l'indice du premier joueur.

        Raises
        ------
            TypeError: Si nb_joueur ou idx_premier_joueur ne sont pas des entiers,
                ou si n_cartes n'est pas une chaîne de caractères.
            ValueError: Si nb_joueur n'est pas entre 1 et 5, si idx_premier_joueur
                n'est pas entre 0 et nb_joueur - 1, si n_cartes n'est pas "13/14"
                ou "14/15", ou s'il n'y a pas assez de cartes dans le paquet
                pour la distribution.
        """
        if not isinstance(nb_joueur, int):
            raise TypeError(f"Le nombre de joueur est un entier positif compris entre "
                           f"1 et 5, la valeur {nb_joueur} n'est pas correct")
        if nb_joueur < 1 or nb_joueur > 5:
            raise ValueError(f"Le nombre de joueur est un entier positif compris entre "
                           f"1 et 5, la valeur {nb_joueur} n'est pas correct")
        if not isinstance(idx_premier_joueur,int):
            raise TypeError(f"L'indice du premier joueur est compris entre 0 et "
                           f"{nb_joueur}, la valeur {idx_premier_joueur} n'est "
                           "pas correct")
        if idx_premier_joueur < 0 or idx_premier_joueur >= nb_joueur:
            raise ValueError(f"L'indice du premier joueur est compris entre 0 et "
                           f"{nb_joueur}, la valeur {idx_premier_joueur} n'est "
                           "pas correct")
        if not isinstance(n_cartes,str):
            raise TypeError("La valeur n_cartes est la chaine de caractère : "
                            "\"13/14\" ou \"14/15\"")
        if n_cartes != "13/14" and n_cartes != "14/15":
            raise ValueError("La valeur n_cartes est la chaine de caractère : "
                            "\"13/14\" ou \"14/15\"")
        # recuperation du nombre de carte à distribuer
        nombre_cartes, nombre_cartes_supp = map(int, n_cartes.split("/"))


        # Verification du nombre de carte disponible
        n_carte_need = nombre_cartes * nb_joueur + 1
        if n_carte_need > len(self):
            raise ValueError("Il n'y a pas assez de carte dans le paquet")

        noms_main = []
        for i in range(nb_joueur):
            nom = 'main' + str(i)
            noms_main.append(nom)

        # Initialisation des mains comme une liste de listes vides
        mains = [[] for _ in range(nb_joueur)]

        # liste_main = [_ListeCartes([])]*nb_joueur renvoie nb_joueur fois la même liste

        # Remplissage des mains
        for i in range(nombre_cartes):
            for j in range(nb_joueur):
                index_joueur = (idx_premier_joueur + j) % nb_joueur
                carte = self.retirer_carte(len(self) - 1)
                mains[index_joueur].append(carte)

        # Distribution des cartes supplémentaires au distributeur

        carte = self.retirer_carte(len(self) - 1)
        mains[idx_premier_joueur].append(carte)
        return mains
