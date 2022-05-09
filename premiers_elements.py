
# !premiers_elements
# !Créer une fonction premiers_elements qui prend en parmètre: liste (list)
# !une liste de types quelconques, nb (int). La fonction doit retourner les
# !nb premiers éléments de la liste. Gérer les cas d'erreur, par exemple nb
# !supérieur à la longueur de la liste. retourner toute la liste,
# !nb < 1 lever une exception.


def premiers_elements(liste, nb_elements):
    """
    Fonction qui renvoie les n premiers éléments d'une liste
    Paramètres:
    liste: liste de types quelconques
    nb: nombre de premiers éléments
    Retourne:
    liste: liste de n premiers éléments
    """
    if nb_elements < 1:
        raise Exception(
            "Le nombre des premiers éléments doit être supérieur à 1"
            )
    elif nb_elements > len(liste):
        return liste
    else:
        return liste[:nb_elements]


print(premiers_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))