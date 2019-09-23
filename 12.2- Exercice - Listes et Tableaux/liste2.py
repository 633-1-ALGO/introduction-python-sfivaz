# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

plus_grand = 0
i = 0
j = 0
while i < len(tab):
    while j < len(tab[i]):
        if tab[i][j] > plus_grand:
            plus_grand = tab[i][j]
        j = j + 1
    i = i + 1
    j = 0

print(plus_grand)
