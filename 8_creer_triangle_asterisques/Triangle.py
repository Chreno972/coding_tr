
def triangle():
    """Cette fonction crée une pyramide de triangles
    sur un maximum de 10 lignes

    Returns:
        str (une boucle de chaine de caractère
    """
    star = ""
    count = 0
    while count <= 10:
        star += "*"
        print(star)
        count += 1


triangle()
