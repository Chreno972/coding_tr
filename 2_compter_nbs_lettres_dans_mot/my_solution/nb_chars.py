
# !Chacune de ces fonctions doit comporter un docstring au format google qui
# !décrit les paramètres d'entrée, ce que fait la fonction et ce que renvoie la
# !fonction. le type retourné, les exceptions levées le cas échéant.
# !Créer une fonction nb_chars qui prend en parmètres: chaine de type (str) et
# !car de type (str) qui représente chaque lettre de chaine. Il retourne le
# !nombre d'occurences de car dans chaine.


def nb_chars(chaine, car):
    """
    Fonction qui compte le nombre de caractères dans une chaîne
    Paramètres:
    chaine: chaîne de caractères
    car: caractère à compter
    Retourne:
    nb: nombre de caractères
    """
    nb_characters = 0
    for i in chaine:
        if i == car:
            nb_characters += 1
    return nb_characters


print(nb_chars("hopooptooomne", "o"))
