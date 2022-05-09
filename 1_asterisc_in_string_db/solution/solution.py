
def solution_auteur(chaine_car):
    """script qui insert un astérisque entre chaque caractère
    d'une chaine de caractère.

    Args:
        chaine_car (str): chaine fournie en entrée
    """

    # Caractère à insérer :
    star = "*"
    # Le nombre de caractères à insérer est inférieur d'une unité au
    # nombre de caractères de la chaîne. On traitera donc celle-ci à
    # partir de son second caractère (en omettant le premier).

    # nombre de caractères total
    length_cc = len(chaine_car)

    # indice du premier caractère à examiner (le second, en fait)
    i = 1

    # nouvelle chaîne à construire (contient déjà le premier caractère)
    nouvelle_chaine = chaine_car[0]

    while i < length_cc:
        nouvelle_chaine = nouvelle_chaine + star + chaine_car[i]
        i = i + 1

    return nouvelle_chaine

# Affichage :


print(solution_auteur("véronique"))
