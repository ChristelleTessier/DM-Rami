"""Implémentation des tests pour la classe Reserve."""
import pytest
from reserve import Reserve
from carte import Carte


def test_reserve_initialisation_vide():
    """Test de l'initialisation d'une réserve vide."""
    # GIVEN
    reserve = Reserve()
    # THEN
    assert len(reserve._cartes) == 0


def test_reserve_initialisation_avec_cartes():
    """Test de l'initialisation d'une réserve avec des cartes."""
    # GIVEN
    valeurs = [
        "As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Valet", "Dame", "Roi"
        ]
    couleurs = ["Pique", "Coeur", "Carreau", "Trêfle"]
    # WHEN
    cartes = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    reserve = Reserve(cartes)
    # THEN
    assert len(reserve._cartes) == len(cartes)


def test_melanger():
    """Test du mélange de la réserve."""
    # GIVEN
    valeurs = [
        "As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Valet", "Dame", "Roi"
        ]
    cartes = [Carte(valeur, 'Coeur') for valeur in valeurs]
    # WHEN
    reserve = Reserve(cartes.copy())
    reserve.melanger()
    # THEN
    assert set(reserve._cartes) == set(cartes)  # Même cartes mais ordre différent
    assert reserve._cartes != cartes


def test_distribuer():
    """Test de la distribution des cartes aux joueurs."""
    # GIVEN
    valeurs = [
        "As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Valet", "Dame", "Roi"
        ]
    couleurs = ["Pique", "Coeur", "Carreau", "Trêfle"]

    cartes = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]*2
    nb_joueur = 4
    idx_premier_joueur = 1
    n_cartes = "14/15"
    # WHEN
    reserve = Reserve(cartes)
    mains = reserve.distribuer(nb_joueur, idx_premier_joueur, n_cartes)
    # THEN
    assert len(mains) == nb_joueur
    assert len(mains[idx_premier_joueur]) == 15
    for i in range(1, nb_joueur):
        if i != idx_premier_joueur:
            assert len(mains[i]) == 14


def test_distribuer_erreur_nb_joueur():
    """Test de la gestion d'erreur pour un nombre de joueurs invalide."""
    # GIVEN
    valeurs = [
        "As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"
        ]
    couleurs = ["Pique", "Coeur", "Carreau", "Trêfle"]

    cartes = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    # WHEN
    reserve = Reserve(cartes)
    # THEN
    with pytest.raises(ValueError):
        reserve.distribuer(6, 0, "14/15")  # Trop de joueurs
    with pytest.raises(ValueError):
        reserve.distribuer(0, 0, "14/15")  # Trop peu de joueurs


def test_distribuer_erreur_idx_joueur():
    """Test de la gestion d'erreur pour un index de premier joueur invalide."""
    # GIVEN
    valeurs = [
        "As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Valet", "Dame", "Roi"
        ]
    couleurs = ["Pique", "Coeur", "Carreau", "Trêfle"]

    cartes = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    reserve = Reserve(cartes)
    # THEN
    with pytest.raises(ValueError):
        reserve.distribuer(3, -1, "14/15")  # Index négatif
    with pytest.raises(ValueError):
        reserve.distribuer(3, 3, "14/15")  # Index hors limites


def test_distribuer_erreur_n_cartes():
    """Test de la gestion d'erreur pour un format de cartes invalide."""
    # GIVEN
    valeurs = [
        "As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Valet", "Dame", "Roi"
        ]
    couleurs = ["Pique", "Coeur", "Carreau", "Trêfle"]

    cartes = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    reserve = Reserve(cartes)
    # THEN
    with pytest.raises(ValueError):
        reserve.distribuer(3, 0, "12/13")  # Format non autorisé
    with pytest.raises(TypeError):
        reserve.distribuer(3, 0, 14)  # Mauvais type pour n_cartes


def test_distribuer_erreur_cartes_insuffisantes():
    """Test de la gestion d'erreur quand il n'y a pas assez de cartes."""
    # GIVEN
    valeurs = [
        "As", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Valet", "Dame", "Roi"
        ]
    couleurs = ["Pique", "Coeur", "Carreau", "Trêfle"]
    # WHEN
    cartes = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    reserve = Reserve(cartes)
    # THEN
    with pytest.raises(ValueError):
        reserve.distribuer(4, 0, "14/15")  # Pas assez de cartes
