# Histoire et définitions

## sommaire
- [Histoire et définitions](#histoire-et-définitions)
  - [sommaire](#sommaire)
  - [Semaines 1 et 2](#semaines-1-et-2)
    - [l'objet](#lobjet)
    - [la variable](#la-variable)
    - [Le typage dynamique](#le-typage-dynamique)
    - [Les 4 types numériques de Python](#les-4-types-numériques-de-python)
    - [Décodage ASCII](#décodage-ascii)
    - [Le projet Unicode](#le-projet-unicode)
    - [Les séquences](#les-séquences)
    - [La liste](#la-liste)
    - [L'instruction if/else](#linstruction-ifelse)
    - [Factorisation du code](#factorisation-du-code)
    - [La boucle for](#la-boucle-for)
    - [Une fonction](#une-fonction)
    - [Une compréhension de liste](#une-compréhension-de-liste)
    - [Un module](#un-module)
  - [Semaine 3](#semaine-3)
    - [Les fichiers](#les-fichiers)

---
---

## Semaines 1 et 2

### l'objet
En python, tout est objet, du coup, dans nos programmes nous seront amenés à manipuler de nombreux objets en leur donnant un nom par l'intermédiaire de variable. On dira alors que la variable référence l'objet.

Un objet est une strucure numérique qui va contenir des données, ansi qu'un ensemble de mécanismes qui permettent de manipuler ces données que l'on appelle méthodes.

Les objets ont tous un type, et le type va permettre de définir les données et les méthodes associées à cet objet. Toutes les méthodes de l'objet viennent de son type. C'est à dire qu'une chaine de caractère n'aura pas les mêmes méthodes qu'un entier...

### la variable
permet de référencer un objet (le nommer). dans note = 1 on dit que note référence l'objet 1(int). Lorsque une variable qui référencie déjà un objet est utilisée de nouveau pour référencer un autre objet, cette variable va déréférencer le premier objet pour référencer le nouveau.
Si l'objet n'a plus de référence, le mécanisme de garbage collector de Python va libérer la mémoire de l'ordinateur de cet objet.

### Le typage dynamique
en python, le type n'est pas lié à la variable qui référence l'objet, mais est lié à l'objet. Du coup la variable peut référencer des objets de type différent en cours d'exécution.

### Les 4 types numériques de Python
int => manipulent les nombres entiers,
float => manipulent les nombres décimaux,
complex => manipulent les nombres complèxes,
bool => manipulent la validation de conditions

### Décodage ASCII
le décodage asci définit une convention qui consiste à découper un flux de bit en blocs d'une certaine taille. Ascii découpe en blocs de 7 bits. Ensuite il s'agit de dire à quelle lettre correspond chaque bloc. Par exemple si le premier bloc retourne 97, le jeux de caractère ASCII retourne qu'il s'agit de la lettre a...
1100001 = 97 = a.
Une police de caractère définit un dessin qui correspond au caractère à afficher.
ASCII est très vite devenu obsolète à cause du fait que cette norme ne permet de représenter 128 caractères. Ses nombreuses extensions aussi bien qu'elles permettaient un découpage de 256 caractères maximum.

### Le projet Unicode
est une norme qui a codé l'intégralité des caractères du monde. Du coup grâce à ce projet, nous avons la possibilité de décoder et coder l'intégralité des caractères du monde entier. Python est totalement compatible avec Unicode.

### Les séquences
list, tuple, str, bytes

Une séquence est un ensemble finit d'éléments (objets) ordonnés et indicés de 0 à n-1 si j'ai n éléments.

### La liste
est une séquence d'objets hétérogènes. On peut y stocker des références vers tous types d'objets. La liste est mutable (on peut la modifier directement)

### L'instruction if/else
qui permet de faire de l'exécution conditionnelle. C'est à dire qu'une instruction d'un bloc de code va être exécuté en fonction qu'un test soit vrai ou faux.

### Factorisation du code
Ce qui permet de ne pas réécrire plusieurs fois un code qui fait la même chose.
Afin de faciliter la maintenance et la qualité du code.

### La boucle for
L'intérêt de la boucle for est d'automatiser une tache qui se répète

### Une fonction
une fonction est une structure ou une suite d'instructions que l'on peut réutiliser plusieurs fois dans un même projet.

### Une compréhension de liste
principe qui permet de manière simple et intuitive d'appliquer une opération à chaque objet d'une liste et éventuellement d'ajouter une condition if.

### Un module
contient un certain nombre de fonctions on d'opérations à effectuer et l'idée des modules c'est de mettre des opérations et fonctions similaires dans une même fichier. Pour jouer avec un module il suffit de l'importer. Il est possible aussi d'importer uniquement une des fonctions (méthodes) de ce module, il me suffit d'importer le nom de cette méthode 'from module import méthode'

## Semaine 3

### Les fichiers
Il faut maitriser 3 notions : l'encodage, l'itération, context manager
C'est l'objet fichier qui va se chager d'encoder ou décoder nos caractères