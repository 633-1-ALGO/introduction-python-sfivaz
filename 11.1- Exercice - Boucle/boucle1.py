# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]


def get_average(number_array):
    sum = 0
    for number in number_array:
        sum += number

    return sum / len(number_array)


print("Moyenne des nombres réels du tableau A", get_average(A), sep=" : ")
