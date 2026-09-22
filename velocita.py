'''
Srivi un programma che:

Chiede all'utente la distanza percorsa (in km) e il tempo impiegato (in ore).
Calcola la velocità media
Stampa il risultato con due cifre decimali e indica l'unità di misura.

'''

distanza= input ("inserire la distanza in km")
distanza= float (distanza)
tempo= input ("inserire il tempo impiegato in ore")
tempo= int (tempo)
velocita= distanza/tempo
velocita= round (velocita,2)
print (velocita)