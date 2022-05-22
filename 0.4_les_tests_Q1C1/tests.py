import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consolidation.settings')
django.setup()
from django.db.models import Q
from group.models import User
from group.models import Agency


"""
Reste :
ne retourner que les salariés qui ont une situation active
(pas de date de fin ou date de fin non atteinte)

Récupérer les situations de l'agence et retourner chaque salarié
correspondant en un seul exemplaire.
"""

#############################################################################

# """
# salariés dont la situation active est sur une agence région parisienne
# """

# agencies = Agency.objects.all()
# for agency in agencies:
#     if '75' in agency.establishment.zip:
#         parisian_user = User.objects.filter(
#             most_current_situation__agency=agency
#             )
#         print('===========================')
#         print(agency.establishment.agency)
#         for firstname in parisian_user:
#             print(f"Employé : {firstname}")
#         print()
# exit()

#############################################################################

# """
# les personnes nées en région parisienne
# """
# parisiens = User.objects.filter(Q(birth_city__iexact="paris"))
# l_parisiens = [
#     {
#         'firstname': parisien.firstname
#     }
#     for parisien in parisiens if parisien.firstname.startswith('S')
# ]

# print(l_parisiens)

# """
# for parisien in parisiens:
#     print(parisien.birth_city)
# exit()
# """

#############################################################################

# """"
# récupérer les salariés sébastien et christophe nés en 1970
# """
# seventies = User.objects.filter(
#         Q(firstname__iexact="sebastien") |
#         Q(firstname__iexact="christophe") &
#         Q(birth_date__year=1970)
#     )
# print(seventies)
# print()

# """
# for seventy in seventies:
#     print(seventy.lastname)
# """

#############################################################################

# """
# agés de plus de 40 ans
# """
# born_before_82 = User.objects.filter(birth_date__year__lte=1982)
# print([user.birth_date.strftime('%d/%m/%Y') for user in born_before_82])

#############################################################################

# """
# test trouvez trois prénoms avec la méthode filter in
# """
# three_users = User.objects.filter(firstname__in=['Tobias', 'Nadine', 'John'])
# print(three_users)
# print()

# """
# for user in three_users:
#     print(user)
# """

#############################################################################

# """
# on récupère les users placés au bout du
# chemin agency.situations
# """
# agencies = Agency.objects.all()

# agency_names = []
# agency_users = []

# for agency in agencies:
#     print('* %s' % agency.name)
#     situations = agency.situations.distinct('user')
#     for situation in situations:
#         # print(dir(situation.user))
#         print(situation)
# exit()

#############################################################################

# """
# récupérer les salariés actifs
# """


# def agency_employees(self):
#     """Récupère les salariés actifs

#     Args:
#         self (class) : Le modèle Agency

#     Returns:
#     """
#     return User.objects.filter(most_current_situation__agency=self).distinct()


# setattr(Agency, 'toto', agency_employees)
# a = Agency.objects.get(id=132)
# print(a.toto())
# exit()

#############################################################################