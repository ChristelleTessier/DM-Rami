"""Implémentation des tests pour la classe Carte."""
import re
import pytest
from carte import Carte

# Test sur la classe Carte
# Test d'erreur
@pytest.mark.parametrize(
    'values,type_erreur, message_erreur',
    [((1,"P"),TypeError,f"Le type de la valeur : 1 n'est pas correct"),
     (("1",1),TypeError,f"Le type de la couleur : 1 n'est pas correct"),
     (("11","Carreau"),ValueError,f"La valeur 11 n'est pas correcte"),
     (("10","careau"),ValueError,f"La couleur careau n'est pas correcte"),
     ]
)
def test_erreur_carte(values, type_erreur, message_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        Carte(*values)

# Validité de création carte
@pytest.mark.parametrize(
    "valeur, couleur, expected_result",
    [('2', 'Pique', True),   # Cas OK : carte valide
    ]
)

def test_carte_valide(valeur, couleur, expected_result):
    # WHEN: Création de la carte
    resultat = Carte(valeur, couleur)

    # THEN: Vérification des valeurs
    assert resultat.valeur == valeur
    assert resultat.couleur == couleur

# Test affichage représentation officiel
@pytest.mark.parametrize(
    'values, resultat_attendu',
    [(("As","Trêfle"),"Carte(\"As\",\"Trêfle\")"),
     (("2","Pique"),"Carte(\"2\",\"Pique\")"),]
)
def test_print(values, resultat_attendu):
    a = Carte(*values)
    assert a.__repr__() == resultat_attendu


# Test affichage print
@pytest.mark.parametrize(
    'values, resultat_attendu',
    [(("As","Trêfle"),"As de trêfle"),
     (("2","Pique"),"2 de pique"),]
)
def test_print(values, resultat_attendu):
    a = Carte(*values)
    assert a.__str__() == resultat_attendu

# Test egalité
def test_egalite_true():
    # GIVEN
    carte1 = Carte('2', 'Coeur')
    carte2 = Carte('2', 'Coeur')

    # WHEN
    equality = carte1 == carte2

    # THEN
    assert equality is True

def test_egalite_false():
    # GIVEN
    carte1 = Carte('2', 'Coeur')
    carte2 = Carte('As', 'Coeur')

    # WHEN
    equality = carte1 == carte2

    # THEN
    assert equality is False

# Test hash_carte
def test_hash_carte():
    # GIVEN : Création de cartes identiques et différentes
    carte1 = Carte('2', 'Coeur')
    carte2 = Carte('2', 'Coeur')  # Identique à carte1
    carte3 = Carte('Roi', 'Coeur')  # Différente

    # WHEN : Calcul des hash
    hash1 = hash(carte1)
    hash2 = hash(carte2)
    hash3 = hash(carte3)

    # THEN : Vérifications
    assert isinstance(hash1, int)  # Vérifier que c'est bien un entier
    assert hash1 == hash2  # Deux cartes identiques doivent avoir le même hash
    assert hash1 != hash3  # Deux cartes différentes doivent avoir un hash différent
