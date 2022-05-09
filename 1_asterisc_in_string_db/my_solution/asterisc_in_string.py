
# Écrivez un script qui recopie une chaîne (dans une nouvelle variable),
# en insérant des astérisques entre les caractères.
# Par exemple, « gaston » devra devenir « g*a*s*t*o*n »


def star_between_letter(string):
    """Fonction qui ajoute un astérisque après chaque lettre
    d'une chaine de caractère.

    Args:
        string (str): la chaine de caractère donnée en entrée

    Returns:
        new_string (str): La nouvelle chaine de caractère générée en sortie
    """
    new_string = ""
    for letter in string:
        letter = letter + "*"
        new_string += letter
    return new_string


print(star_between_letter("Martin"))
