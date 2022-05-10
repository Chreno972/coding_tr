def pdt_nb_consecutifs(maxi):
    resultat = 1
    entiers = [n for n in range(2, maxi + 1, 2)]
    for n in entiers:
        resultat *= n
        print('%s : %s' % (n, resultat))
    return resultat

maxi = 10
prod = pdt_nb_consecutifs(10)

print("Le résultat du produit nombres entiers pairs de 2 à %s est de %s" % (maxi, prod))