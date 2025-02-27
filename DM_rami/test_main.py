"""Implémentation des tests pour la classe Main"""

import re
import pytest
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
                                 Valeur_attendue_main,Valeur_attendue_reserve):
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
        [1, pytest.as_coeur,TypeError,
        "defausse représente la defausse de carte"],
        [1,(pytest.as_coeur),TypeError,
        "defausse représente la defausse de carte"]

    ],
)
def test_erreur_piocher(main, indice, defausse, type_erreur, message_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        main.jeter(indice,defausse)

# Test valeur
@pytest.fixture
def defausse():
    return Defausse([pytest.deux_coeur])

@pytest.mark.parametrize(
    "indice,Valeur_attendue_main,Valeur_attendue_defausse",
    [[0,Main([pytest.as_trefle,pytest.as_carreau]),
    Defausse([pytest.deux_coeur,pytest.as_coeur])],
    [1,Main([pytest.as_coeur,pytest.as_carreau]),
    Defausse([pytest.deux_coeur,pytest.as_trefle])],
    [2,Main([pytest.as_coeur,pytest.as_trefle]),
    Defausse([pytest.deux_coeur,pytest.as_carreau])],
    ],
)
def test_liste_cartes_jeter_resultat(main,defausse,indice,
                                 Valeur_attendue_main,Valeur_attendue_defausse):
    main.jeter(indice,defausse)
    assert main == Valeur_attendue_main
    assert defausse == Valeur_attendue_defausse

# Test poser
# Test erreur
@pytest.fixture
def main_pose():
    return Main([pytest.roi_coeur, pytest.roi_carreau, pytest.roi_trefle,
                  pytest.huit_coeur,pytest.neuf_coeur, pytest.dix_coeur])

# Test de type, et test de valeur sur les indices (valeur, pas de double)
# et combinaison(s) valident
@pytest.mark.parametrize(
    "indices_combinaison, premiere_pose, type_erreur, message_erreur",
    [
        [1,True,TypeError,"indices_combinaison doit être une liste de liste d'entier"],
        [[1,2],True,TypeError,
         "indices_combinaison doit être une liste de liste d'entier"],
        [[["a"]],True,TypeError,
         "les indices doivent être des nombres entiers compris entre 0 et 5"],
        [[[]],True,ValueError,
         "() n'est pas une combinaison valide"],
        [[[1,2,-1]],True,ValueError,
         "les indices doivent être des nombres entiers compris entre 0 et 5"],
        [[[1,2,10]],True,ValueError,
         "les indices doivent être des nombres entiers compris entre 0 et 5"],
        [[[1,2,3]],1,TypeError,
         "Premiere_pose doit être un booléen"],
        [[[1,2,1]],True,ValueError,
        "Tous les indices doivent être différent"],
        [[[0,1,3]],True,ValueError,
        "(Roi de coeur, Roi de carreau, 8 de coeur) n'est pas une combinaison valide"],
    ],
)
def test_erreur_poser(main_pose, indices_combinaison, premiere_pose,
                        type_erreur, message_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        main_pose.poser(indices_combinaison, premiere_pose)

# Pour 1er pose, Test de nombre de point et de presence de suite
@pytest.mark.parametrize(
    "main,indices_combinaison, type_erreur, message_erreur",
    [[Main([pytest.deux_coeur, pytest.deux_carreau, pytest.deux_trefle,
                  pytest.huit_coeur,pytest.neuf_coeur, pytest.dix_coeur]),
    [[0,1,2],[3,4,5]],ValueError,"Pour la 1ere pose il faut au moins 51 points pour poser"],
    [Main([pytest.roi_coeur, pytest.roi_carreau, pytest.roi_trefle,
                  pytest.huit_coeur,pytest.huit_carreau, pytest.huit_trefle]),
    [[0,1,2],[3,4,5]],ValueError,"Il n'y a pas de suite"],
    ],
)
def test_erreur_poser(main, indices_combinaison,
                        type_erreur, message_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        main.poser(indices_combinaison, True)

# Pour pose différente de 1er pose
@pytest.mark.parametrize(
    "main, indices_combinaison, type_erreur, message_erreur",
    [
        [Main([pytest.as_carreau,pytest.as_trefle,pytest.as_coeur,pytest.deux_carreau]),
        [[0,1,3]], ValueError,
        "(As de carreau, As de trêfle, 2 de carreau) n'est pas une combinaison valide"],
    ],
)
def test_erreur_poser(main, indices_combinaison,
                        type_erreur, message_erreur):
    with pytest.raises(type_erreur, match=re.escape(message_erreur)):
        main.poser(indices_combinaison, False)

# Test affichage
# Pour première pose
@pytest.mark.parametrize(
    "indice, Valeur_attendue_main, Valeur_attendue_comb_posee,Valeur_attendue_point",
    [
    [[[0,1,2],[3,4,5]], Main([]),
     [Combinaison((pytest.roi_coeur, pytest.roi_carreau, pytest.roi_trefle)),
      Combinaison((pytest.huit_coeur, pytest.neuf_coeur, pytest.dix_coeur))]
      ,60],
    ],
)
def test_poser_valide(main_pose, indice, Valeur_attendue_main, Valeur_attendue_comb_posee,
                      Valeur_attendue_point):
    pose, point = main_pose.poser(indice,True)
    assert main_pose == Valeur_attendue_main
    assert pose == Valeur_attendue_comb_posee
    assert point == Valeur_attendue_point

# Pour autre pose
@pytest.mark.parametrize(
    "main, indice, Valeur_attendue_main, Valeur_attendue_comb_posee,Valeur_attendue_point",
    [
    [Main([pytest.as_carreau,pytest.as_trefle,pytest.as_coeur,pytest.deux_carreau]),
        [[0,1,2]],Main([pytest.deux_carreau]),
        [Combinaison((pytest.as_carreau,pytest.as_trefle,pytest.as_coeur))], 33
    ],],
)
def test_poser_valide(main, indice, Valeur_attendue_main, Valeur_attendue_comb_posee,
                      Valeur_attendue_point):
    pose, point = main.poser(indice,False)
    assert main == Valeur_attendue_main
    assert pose == Valeur_attendue_comb_posee
    assert point == Valeur_attendue_point
