n = int(input("Entrez un nombre entier positif : "))
somme = 0

for i in range(1, n + 1):
    somme += i

print(f"La somme des nombres de 1 à {n} est : {somme}")
