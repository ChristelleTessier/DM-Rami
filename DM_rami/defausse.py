from base import _ListeCartes


class Defausse(_ListeCartes):
    """Initialise la défausse.

    La classe Defausse permet de modéliser la défausse,
    c’est-à-dire la liste des cartes jetées.


    Attributes
    ----------
    __cartes (list[Carte]) : La liste des cartes dans la défausse.


    Raises (Hérité de _ListeCartes)
    ------
    TypeError : L'argument 'cartes' doit être une liste.
    """

    def __init__(self, cartes=None):
        """ Constructeur de la classe Defausse."""
        # Initialise avec une liste vide si aucun paramètre n'est donné
        if cartes is None:
            cartes = []
        elif not isinstance(cartes, list):
            raise ValueError("L'argument 'cartes' doit être une liste.")
        super().__init__(cartes)  # Appelle le constructeur de _ListeCartes

    def vider(self, reserve):
        """Vide la défausse et transfère les cartes dans la réserve.

        Attributes
        ----------
        reserve(list[Carte]) : La liste des cartes dans la défausse.

        Examples :
        ---------
        >>> defausse = Defausse([Carte("As","Coeur"), Carte("6","Pique")])
        >>> reserve = Reserve([])
        >>> defausse.vider(reserve)
        >>> print(len(defausse))
        0
        >>> print(len(reserve))
        2
        """
        if not self.cartes:
            # Vérifie si la défausse est vide
            return False

        self.melanger()
        for carte in self.cartes[:]:
            # Copie pour éviter les modifications pendant l'itération
            reserve.ajouter_carte(carte)

        self.reinitialiser()  # Vider la défausse

        return True

    def reinitialiser(self):
        """ Reinitialise la défausse.

        Supprime toutes les cartes de la défausse et les remet à zéro.

        Examples :
        ---------
        >>> defausse = Defausse([Carte("As","Coeur"), Carte("6","Pique")])
        >>> defausse.reinitialiser()
        >>> print(len(defausse))
        0
        """
        if isinstance(self.cartes, list):
            self._ListeCartes__cartes.clear()
        else:
            print("Attention: self.cartes n'est pas une liste mutable !")

    def __str__(self):
        """Affichage de la défausse sous forme de chaîne.

        Returns:
        -------
            str : Chaîne de caractères représentant la défausse.

        Examples:
        ----------
        >>> defausse = Defausse([Carte("10","Coeur"), Carte("6","Pique")])
        >>> print(defausse)
        Défausse: [10 de coeur, 6 de pique]
        """
        return f"Défausse: [{', '.join(str(carte) for carte in self.cartes)}]"
