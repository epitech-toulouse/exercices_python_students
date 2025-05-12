nombres = []

for i in range(5):
    nombre = float(input(f"Entrez le nombre {i+1} : "))
    nombres.append(nombre)

plus_petit = min(nombres)
plus_grand = max(nombres)

print(f"Le plus petit nombre est : {plus_petit}")
print(f"Le plus grand nombre est : {plus_grand}")
