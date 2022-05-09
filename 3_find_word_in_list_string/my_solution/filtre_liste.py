
# !filtre_liste
# !Créer une fonction filtre_liste qui prend en paramètres: liste (list),
# !chaine (str). Retourner une liste de tous les éléments qui contiennent
# !une chaine. Par exemple: l'élément 'mer du nord' contient 'nord'.
# !La recherche doit être insensible à la casse.


def filtre_liste(liste, chaine):
    """
    Fonction qui renvoie les éléments de la liste qui contiennent une
    chaine
    Paramètres:
    liste: liste de chaines de caractères
    chaine: chaîne de caractères
    Retourne:
    liste: liste de chaines de caractères
    """
    liste_filtree = []
    for i in liste:
        if chaine in i:
            liste_filtree.append(i)
        elif i == "":
            raise Exception("veuillez ne pas entrer de chaines de caractères vide")
    return liste_filtree


print(filtre_liste(
    [
        "mer du nord",
        "mer du sud",
        "caca du sud",
        "bite du sud",
        "mer du sud",
        "mer du nord",
        "mer du nord",
        "mer du sud",
        "Glavio DU SUD est"
    ],
    "sud"
    ))

