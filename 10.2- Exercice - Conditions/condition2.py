# Problème : Déterminer si une année est bissextile ou non. Pour cela, il faut avoir ces règles en tête :
#                   Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
#                   Si elle est multiple de 4, on regarde si elle est multiple de 100.
#                       Si c'est le cas, on regarde si elle est multiple de 400.
#                           Si c'est le cas, l'année est bissextile.
#                           Sinon, elle n'est pas bissextile.
#                       Sinon, elle est bissextile.
#
# Résultat attendu : Un message affichant "Année bissextile" ou "Année non bissextile"

def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            return (year % 400 == 0)
        else:
            return True
    else:
        return False


def check_is_leap_year(year):
    if (is_leap_year(year)):
        print("Année bissextile")
    else:
        print("Année non bissextile")


check_is_leap_year(2020)
