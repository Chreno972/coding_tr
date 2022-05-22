
def pdt_nb_consecutifs(maxi):
    """Fonction qui récupères un entier (int)
    et qui retourne chaque occurence d'une boucle
    'le produit de chaque chiffre de ce nombre entier'

    Args:
        maxi (int): Le nombre en entrée

    Returns:
        str: le produit de chaque chiffre du nombre
    """
    resultat = 1
    entiers = [n for n in range(2, maxi + 1, 2)]
    for n in entiers:
        resultat *= n
        print('%s : %s' % (n, resultat))
    return resultat


prod = pdt_nb_consecutifs(10)


print(
    "Le résultat du produit nombres entiers pairs de 2 à %s est de %s" % (maxi, prod)
)