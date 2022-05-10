def calcul_moyenne(notes):
    """Fonction qui récupère une liste et
    donne la moyenne de tous les chiffres de cette liste

    Args:
        notes (list): La liste des nombres

    Returns:
        int (la moyenne des chiffres)
    """
    total = 0
    for note in notes:
        total += note

    moyenne = total / len(notes)
    return "La moyenne de tous les chiffres est de {0:.nf}".format(moyenne)


print(calcul_moyenne([14, 9, 6, 8, 12, 40]))