
# !Index_of
# !Créer une fonction index_of qui prend en paramètres: liste (list),
# !une liste de chaines de caractères et chaine (str) et qui retourne
# !la position de chaine dans liste, -1 si la chaine n'est pas présente.


def index_of(liste, chaine):
    """
    Fonction qui renvoie la position d'une chaine dans une liste
    Paramètres:
    liste: liste de chaines de caractères
    chaine: chaîne de caractères
    Retourne:
    index: position de la chaine
    """
    indexe = -1
    if not isinstance(chaine, str):
        raise Exception("le type de chaine doit être str, or le type entré est %s" % type(chaine))
    elif not isinstance(liste, list):
        raise Exception("le type de liste doit être list, or le type entré est de type %s" % type(liste))
    else:
        for x in range(len(liste)):
            if liste[x] == chaine:
                return x
    return indexe


print(index_of(["hop", "oop", "tooomne"], "tooomne"))
# print(index_of(["hop", "oop", "tooomne"], "lodsf"))
# print(index_of(["hop", "oop", "tooomne"], 1))
# print(index_of(4, "lodsf"))
