# Question :
# 1. doit-on faire un docstring plus complet pour les méthode des classes ?
# 2. Pour moi l'attribut par défaut de reserve est None et pas une liste vide - qu'en
# penses-tu ?
# 3. A modifier : integrer le type dans la definition de chaque méthode (nomvar : type)
# 4. nombre de cartes a distribuer, je ne comprends pas "13/14"

from carte import Carte
from base import _ListeCartes
from combinaisonv3 import Combinaison
from reserve import Reserve

#l1 = Combinaison((Carte("2","Pique"),Carte("Roi","Pique"),Carte("Dame","Pique")))
#l2 = Combinaison((Carte("Roi","Pique"),Carte("2","Pique"),Carte("Dame","Pique")))
#print(l1 == l2)


res = Reserve()
res.melanger()

mains = res.distribuer(3,2)
print(mains[0])
print(mains[1])
print(mains[2])

#l1= Combinaison(tuple())
#l2 = Combinaison(tuple())
#print(l1 == l2)

#print(isinstance(tuple(), tuple))
