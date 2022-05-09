
# !filtre dicts
# !Créer une fonction filtre_dicts qui prend en paramètres: liste (list)
# !une liste de dictionnaires, champ (str), le nom du champ, dans lequel
# !on souhaite rechercher et valeur(str). La fonction doit rechercher dans
# !la liste de dictionnaires et retourner une liste de tous les dictionnaires
# !et retourner une liste de tous les dictionnaires dont le champ 'champ'
# !est égal à 'valeur'.


def filtre_dicts(liste, champ, valeur):
    """
    Fonction qui renvoie les dictionnaires de la liste qui contiennent une
    valeur
    Paramètres:
    liste (list): liste de dictionnaires
    champ (str): nom du champ
    valeur (dict): valeur à rechercher
    Retourne:
    liste (list): liste de dictionnaires
    """
    liste_filtree = []
    for i in liste:
        if i[champ] == valeur:
            liste_filtree.append(i)
    return liste_filtree


print(filtre_dicts(
    [
        {"nom": "jean","age": 70},
        {"nom": "jean", "age": 20},
        {"nom": "jean", "age": 80},
        {"nom": "jean", "age": 20},
        {"nom": "jean", "age": 60},
        {"nom": "jean", "age": 20}
    ],
    "age", 20
    ))
