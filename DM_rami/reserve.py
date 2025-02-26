"""Implémentation de la classe Reserve."""


from base import _ListeCartes
from carte import Carte

class Reserve(_ListeCartes):
    """
    Représente une réserve de cartes, héritant des fonctionnalités de _ListeCartes.

    Cette classe étend _ListeCartes pour fournir une représentation d'une réserve
    de cartes, avec des fonctionnalités supplémentaires telles que la distribution
    de cartes aux joueurs.

    Attributes
    ----------
    cartes : list of Carte, optional
        Liste initiale de cartes dans la réserve.
        Par défaut, None (pour construire réserve à 2*52 cartes).

    Methods
    -------
    distribuer(nb_joueur : int, idx_premier_joueur : int, n_cartes="14/15" : str)
        Distribue les cartes aux joueurs à partir de la réserve, en commençant par
        idx_premier_joueur.
    """

    def __init__(self, cartes = None):
        """ COnstructeur """
        super().__init__(cartes) # Utiliser le constreur de la classe mère (_ListeCartes)
        self.__cartes = cartes

    def distribuer(self, nb_joueur, idx_premier_joueur, n_cartes = "14/15"):
        """
        Distribue les cartes aux joueurs.

        Cette méthode distribue un nombre spécifique de cartes à chaque joueur,
        en commençant par un joueur désigné. Une carte supplémentaire est donnée
        au joueur qui distribue.

        Parameters
        ----------
        nb_joueur : int
            Le nombre de joueurs participants. Doit être un entier positif entre 1 et 5.
        idx_premier_joueur : int
            L'indice du joueur qui commence la distribution. Doit être un entier
            positif entre 0 et nb_joueur - 1.
        n_cartes : str, optional
            Une chaîne de caractères au format "nombre_cartes/nombre_cartes_supplementaire".
            Définit le nombre de cartes à distribuer à chaque joueur et le nombre
            de cartes supplémentaires pour le distributeur. Par défaut, "14/15".

        Returns
        -------
        list of _ListeCartes
            Une liste de mains de cartes, où chaque élément est une instance de
            _ListeCartes représentant la main d'un joueur. L'ordre des mains dans
            la liste est déterminé par l'indice du premier joueur.

        Raises
        ------
        TypeError
            Si nb_joueur ou idx_premier_joueur ne sont pas des entiers, ou si
            n_cartes n'est pas une chaîne de caractères.
        ValueError
            Si nb_joueur n'est pas entre 1 et 5, si idx_premier_joueur n'est pas
            entre 0 et nb_joueur - 1, si n_cartes n'est pas "13/14" ou "14/15", ou
            s'il n'y a pas assez de cartes dans le paquet pour la distribution.
        """
        if not isinstance(nb_joueur, int):
            raise TypeError(f"Le nombre de joueur est un entier positif compris entre "
                           f"1 et 5, la valeur {nb_joueur} n'est pas correct")
        if nb_joueur < 0 or nb_joueur > 5:
            raise ValueError(f"Le nombre de joueur est un entier positif compris entre "
                           f"1 et 5, la valeur {nb_joueur} n'est pas correct")
        if not isinstance(idx_premier_joueur,int):
            raise TypeError(f"L'indice du premier joueur est compris entre 0 et "
                           f"{nb_joueur}, la valeur {idx_premier_joueur} n'est "
                           "pas correct")
        if idx_premier_joueur < 0 or idx_premier_joueur > nb_joueur:
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
        nombres = n_cartes.split("/")
        nombre_cartes = int(nombres[0])

        # Verification du nombre de carte disponible
        n_carte_need = nombre_cartes * nb_joueur + 1
        if n_carte_need > len(self):
            raise ValueError("Il n'y a pas assez de carte dans le paquet")

        noms_main = []
        for i in range(nb_joueur):
            nom = 'main' + str(i)
            noms_main.append(nom)

        # Initialisation
        liste_main = [_ListeCartes([]) for _ in range(nb_joueur)]
        # liste_main = [_ListeCartes([])]*nb_joeur renvoie nb_joueur fois la même liste

        # Remplissage des mains
        for i in range(nombre_cartes):
            for main in liste_main:
                main.ajouter_carte(self.retirer_carte(len(self)-1))

        #Ajouter la carte supplementaire à celui qui distribue)
        liste_main[0].ajouter_carte(self.retirer_carte(len(self)-1))

        # Rearangement de l'ordre des cartes en fonction de idx_premier_joeur
        result = [tuple()]*nb_joueur
        for i in range(nb_joueur):
            result[(i + idx_premier_joueur) % nb_joueur]=liste_main[i]

        return result
