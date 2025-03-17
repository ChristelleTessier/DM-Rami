"""Implémentation des tests pour la classe Combinaison."""
import re
import pytest
from carte import Carte
from combinaison import Combinaison

# Initialisation d'une combinaison
def test_init():
    """Test du constructeur de Combinaison."""
    c1 = Carte("As", "Pique")
    c2 = Carte("Roi", "Pique")
    c3 = Carte("Dame", "Pique")

    combi = Combinaison((c1, c2, c3))

    assert isinstance(combi, Combinaison)
    assert len(combi) == 3

    with pytest.raises(
        TypeError,
        match=re.escape("L'argument 'cartes' doit être un tuple de carte.")
        ):
        Combinaison([c1, c2, c3])
        # Doit lever une erreur (doit être un tuple)

    with pytest.raises(
        TypeError,
        match=re.escape("L'argument 'cartes' doit être un tuple de carte.")
        ):
        Combinaison(("As", "Pique"))
        # Doit lever une erreur (doit être un tuple)

    with pytest.raises(
        TypeError,
        match=re.escape("L'argument 'cartes' doit être un tuple de carte.")
        ):
        Combinaison((1,2,3))
        # Doit lever une erreur (éléments du tuple invalide)

# Vérification de la copie
def test_copie():
    """Test de la copie des cartes de la combinaison."""
    c1 = Carte("As", "Pique")
    c2 = Carte("Roi", "Pique")
    c3 = Carte("Dame", "Pique")

    combi = Combinaison((c1, c2, c3))
    cartes = combi.cartes

    assert cartes == (c1, c2, c3) # Valeurs et couleurs identiques
    assert cartes is not combi.cartes  # Doit être une copie profonde


# Egalité de deux combinaisons
def test_eq():
    """Test de l'égalité entre combinaisons."""
    c1 = Carte("As", "Pique")
    c2 = Carte("Roi", "Pique")
    c3 = Carte("Dame", "Pique")


    combi1 = Combinaison((c1, c2, c3))
    combi2 = Combinaison((c1, c2, c3))
    combi3 = Combinaison((c3, c2, c1))  # Ordre différent

    assert combi1 == combi2
    assert combi1 == combi3
    assert combi1 != "string"  # Comparaison avec un autre type


# Test affichage représentation officiel
@pytest.mark.parametrize(
    'values, resultat_attendu',
    [((pytest.as_coeur, pytest.as_trefle, pytest.as_carreau),
      "Combinaison(Carte(As,Coeur), Carte(As,Trêfle), Carte(As,Carreau))"),
     ((),"Combinaison()"),
      ]
)
def test_print(values, resultat_attendu):
    a = Combinaison(values)
    assert a.__repr__() == resultat_attendu


# Test affichage print
@pytest.mark.parametrize(
    'values, resultat_attendu',
    [((pytest.as_coeur, pytest.as_trefle, pytest.as_carreau),
      "(As de coeur, As de trêfle, As de carreau)"),
     ((),"()"),
      ]
)
def test_print(values, resultat_attendu):
    a = Combinaison(values)
    assert a.__str__() == resultat_attendu

# Test len
@pytest.mark.parametrize(
    'values, resultat_attendu',
    [((pytest.as_coeur, pytest.as_trefle, pytest.as_carreau),3),
     ((),0),
      ]
)
def test_print(values, resultat_attendu):
    a = Combinaison(values)
    assert a.__len__() == resultat_attendu


# Test de la détection d'un brelan
def test_est_brelan():

    # GIVEN
    c1 = Carte("As", "Pique")
    c2 = Carte("As", "Coeur")
    c3 = Carte("As", "Carreau")
    c4 = Carte("Roi", "Pique")
    c5 = Carte("As", "Pique")

    # WHEN
    combi_brelan = Combinaison((c1, c2, c3))
    combi_pas_brelan = Combinaison((c1, c2))  # Pas assez de carte
    combi_pas_brelan2 = Combinaison((c1, c2, c4))  # Une carte mauvaise valeur
    combi_pas_brelan3 = Combinaison((c1, c2, c5))  # Deux fois la même carte

    #THEN
    assert combi_brelan.est_brelan
    assert not combi_pas_brelan.est_brelan
    assert not combi_pas_brelan2.est_brelan 
    assert not combi_pas_brelan3.est_brelan


