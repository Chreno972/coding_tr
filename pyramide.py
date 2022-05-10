import math


def pyramide(nb_lignes):
    nb_colonnes = nb_lignes * 2 + 1
    milieu = math.floor(nb_colonnes / 2 ) + 1
    pos_etoile_1 = milieu
    pos_etoile_2 = milieu
    print(milieu)
    for ligne in range(1, nb_lignes + 1):
        for colonne in range(1, nb_colonnes + 1):
            #position = nb_colonnes - ligne + 1
            if colonne < pos_etoile_1 or colonne > pos_etoile_2:
                print('-', end='')
            else:
                print('*', end='')
        pos_etoile_1 -= 1
        pos_etoile_2 += 1
        print('')

pyramide(11)