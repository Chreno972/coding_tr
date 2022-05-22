
a = 'sonIa BBellééçào2'

# 'capitalize', 'casefold', 'center', 'count', 'encode',
# 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind',
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# 'title', 'translate', 'upper', 'zfill'

# Alpha
print(a.capitalize())  # met majuscule en début de chaîne
print()
print(a.lower())  # met tout en minuscule
print()
print(a.count('o'))  # compte le nombre de 'o'
print()
print(a.endswith('o'))  # teste si la chaîne finit par 'o'
print()
print(a.find('o'))  # retourne la position du premier 'o'
print()
print(a.isalpha())  # teste si la chaîne est alphabétique
print()
print(a.islower())  # teste si la chaîne est en minuscule
print()
print(a.isupper())  # teste si la chaîne est en majuscule
print()
print(a.isprintable())  # teste si la chaîne est imprimable
print()
print(a.isspace())  # teste si la chaîne est un espace
print()
print(a.split('o'))  # coupe la chaîne à la position du o est crée une liste
# encode - decode
encd = a.encode()  # python code les caractères sous forme d'octets (bytes)
print(encd)
print()

encd = encd.decode('utf8').casefold()  # decode les octets en caractères
print(encd)
print()

la_liste = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

le_dictionnaire = {
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g',
    'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n',
}

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
# 'setdefault', 'update', 'values'

vara = 'a'
varb = 'b'
varc = 'c'
vard = 'd'
vare = 'e'
le_tuple = ( vara, varb, varc, vard, vare )

# 'count', 'index'
