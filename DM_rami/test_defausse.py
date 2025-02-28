"""Implémentation des tests pour la classe Defausse."""
import pytest
import random
from defausse import Defausse
from carte import Carte
from base import _ListeCartes
from reserve import Reserve


def test_defausse_initialisation_vide():
    """Test de l'initialisation d'une défausse vide."""
    #GIVEN
    
    defausse = Defausse()
    
    #THEN
    assert len(defausse.cartes) == 0
    assert str(defausse) == "Défausse: []"

def test_defausse_initialisation_avec_cartes():
    """Test de l'initialisation d'une défausse avec des cartes."""
    #GIVEN
    cartes = [Carte("As", "Pique"), Carte("Roi", "Carreau")]
    #WHEN
    defausse = Defausse(cartes)
    #THEN
    assert len(defausse.cartes) == 2
    assert str(defausse).lower() == "défausse: [as de pique, roi de carreau]"

def test_vider_defausse_vide():
    """Test de la méthode vider() avec une défausse vide."""
    #GIVEN
    defausse = Defausse()
    reserve = Reserve()
    reserve = Reserve()
    #THEN
    assert defausse.vider(reserve) == False  # Rien à vider
    assert len(reserve.cartes) == 0
    assert len(defausse.cartes) == 0

def test_vider_defausse_non_vide():
    """Test de la méthode vider() avec une défausse contenant des cartes."""
    #GIVEN
    cartes = [Carte("As", "Pique"), Carte("Roi", "Coeur"), Carte("10", "Trêfle")]
    #WHEN
    defausse = Defausse(cartes)
    reserve = Reserve()

    # THEN
    assert len(defausse.cartes) == 3
    assert len(reserve.cartes) == 0

    # Vider la défausse dans la réserve
    assert defausse.vider(reserve) == True

    # Vérifier l'état après vidage
    assert len(defausse.cartes) == 0
    assert len(reserve.cartes) == 3  # Les cartes doivent être transférées

def test_vider_defausse_melange():
    """Test que les cartes sont bien mélangées avant d'être ajoutées à la réserve."""
    #GIVEN
    cartes = [Carte("As", "Pique"), Carte("Roi", "Coeur"), Carte("10", "Trêfle")]
    #WHEN
    defausse = Defausse(cartes.copy())  # Copie pour comparer plus tard
    reserve = Reserve()

    # Mélanger de façon prévisible avec un seed
    random.seed(42)
    defausse.vider(reserve)
    #THEN
    # Vérifier que les cartes ne sont pas dans le même ordre
    assert set(cartes) == set(reserve._cartes)  # Même cartes
    assert cartes != reserve._cartes  # Mais ordre différent
