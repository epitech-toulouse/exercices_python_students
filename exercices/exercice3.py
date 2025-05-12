# Exercice 3
#
# Le but de cet exercice est de faire deviner
# un mot en 3 essaies. Si l'utilisateur trouve le mot : Ecrire "Gagné"
# Sinon : "Perdu"
#
# Niveau (Moyen)
#
# Concepts abordés : while - if - lower()

motMystere = "python"
nbrEssais = 3

while nbrEssais > 0:
    mot = input("Devinez le mot mystère : ")
    if mot.lower() == motMystere:
        print("Gagné")
        break
    else:
        nbrEssais -= 1
        print("Perdu")
