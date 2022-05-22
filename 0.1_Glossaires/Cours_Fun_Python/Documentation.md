# Documentation du cours

## Sommaire
- [Documentation du cours](#documentation-du-cours)
  - [Sommaire](#sommaire)
  - [Semaine 1](#semaine-1)
    - [L'objet str](#lobjet-str)
    - [Le typage dynamique](#le-typage-dynamique)
    - [les mots-clés interdits](#les-mots-clés-interdits)
    - [La fonction type](#la-fonction-type)
    - [La fonction isinstance](#la-fonction-isinstance)
    - [Les types numériques](#les-types-numériques)
  - [Semaine 2](#semaine-2)
    - [Codage, jeux de caractères et unicode](#codage-jeux-de-caractères-et-unicode)
    - [Les chaines de caractères](#les-chaines-de-caractères)
    - [Les méthodes `split` et `join` et +](#les-méthodes-split-et-join-et-)
    - [String format](#string-format)
    - [Les expressions régulières](#les-expressions-régulières)
    - [Les séquences](#les-séquences)
    - [Les Listes](#les-listes)
    - [Exécutions conditionnelles if-else](#exécutions-conditionnelles-if-else)
    - [Boucles for et fonctions](#boucles-for-et-fonctions)
    - [Introduction aux compréhensions de liste*](#introduction-aux-compréhensions-de-liste)
    - [Introduction aux modules](#introduction-aux-modules)
  - [Semaine 3 notions de base](#semaine-3-notions-de-base)

---
---

## Semaine 1
[Sommaire](#sommaire)

En python tout est un objet, et le moyen de manipuler ces objets en Python, c'est de leur donner un nom,
par l'intermédiaire d'une variable. On dit que les variables référencent les objets.

Un objet est une structure qui va contenir des données et un ensemble de comportements
et que l'on appelle méthodes qui permettent de manipuler ces données. Les objets ont tous un type. Le type est le comportement par défaut
qui va être défini pour ces objets. Par conséquent, le type va permettre de définir les données et les
méthodes qui vont être associées à cet objet.

### L'objet str
> cet objet a des données associées c'est le mot "spam" et cet objet a également un ensemble de méthodes
> comme par exemple la méthode upper(). toutes les méthodes de la chaîne de caractères viennent grâce à 
> son type le type "chaîne de caractères". Pour appeler une méthode sur un objet, il faut utiliser la
> notation . Pour cela, nous allons mettre l'objet "point" de la méthode que l'on veut appeler.

Données => 'spam'
Méthodes => upper()
upper est une fonction built-in de python.
spam.upper()

---

### Le typage dynamique

Lorsque je fais a = 3 puis a = 'spam'
en sortie cela nous retourne 'spam'. 

La variable changer de type. Le type est défini à l'affectation.
```python
a = 1  # a devient un int
a = 'b' # a devient un str
```

Pour pouvoir manipuler des objets, il faut être capable de leur donner un nom, 
et on leur donne ce nom par le mécanisme de référencement qui consiste à donner 
un nom de variable qui désigne un objet sauvegardé dans la mémoire de l'ordinateur.

Si l'on utilise la fonction del pour supprimer la variable, le garbage collector de python supprime 
cette variable de la mémoire.

### les mots-clés interdits
Il existe en Python certains mots spéciaux, qu'on appelle des mots-clés, ou keywords en anglais,
qui sont réservés et ne peuvent pas être utilisés

**False, await, else, import, pass, None, break, except, in, raise, True, class, finally, is, return
and, continue, for, lambda, try, as, def, from, nonlocal, while, assert, del, global, not, with
async	elif	if	or	yield**

C'est une mauvaise pratique de réutiliser des noms d'objets mis à disposition par python :
```python
id(a) # retourne l'adresse mémoire de a
filter()
```

### La fonction type
type([4,7,yes])
return => list() (le type de l'objet)

---

### La fonction isinstance

print(isinstance(23, int))

Le print de cette instruction affiche True, 
ce qui signifie que 23 est une instance de la classe (du type) int (integer)

---

### Les types numériques
int(4.3)

float(4)

complex(4.0) => (4.0j) 'nombre complexe'

1 + 4

1 - 4

3 * 5

3 ** 5 => puissances

3 // 6

3 % 6

abs(-4)

True

False

1 < 2

1 > 5

entier <<= 2 (opérateur de décalage gauche)

---
---

[Sommaire](#sommaire)
## Semaine 2
**Notions de base pour écrire son premier programme en Python**
### Codage, jeux de caractères et unicode

**Unicode**

Unicode est une norme qui permet de coder et décoder l'intégralité des caractères du monde entier.
Unicode supporte tous les caractères du monde, il contient actuellement plus de 120 000 caractères.
"utf-8" => compatible avec ASCII (préférable d'utiliser cet encodage en python)
"utf-16'
"utf-32"

**Encode - Decode**

Encode = le programme re

Ce qui est stocké c'est toujours une suite de bits.

Pour traduire une suite d'octets en un caractère, il faut une convention qui permette de faire
la correspondance.

Le decode prend en entrée des bytes et permet d'obtenir un str.

Le encode prend un str et le représente comme une suite d'octets dans un certain jeu de caractères.


à la base, un caractère n'est pas sous forme d'octets, mais de type string.
pour qu'il soit chargé en mémoire sous forme d'octets, il faut utiliser des 
opérations d'encodage, ce qui retourne des caractères de type byte.
On passe de l'un à l'autre de ces types gràce à des opérations d'encodage spécifiques.

Encode => Aujourd'hui Python 3 supporte Unicode, et définit par défaut UTF-8 comme solution
d'encodage, à moins que la police de caractère à laquelle on fait référence ne soit pas contenue
dans l'ordinateur que l'on utilise.
Il est aussi possible aujourd'hui, d'utiliser des caractères accentués pour les noms de variables,
autant que certains symboles comme '𝞟', bien qu'il soit fortement
conseillé d'utiliser le plus possible les caractères anglo-saxons pour pallier à tout problème de
compatibilité.

**Python 3 considère que votre code source utilise par défaut l'encodage UTF-8**

> les données manipulées par un programme proviennent pour l'essentiel de sources externes, (base de
> données ou formulaire Web), et donc pas du code source. 
> Lorsque votre programme doit interagir avec les utilisateurs d'une langue spécifique
> il faudrait créer un fichier spécifique, qui contient toutes les chaînes de
> caractères spécifiques.

Il est possible de changer l'encodage de notre code source en insérant une ligne de code commentée
en haut du fichier.

```python
# -*- coding: <nom_de_l_encodage> -*-
```

Il est aussi possible de savoir quel encodage est utilisé par notre système par défaut:

```python
import sys
print(sys.getdefaultencoding())

# affiche UTF-8
```

---

[Sommaire](#sommaire)
### Les chaines de caractères

str est la classe qui représente une chaine de caractères. Il est possible de manipuler un chaine de
caractères gràce à des méthodes natives de Python. 
Par exemple:
```python
"""
Afin de trouver toutes les méthodes à utiliser sur notre type de classe
on utilise la fonction dir()
"""
(print(dir(str)))
# => '__add__', '__class__', '__contains__'...

"""
par exemple pour obtenir la longueur d'une chaine de caractères
"""
chaine_de_car = 'salut je suis une chaine de caractères'

chaine_de_car.__class__
# <class 'str'> => class est une méthode built_in

print(len(chaine_de_car))
# 8 => len() est une fonction built_in
```

### Les méthodes `split` et `join` et +

`split` : permet de découper une chaine selon un séparateur pour obtenir une liste,
```python
'abc=:=def=:=ghi=:=jkl'.split('=:=')
# ['abc', 'def', 'ghi', 'jkl']
```

`join` : permet de reconstruire une chaine à partir d'une liste.

exemple
```python
"=:=".join(['abc', 'def', 'ghi', 'jkl'])
# 'abc=:=def=:=ghi=:=jkl'
```

!!! S'exercer avec les outils de base sur les chaines de caractères 'fonctions et méthodes'.
(
replace, strip, find, rfind, index, count, startswith, endswith, upper(), lower(),
swapcase(), capitalize(), title() ...
)

---

[Sommaire](#sommaire)
### String format
**Formatage de chaines de caractères**

> On désigne par formatage les outils qui permettent d'obtenir une présentation fine des résultats,
> que ce soit pour améliorer la lisibilité ou pour respecter la syntaxe d'un outil auquel on veut passer les données
> pour un traitement ultérieur.

**Les f-strings**
Depuis la version 3.6 de Python, on peut utiliser les f-strings, le premier mécanisme de formatage que nous étudierons.
C'est le mécanisme de formatage le plus simple et le plus agréable à utiliser.
Ne pas oublier quand même qu'il reste des outils de formatages toujours fortement utilisés comme
'%' et '.format()'

```python
prenom, nom, age = 'Jean', 'Dupont', 35

print(f"{prenom} {nom} a {age} ans")

# 'Jean Dupont a 35 ans'
```

On peut ajouter plusieurs choses entre les crochets y compris des appels de fonction
```python
notes = [12, 15, 19]
f"nous avons pour l'instant {len(notes)} notes"
```

**Méthode .format()**
```python
prenom, nom, age = 'Jean', 'Dupont', 35

"{} {} a {} ans".format(prenom, nom, age)
```

**L'opérateur %**
```python
"%s %s a %s ans" % (prenom, nom, age)
```

---

[Sommaire](#sommaire)
### Les expressions régulières

Une expression régulière est un objet mathématique permettant de décrire un ensemble de textes qui
possèdent des propriétés communes.

l'une des plus simples expressions régulières utilisées est par exemple:
*.txt => désigne tous les fichiers dont le nom se termine par .txt, c'est le "pattern matching"

!!! réaliser des entrainements sur les regex et re

---

### Les séquences
**list, tuple, str, bytes**
(une séquence en python est un ensemble fini et ordonné d'éléments indicés de 0 à n-1 si j'ai n éléments)

exemple
```python
s = 'egg, bacon'
len(s)
# 10
'egg in s'
# True
```
Il est possible de faire du slicing sur les éléments contenus dans une séquence.
```python
s = 'egg, bacon'
s[0]
s[9]
len(s)
'egg' in s
'egg' not in s
s 
s + ', and beans'
s.index('g')
s.count('g')
min(s)
max(s)
'x'*30 
s = 'egg, bacon'
s[0:3]
s[5:10]
s[:3]
s[5:]
s[:]
s[0:10:2]
s[::2]
s[:8:3]
s[2::3]
s[100]
s[5:100]
s[100:200]
s[-10:-7]
s[:-3]
s[::-1]
s[2:0:-1]
s[2::-1]
```

---

[Sommaire](#sommaire)
### Les Listes
Une liste est une séquence d'objets hétérogène 'qui accèpte tout type d'objets
Elle ne contient pas les objets elle même, mais des références vers ces objets.
La liste est très maléable et mutable indéfiniment.

Comme il s'agit d'une séquence, il est possible d'intéragir sur une liste avec du slicing.
Pour regarder toutes les opérations qui sont possibles sur un liste comme pour tout autre objet
nous pouvons utiliser la fonction dir(la_liste), la_liste__class__.

Pour avoir la réelle signification d'un objet on utilise help(la_liste.append)

**append et extend**
```python
la_liste = [1, 2, 3, 4]
la_liste.append('ajout')
# [1, 2, 3, 4, 'ajout']

la_liste.extend([5, 6, 7, 8])
# [1, 2, 3, 4, 'ajout', 5, 6, 7, 8]
```
append => insère un élément à la fin d'une liste
extend => ajoute plusieurs élément d'une liste à la fin d'une autre liste
insert => ajoute un élément à un index précis d'une liste

---

[Sommaire](#sommaire)
### Exécutions conditionnelles if-else

Les clauses if else sont exécutées dans un bloc d'instructions.
Un bloc d'instruction est un ensemble d'instructions qui sont toutes
indéntées de 4 caractères vers la droite (espaces).

---

### Boucles for et fonctions

---
### Introduction aux compréhensions de liste*

---
### Introduction aux modules

---
---

[Sommaire](#sommaire)
## Semaine 3 notions de base
**Renforcement des notions de base, références partagées.**