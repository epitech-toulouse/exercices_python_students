# Exercice 2
#
# Le programme doit demander un nombre à l'utilisateur et lui dit si
# ce nombre est pair ou impair.
#
# Niveau (Facile)
#
# Concepts abordés : input() - print() - modulo % - if

a = input("Entrez un nombre : ")

if int(a) % 2 == 0:
    print("Le nombre est pair")
else:
    print("Le nombre est impair")
