"""Le text slicing"""
# Il est possible comme pour les listes, de découper des chaines
# de caractères en plusieurs morceaux de longueur variable.

string_to_slice = 'Tours, Paris, Bordeaux'

print(string_to_slice[:3])
# de 0 à 3 exclu => Tou

print(string_to_slice[3:])
# de 3 inclus à la fin => rs, Paris, Bordeaux

print(string_to_slice[::2])
# de 0 à la fin par pas de 2 => Tus ai, Breu
# Revient à faire
print(string_to_slice[0:-1:2])

print(string_to_slice[-10: -7])
# pars du 10ème caractère à partir de la fin, jusqu'au 7ème à partir de la fin
# retourn , B

print(string_to_slice[::-2])
# parcours les éléments dans le sens inverse de 2 pas

print(string_to_slice[::-1])
