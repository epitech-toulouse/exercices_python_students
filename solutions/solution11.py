import re
from collections import Counter

def analyser_texte():
    choix = input("Voulez-vous saisir votre propre texte? (o/n): ").lower()

    if choix == 'o':
        texte = input("Entrez votre texte: ")
    else:
        texte = """
        Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat.
        In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor.
        Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere.
        Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
        """

    texte = texte.lower()
    texte = re.sub(r'[^\w\s]', '', texte) # => retirer la ponctuation

    mots = texte.split()

    compteur = {}
    for mot in mots:
        if mot in compteur:
            compteur[mot] += 1
        else:
            compteur[mot] = 1

    print(f"\nNombre total de mots: {len(mots)}")
    print(f"Nombre de mots uniques: {len(compteur)}")

    mots_tries = sorted(compteur.items(), key=lambda x: x[1], reverse=True)

    print("\nLes 5 mots les plus fréquents:")
    print("------------------------------")

    nb_a_afficher = min(5, len(mots_tries))

    for i in range(nb_a_afficher):
        mot, occurrences = mots_tries[i]
        print(f"{i+1}. '{mot}' : {occurrences} occurrence(s)")


analyser_texte()
