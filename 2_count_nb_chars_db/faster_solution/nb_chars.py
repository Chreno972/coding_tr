
# ! Utiliser tout simplement count()


def nb_chars(chaine, car):
    """
    Fonction qui compte le nombre de caractères dans une chaîne
    Paramètres:
    chaine: chaîne de caractères
    car: caractère à compter
    Retourne:
    nb: nombre de caractères
    """

    return chaine.count(car)


print(nb_chars("hopooptooomne", "o"))
