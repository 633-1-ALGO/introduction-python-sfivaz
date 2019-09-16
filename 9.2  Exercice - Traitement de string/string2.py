# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

def inverseur(string):
    string_inverse = ""
    cpt = len(string)-1
    while(cpt != 0):
        string_inverse = string_inverse + string[cpt]
        cpt -= 1
    return string_inverse

new_texte = inverseur(texte)
print(new_texte)

