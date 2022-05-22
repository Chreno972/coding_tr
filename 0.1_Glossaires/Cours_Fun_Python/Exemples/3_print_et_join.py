"""Les fonctions print et join"""

# variable.split(séparateur)
split_test = 'je __ suis __ très __ en __ forme'
# séparateur.join([liste])
join_test = ['Je', 'suis', 'très', 'en', 'forme']

# La fonction split() construit une liste en séparant
# une chaine de caractère par son séparateur
print(split_test.split(' __ '))

# La fonction join() construit une chaine de caractère
# en joignant une liste par un séparateur
print(' __ '.join(join_test))
