from base import _ListeCartes
from carte import Carte
from defausse import Defausse
from reserve import Reserve

defausse = Defausse([Carte("2","Coeur"),Carte("3","Coeur"),Carte("4","Coeur"),Carte("5","Coeur"),Carte("6","Coeur")])

reserve = Reserve([])
defausse.vider(reserve)
