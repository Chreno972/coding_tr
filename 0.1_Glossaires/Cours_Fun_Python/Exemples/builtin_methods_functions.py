

# affiche toutes les fonctions et méthodes built_in d'un objet Python
print(dir(str()))
la_phrase = "Bonjour"

# permet de créer une condition selon le contenu d'un string
if la_phrase.__contains__('our'):
    print("La phrase contient 'our'")

# __add__ => concaténation de chaine de caractères
print(la_phrase.__add__(" aussi"))

# __add__ => addition de chiffres
chiffres = 25
print(chiffres.__add__(5))

chiffres.__eq__(25)

# =======================================================================

class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate() 

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

# delattr ici consiste à supprimer une variable d'un objet
# delattr(Coordinate, 'z')
# ou
# Coordinate.__delattr__('z')
# ou même
# del Coordinate.z
# print('z = ', point1.z)

# =======================================================================

nums = 41
'{}'.format(nums)
print(str(nums.__format__('--')))
