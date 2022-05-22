"""Insert et append et extend"""

# ici, on cherche à transformer 0123 en 01423
liste = [0, 1, 2, 3]

# insert permet d'ajouter un élément à un index précis sans
# pour autant effacer celui qui était à cet index, ce qui
# déplace l'ancien élément sur la droite.
liste.insert(2, 4)
print(liste)

# Ici, append permet d'ajouter un élément à la fin de la liste
# sans effacer l'élément qui était à la fin de la liste.
liste.append('ajout')
print(liste)

# Ici extend permet d'ajouter une liste à la fin de la liste
# sans effacer l'élément qui était à la fin de la liste.
liste.extend([5, 6, 7, 8])
print(liste)
