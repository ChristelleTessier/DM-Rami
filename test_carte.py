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
