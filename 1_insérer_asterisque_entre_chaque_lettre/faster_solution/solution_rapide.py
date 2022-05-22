

# ! Utiliser .join() tout simplement


def star_between_letter(string):
    """Fonction qui ajoute un astérisque après chaque lettre
    d'une chaine de caractère.

    Args:
        string (str): la chaine de caractère donnée en entrée

    Returns:
        new_string (str): La nouvelle chaine de caractère générée en sortie
    """

    return '*'.join(string)


print(star_between_letter("Martin"))
