# Exemples de boucle for

print("Décomposition d'un mot en lettre")

chaine = "Hello World !"

for lettre in chaine:
    print("Lettre courante = ", lettre)
print("")

tableau = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

cpt = 0
for element in tableau:
    print("indice courant = ", cpt)
    print("element courant = ", element)
    print("-------------------")
    cpt += 1
print("")

print("Décompte du nombre d'execution de la boucle")
n = len(tableau)  # longueur du tableau
for i in range(0, n):  # "i" représentant l'indice courant et range une séquence de [0 à n-1]
    for j in range(0, len(tableau[i])):
        print("Execution n°:", i + 1, "Resultat :", "ligne: ", i, "colonne: ", j, " ", tableau[i][j])
    print("")
