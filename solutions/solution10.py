mot = input("Entrez un mot : ").lower()
voyelles = "aeiouy"
nombre_voyelles = 0

for lettre in mot:
    if lettre in voyelles:
        nombre_voyelles += 1

print(f"Le mot '{mot}' contient {nombre_voyelles} voyelle(s).")
