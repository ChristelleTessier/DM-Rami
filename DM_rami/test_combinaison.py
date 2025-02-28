"""Implémentation des tests pour la classe Combinaison."""
import pytest
from carte import Carte
from combinaison import Combinaison


def test_init():
    """Test du constructeur de Combinaison."""
    c1 = Carte("As", "Pique")
    c2 = Carte("Roi", "Pique")
    c3 = Carte("Dame", "Pique")

    combi = Combinaison((c1, c2, c3))

    assert isinstance(combi, Combinaison)
    assert len(combi) == 3

    with pytest.raises(TypeError):
        Combinaison([c1, c2, c3])  # Doit lever une erreur (doit être un tuple)

    with pytest.raises(TypeError):
        Combinaison(("As", "Pique"))  # Doit lever une erreur (éléments invalides)


def test_eq():
    """Test de l'égalité entre combinaisons."""
    c1 = Carte("As", "Pique")
    c2 = Carte("Roi", "Pique")
    c3 = Carte("Dame", "Pique")
    

    combi1 = Combinaison((c1, c2, c3))
    combi2 = Combinaison((c1, c2, c3))
    combi3 = Combinaison((c3, c2, c1))  # Ordre différent

    assert combi1 == combi2
    assert combi1 != combi3
    assert combi1 != "string"  # Comparaison avec un autre type


def test_est_brelan():
    """Test de la détection d'un brelan."""
    # GIVEN
    c1 = Carte("As", "Pique")
    c2 = Carte("As", "Coeur")
    c3 = Carte("As", "Carreau")
    c4 = Carte("Roi", "Pique")
    c5 = Carte("As", "Pique")
    # WHEN
    combi_brelan = Combinaison((c1, c2, c3))
    combi_pas_brelan = Combinaison((c1, c2, c4))
    combi_pas_brelan2 = Combinaison((c1, c2, c5))
    
    #THEN
    assert combi_brelan.est_brelan() is True
    assert combi_pas_brelan.est_brelan() is False
    assert combi_pas_brelan2.est_brelan() is False


def test_est_carre():
        
    """Test de la détection d'un carré."""
    # GIVEN
    c1 = Carte("As", "Pique")
    c2 = Carte("As", "Coeur")
    c3 = Carte("As", "Carreau")
    c4 = Carte("As", "Trêfle")
    c5 = Carte("Roi", "Pique")
    c6 = Carte("As", "Trêfle")

     # WHEN
    combi_carre = Combinaison((c1, c2, c3, c4))   
    combi_pas_carre = Combinaison((c1, c2, c3, c5))
    combi_pas_carre2 = Combinaison((c1, c2, c4, c6))
    
    #THEN
    assert combi_carre.est_carre() is True
    assert combi_pas_carre.est_carre() is False
    assert combi_pas_carre2.est_carre() is False
    
def test_est_sequence():
    """Test de la détection d'une séquence."""
    #GIVEN
    c1 = Carte("Dame", "Pique")
    c2 = Carte("Roi", "Pique")
    c3 = Carte("As", "Pique")
    c4 = Carte("As", "Coeur")

    #WHEN
    combi_sequence = Combinaison((c1, c2, c3)) 
    combi_pas_sequence = Combinaison((c1, c2, c4))  # Couleurs différentes
    
    #THEN
    assert combi_pas_sequence.est_sequence() is False
    assert combi_sequence.est_sequence() is True


def test_est_valide():
    """Test de la validation d'une combinaison."""
    #GIVEN
    c1 = Carte("As", "Pique")
    c2 = Carte("As", "Coeur")
    c3 = Carte("As", "Carreau")
    c4 = Carte("As", "Trêfle")
    c5 = Carte("Roi", "Pique")

    #WHEN
    combi_brelan = Combinaison((c1, c2, c3))
    combi_carre = Combinaison((c1, c2, c3, c4))
    combi_invalide = Combinaison((c1, c2, c5))
    
    #THEN
    assert combi_brelan.est_valide() is True  
    assert combi_carre.est_valide() is True
    assert combi_invalide.est_valide() is False


def test_calcule_nombre_points():
    """Test du calcul des points d'une combinaison."""
    #GIVEN
    c1 = Carte("As", "Pique")
    c2 = Carte("As", "Coeur")
    c3 = Carte("As", "Carreau")
    c4 = Carte("As", "Trêfle")

    #WHEN
    combi_brelan = Combinaison((c1, c2, c3))
    combi_carre = Combinaison((c1, c2, c3, c4))
    
    #THEN
    assert combi_brelan.calcule_nombre_points() == 33  # Chaque As vaut 11
    assert combi_carre.calcule_nombre_points() == 44 # Chaque As vaut 11