# Test de la détection d'un carré
def test_est_carre():

    # GIVEN
    c1 = Carte("As", "Pique")
    c2 = Carte("As", "Coeur")
    c3 = Carte("As", "Carreau")
    c4 = Carte("As", "Trêfle")
    c5 = Carte("Roi", "Pique")
    c6 = Carte("As", "Trêfle")

     # WHEN
    combi_carre = Combinaison((c1, c2, c3, c4))
    combi_pas_carre = Combinaison((c1, c2))  # Pas assez de carte
    combi_pas_carre2 = Combinaison((c1, c2, c3, c5)) # Une carte mauvaise valeur
    combi_pas_carre3 = Combinaison((c1, c2, c4, c6))  # Deux fois la même carte

    #THEN
    assert combi_carre.est_carre is True
    assert combi_pas_carre.est_carre is False
    assert combi_pas_carre2.est_carre is False
    assert combi_pas_carre3.est_carre is False

# Test de la détection d'une séquence
def test_est_sequence():

    #GIVEN
    c1 = Carte("Dame", "Pique")
    c2 = Carte("Roi", "Pique")
    c3 = Carte("As", "Pique")
    c4 = Carte("As", "Coeur")

    #WHEN
    combi_sequence = Combinaison((c1, c2, c3))
    combi_pas_sequence = Combinaison((c1, c2))  # Pas assez de carte
    combi_pas_sequence2 = Combinaison((c1, c2, c4))  # Couleurs différentes


    #THEN
    assert combi_pas_sequence.est_sequence() is False
    assert combi_pas_sequence2.est_sequence() is False
    assert combi_sequence.est_sequence() is True

# Test de la validation d'une combinaison.
def test_est_valide():

    #GIVEN
    c1 = Carte("As", "Pique")
    c2 = Carte("As", "Coeur")
    c3 = Carte("As", "Carreau")
    c4 = Carte("As", "Trêfle")
    c5 = Carte("Roi", "Pique")

    #WHEN
    combi_brelan = Combinaison((c1, c2, c3)) # Un brelan
    combi_carre = Combinaison((c1, c2, c3, c4)) # Un carré
    combi_invalide = Combinaison((c1, c2, c5))  # rien

    #THEN
    assert combi_brelan.est_valide() is True
    assert combi_carre.est_valide() is True
    assert combi_invalide.est_valide() is False

# Test du calcul des points d'une combinaison.
def test_calcule_nombre_points():

    #GIVEN
    c1 = Carte("As", "Pique")
    c2 = Carte("As", "Coeur")
    c3 = Carte("As", "Carreau")
    c4 = Carte("As", "Trêfle")
    c5 = Carte("Roi", "Pique")
    c6 = Carte("Dame", "Pique")
    c7 = Carte("2","Pique")
    c8 = Carte("3","Pique")

    #WHEN
    combi_brelan = Combinaison((c1, c2, c3))
    combi_carre = Combinaison((c1, c2, c3, c4))
    pas_combi = Combinaison((c1, c2))
    combi_suite_123 = Combinaison((c1, c7, c8))
    combi_suite_1RD = Combinaison((c1, c5, c6))


    #THEN
    assert combi_brelan.calcule_nombre_points() == 33  # Chaque As vaut 11
    assert combi_carre.calcule_nombre_points() == 44 # Chaque As vaut
    assert pas_combi.calcule_nombre_points() == 0 # Combi non valide
    assert combi_suite_123.calcule_nombre_points() == 6 # L'as vaut 1
    assert combi_suite_1RD.calcule_nombre_points() == 33 # As et les figures valent 11
