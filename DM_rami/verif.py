# Question : doit-on faire un docstring plus complet pour les méthode des classes ?


from carte import Carte
from base import _ListeCartes
from combinaisonv2 import Combinaison

l1 = Combinaison((Carte("2","Pique"),Carte("Roi","Pique"),Carte("Dame","Pique")))
l2 = Combinaison((Carte("Roi","Pique"),Carte("2","Pique"),Carte("Dame","Pique")))
l1 = Combinaison(None)
l2 = Combinaison(None)
print(l1 == l2)
