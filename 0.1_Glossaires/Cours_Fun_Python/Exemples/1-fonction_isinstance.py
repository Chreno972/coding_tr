"""La fonction isinstance"""


class Homme:
    """crée une classe Homme
    qui possède deux attributs:
    nom et prenom
    
    nom = str
    prenom = str
    """
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        """Methode __str__

        Returns:
            str: la concaténation de Nom et Prénom
        """
        return f'{self.nom} - {self.prenom}'


chris = Homme('Reno', 'Christophe')

print(chris.nom)
print(chris.__str__())
# la fonction isinstance() retourne True 
# si l'argument ou objet chris fait partie de l'instance de la classe homme
print(isinstance(chris, Homme))

# sachant que tout élément est un objet dans Python, 
# 23 est considéré comme une instance de la classe int
# "salut" est considéré comme une instance de la classe str...
print(f'is 23 an instance of Python int (integer) object ? {isinstance(23, int)}')
print(f'is 34 an instance of Python str (string) object ? {isinstance(34, str)}')
print(f'is "salut" an instance of Python str (string) object ? {isinstance("salut", str)}')
