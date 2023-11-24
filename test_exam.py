
# INSTRUCTIONS
# ------------
# - Il y a un fichier par question.
# - Attention de bien extraire les fichiers de l'archive avant de rÃ©pondre.
# - RÃ©pondez Ã  la question en complÃ©tant la fonction/classe dont l'entÃªte est dÃ©jÃ  indiquÃ©e.
# - Ne modifiez pas les noms des fonctions/classes ou les noms des fichiers.
# - Vous pouvez ajouter des fonctions pour dÃ©couper le problÃ¨me.
# - Vous pouvez utiliser les bibliothÃ¨ques vues au cours.
# - Sauf mention contraire, les fonctions doivent renvoyer leur rÃ©sultat (return)
# - Un programme qui ne s'exÃ©cute pas ou qui plante ne rapporte aucun point.
# - Veillez Ã  renvoyer le bon type ("True" != True).
# - Les fichiers complÃ©tÃ©s doivent Ãªtre remis dans une archive ZIP sur claco.



# --------Q1-----------------------
# 19:05 - 19:12

# 4 points
# Ecrire une fonction nommÃ©e make_dict() qui renvoie un
# dictionnaire dont les clÃ©s sont les Ã©lÃ©ments d'une liste de
# chaÃ®nes de caractÃ¨res reÃ§ue en paramÃ¨tre. La valeur associÃ©e
# Ã  chaque clé sera un entier correspondant Ã  la somme du
# nombre de caractÃ¨res de la clÃ© et de 42.

def make_dict(my_list):
    dico = {}
    for i in range(len(my_list)):
        dico[my_list[i]] = int(len(my_list[i])) + 42

    return dico

my_list = ['ak0', 'fh', 'r', 'uyxio', 'd', 'w', 'okoiu']

# print(make_dict(my_list))






# ---------------------------Q2--------------------------------

# 19:12-19:22

# 5 points
# Ecrire une fonction nommÃ©e compute_means() qui prend en paramÃ¨tre
# une liste de dictionnaires dont la structure est semblale Ã  celle-ci:
my_list2 = [
    {
        "name": "Peter Parker",
        "matricule": "00001",
        "grades": [16, 18, 15, 19, 16]
    },
    {
        "name": "Tony Stark",
        "matricule": "00002",
        "grades": [15, 19, 15, 20, 15, 11]
    },
    {
        "name": "Steve Rogers",
        "matricule": "00003",
        "grades": [12, 13, 10, 20]
    }
]
# (Le nombre d'Ã©tudiants et le nombre de notes peut Ãªtre quelconque)
# La fonction devra renvoyer la liste d'Ã©tudiants modifiée: Une clÃ© "mean"
# devra Ãªtre ajoutÃ©e Ã  chaque dictionnaires d'Ã©tudiant avec la moyenne de
# ses notes comme valeur.

def compute_means(students):
    points = 0
    sum = 0
    for i in range(len(students)):
        points_list = students[i]["grades"]
        for j in points_list:
            sum += j
            points = sum/len(points_list)

        students[i]["mean"] = points

    return students



# print(compute_means(my_list2))





# --------------Q3----------------------

# 19:26 - 19:38

# Lecture ou ecriture de fichier
# 5 points
# Ecrire une fonction nommÃ©e parse_file() prenant un chemin vers
# un fichier en paramÃ¨tre. Le fichier contiendra sur chaque ligne
# un mot et un entier séparÃ©s par un espace (Le mot ne contiendra
# pas d'espace). Pour chaque ligne l'entier indique l'indice d'un
# caractÃ¨re du mot. La fonction parse_file() devra renvoyer une
# chaine de caractÃ¨res composÃ©e des caractÃ¨res indiquÃ©s sur chaque
# ligne. Le fichier data.txt est un exemple. On suppose que le
# fichier existe et que la structure qu'il contient est valide.
def parse_file(filename):
    res = ''
    with open(filename, 'r') as file:
        for line in file:
            a, b = line.split(" ")
            res += str(a[int(b)])
    return res


# Votre code ici
# if __name__ == "__main__":
#     print(parse_file('data.txt'))
# affichera cool



# ------------Q4-----------------------

# 19:40 - 56

#  4 points
# CrÃ©ez une classe nommÃ©e Person. Le constucteur devra prendre le
# prÃ©nom et le nom d'une personne en paramÃ¨tre. Les objets de la
# classe Person auront une propriÃ©tÃ© nommÃ©e fullname qui renverra
# une chaÃ®ne de caractÃ¨res composÃ©e du prÃ©nom suivit du nom sÃ©parÃ©s
# par un espace.
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def fullname(self):
        # return str(str(self.name), str(self.last_name))
        return self.name + " " + self.last_name


if __name__ == "__main__":
    lur = Person("Quentin", "Lurkin")
    print(lur.fullname())
    # affiche Quentin Lurkin




# -------------------Q5---------------------
import math
# 1 point
# Ecrivez la fonction integral() qui renvoie la valeur (float) de
# l'intÃ©grale dÃ©finie reprÃ©sentÃ©e dans le fichier integral.jpg
def integral():
    a = - 0.8
    b = 0.6
    res = 0
    x = 1
    f = (1 - x**4)**(1/2)
    for i in range(0, 0.8, 0.001):
        res -= (1 - i**4)**(1/2)

    for i in range(0, 0.6, 0.001):
        res += (1 - i**4)**(1/2)

    return res




if __name__ == "__main__":
    print(integral())



# --------------------Q6------------------

# choix multiple rÃ©seau
# 1 point
# Le protocol qui permet a un ordinateur d'obtenir une adresse IP
# lorsqu'il se connecter Ã  un rÃ©seau s'appelle:
#    1. HTTP
#    2. DHCP
#    3. DNS
#
# Pour rÃ©pondre Ã©crivez une fonction nommÃ©e answer() qui renvoie
# l'entier 1, 2, ou 3.


def answer():
    return 2
if __name__ == "__main__":
    print(answer())



