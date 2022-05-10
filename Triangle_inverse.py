def triangle_inverse(nb_lignes):
    nb_colonnes = nb_lignes
    for ligne in range(1, nb_lignes + 1):
        for colonne in range(1, nb_colonnes + 1):
            position = nb_colonnes - ligne + 1
            if colonne <= position:
                print('*', end='')
            else:
                print(' ', end='')
        print('')

triangle_inverse(10)