# Aides compréhension

## Imports

tout d'abord on importe django afin de pouvoir utiliser toutes ses
fonctionnalités, ainsi que les autres modules dont on a besoin

```python
# Import de django pour utiliser ses fonctionnalités
import django

# on définit le module de settings comme étant le settings du projet consolidation
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consolidation.settings')

# on utilise la méthode setup de django
django.setup()

# On importe le module Q de django.db.models, afin de concatèner plusieurs filtres
from django.db.models import Q

# On importe le module os afin de pouvoir manipuler les directories et folders
import os

# On importe la classe LdapUser du modèle du dossier external_writings
from external_writings.models import LdapUser

# On importe la classe import_ldap_accounts du modèle utils du dossier models
# lui même contenu dans le dossier group
from group.models.utils import import_ldap_accounts

# On importe la classe User du modèle models contenu dans le dossier group
from group.models import User

# On importe la classe RunPart du modèle models contenu dans le dossier models
# Lui même contenu dans le dossier group
from group.models.models import RunPart

# On importe la classe Agency du modèle models contenu dans le dossier group
from group.models import Agency
```

---
---

## Les grosses requêtes

Après avoir effectué tous les imports nécessaires à la création des requêtes
nécessaires à mon entrainement.

```python
class Employee(models.Models):
    most_current_situation = models.etc
    agency = models.ForeignKey
    ...

class Agency(models.Models):
    employe = models.ForeignKey(...)
    ...
    
    def agency_employees(self):
        return employe.dont(most_current_situation)
"""
La classe Agency importée plus haut, grâce au setattr, récupère une méthode agency_employees
Cette méthode retourne tous les users dont l'attribut most_current_situation appartient à
une agence spécifique
"""
def agency_employees(self):
    return User.objects.filter(most_current_situation__agency=self).distinct()

"""
Description => setattr(objet, nom_de_la_methode, valeur_de_la_méthode)
"""
setattr(Agency, 'toto', agency_employees)

"""
crée une instance de la classe Agency qui s'appelle a, et qui récupères
l'employé avec l'id 132
et affiche le résultat de la méthode agency_employees
"""
a = Agency.objects.get(id=132)
print(a.toto())
```

---

```python
"""
On récupère tous les objets du modèle Agency
on crée une loop afin de récupérer tous les 
users(employés) de cette agence. On compte
ne nombre de users à travers une fonction
agency_employees qui a comme argument agency
on compte les users, on les affiche un par un
puis, on récupère les users placés au bout du
chemin agency.situations, avec distinct('user')
on récupère une seule occurence d'un user car il
en existe plusieurs selon plusieurs situations
"""
agencies = Agency.objects.all()

for agency in agencies:
    users = agency_employees(agency)
    print(users.count())
    exit()
    for user in users:
        print(user)


    print('* %s' % agency.name)
    situations = agency.situations.distinct('user')
    for situation in situations:
        # print(dir(situation.user))
        print(situation)
    exit()
```

---
---

## Les petites requêtes

```python
"""les personnes nées en région parisienne"""
parisiens = User.objects.filter(Q(birth_city__iexact="paris"))
l_parisiens = [{'firstname': parisien.firstname} for parisien in parisiens if parisien.firstname.startswith('S')]
print(l_parisiens)
"""for parisien in parisiens:
    print(parisien.birth_city)"""
```

```python
""""récupérer les salariés sébastien et christophe nés en 1970"""
seventies = User.objects.filter(Q(firstname__iexact="sebastien") | Q(firstname__iexact="christophe") & Q(birth_date__year=1970))
print(seventies)
print()
"""for seventy in seventies:
    print(seventy.lastname)"""
```

```python
"""agés de plus de 40 ans"""
born_before_82 = User.objects.filter(birth_date__year__lte=1982)
print([user.birth_date.strftime('%d/%m/%Y') for user in born_before_82])
```

```python
"""test trouvez trois prénoms avec la méthode filter in"""
three_users = User.objects.filter(firstname__in=['Tobias', 'Nadine', 'John'])
print(three_users)
print()
"""for user in three_users:
    print(user)"""
```