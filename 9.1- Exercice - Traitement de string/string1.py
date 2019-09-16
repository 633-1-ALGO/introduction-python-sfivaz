# Consigne : Récupérer le mot "chaine" du string s et l'afficher
s = 'un exemple de chaine'

# Pourquoi l'IDE reclame de scope Monsieur?
def getSubString(string, start, end):
    substring = ""
    for letter in range(start, end):
        substring = substring + string[letter]
    return substring


substring = getSubString(s, 14, 20)
print(substring)
