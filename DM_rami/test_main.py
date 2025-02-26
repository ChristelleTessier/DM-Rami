"""Implémentation des tests pour la classe Main"""

import re
import pytest
from carte import Carte
from base import _ListeCartes
from reserve import Reserve
from defausse import Defausse
from combinaison import Combinaison
from main import Main


# Test sur la classe Main
# Test d'erreur
@pytest.mark.parametrize(
    "param",
    [
        pytest.as_coeur,
        (pytest.as_coeur, pytest.six_pique),
        {pytest.as_coeur, pytest.six_pique},
        {pytest.as_coeur: 1, pytest.six_pique: 2},
        ["As de coeur", "3 de trêfle"],
        ["As de coeur", pytest.as_coeur],
    ],
)
def test_liste_cartes_init_echec(param):
    with pytest.raises(
        ValueError, match="L'argument 'cartes' doit être None ou une liste de cartes."
    ):
        Main(param)


# Test affichage -> déjà fait dans _ListeCartes

# Test égalité
@pytest.mark.parametrize(
    "main1, main2, Valeur_attendue",
    [
        ([],[],True),
        ([pytest.as_coeur,pytest.as_trefle,pytest.as_carreau],
        [pytest.as_coeur,pytest.as_trefle,pytest.as_carreau],True),
        ([pytest.as_trefle,pytest.as_coeur,pytest.as_carreau],
        [pytest.as_coeur,pytest.as_trefle,pytest.as_carreau],True),
        ([pytest.deux_trefle,pytest.as_coeur,pytest.as_carreau],
        [pytest.as_coeur,pytest.as_trefle,pytest.as_carreau],False),
        ([pytest.as_trefle,pytest.as_coeur,pytest.as_carreau],
        [pytest.as_coeur,pytest.as_trefle],False),
    ],
)
def test_liste_cartes_init_echec(main1, main2, Valeur_attendue):
    assert (Main(main1)==Main(main2)) == Valeur_attendue

# Test piocher
@pytest.fixture
def main():
    return Main([pytest.as_coeur,pytest.as_trefle,pytest.as_carreau])

# Test erreur
@pytest.mark.parametrize(
    "reserve, type_erreur, message_erreur",
    [
        ["1",TypeError,"reserve représente la reserve de carte"],
        [0,TypeError,"reserve représente la reserve de carte"],
        [pytest.deux_pique,TypeError,"reserve représente la reserve de carte"],
        [(pytest.deux_pique),TypeError,"reserve représente la reserve de carte"],
        [True,TypeError,"reserve représente la reserve de carte"],
    ],
)
def test_erreur_piocher(main, reserve, type_erreur, message_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        main.piocher(reserve)

# Test resultat
@pytest.fixture
def reserve():
    return Reserve([pytest.deux_coeur,pytest.roi_trefle,pytest.cinq_carreau])

@pytest.mark.parametrize(
    "Valeur_attendue_main,Valeur_attendue_reserve",
    [[Main([pytest.as_coeur,pytest.as_trefle,pytest.as_carreau,pytest.cinq_carreau]),
    Reserve([pytest.deux_coeur,pytest.roi_trefle])],
    ],
)
def test_liste_cartes_piocher_resultat(main,reserve,
                                 Valeur_attendue_reserve,Valeur_attendue_main):
    main.piocher(reserve)
    assert main == Valeur_attendue_main
    assert reserve == Valeur_attendue_reserve

# Test jeter
# Test erreur
@pytest.mark.parametrize(
    "indice, defausse, type_erreur, message_erreur",
    [
        ["1",Defausse([]),TypeError,
         "Indice doit etre un entier compris entre 0 et 2"],
        [-1,Defausse([]),ValueError,
         "Indice doit etre un entier compris entre 0 et 2"],
        [5,Defausse([]),ValueError,
         "Indice doit etre un entier compris entre 0 et 2"],
    ],
)
def test_erreur_piocher(main, indice, defausse, type_erreur, message_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        main.jeter(indice,defausse)
