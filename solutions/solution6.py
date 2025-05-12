liste_courses = []
while True:
    item = input("Ajoutez un article à votre liste (ou tapez 'fin' pour terminer) : ")
    if item.lower() == "fin":
        break
    liste_courses.append(item)

print("\nVotre liste de courses :")
for article in liste_courses:
    print("- " + article)
