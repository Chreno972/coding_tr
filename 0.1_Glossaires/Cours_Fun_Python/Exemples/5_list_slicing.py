"""List slicing"""
# Il est possible de sélectionner un sous-ensemble d'éléments d'une liste
# grâce au list slicing.

a = ['2', '9', 'blah', True, 52, 'Yes', 5.26]

# remplace les élément 9 et blah situés 1 et 3
a[1:4] = ['ajout1', 'ajout2', 100]

print(a)
# ['2', 'ajout1', 'ajout2', 100, 52, 'Yes', 5.26]


# Ici, on souhaite effacer l'élément à l'index 0
# afin de pouvoir afficher la liste sans cet élément.
new_liste = [8, 1, 2, 3]

suivant = new_liste.pop(0)

print(new_liste)
# en plus d'enlever l'index 0 de la liste, la nouvelle variable suivant
# récupère la référence de l'objet enlevée [1, 2, 3]
