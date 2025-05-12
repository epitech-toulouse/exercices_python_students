# Solution 3

mot_secret = "python"
essais = 3

print("Bienvenue dans le jeu du Mot Mystère !")
print("Devine le mot secret en 3 essais.")

while essais > 0:
    reponse = input("Quel est ton essai ? ")
    if reponse.lower() == mot_secret:
        print("Bravo ! Tu as trouvé le mot mystère !")
        break
    else:
        essais -= 1
        print("Raté ! Il te reste", essais, "essai(s).")

if essais == 0:
    print("Dommage ! Le mot mystère était :", mot_secret)
