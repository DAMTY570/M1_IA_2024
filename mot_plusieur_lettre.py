from collections import Counter

def mot_lettre_repetee(liste_mots):
    max_repetition = 0
    mot_choisi = None

    for mot in liste_mots:
        compte_lettres = Counter(mot)
        lettre, repetition = compte_lettres.most_common(1)[0]

        if repetition > max_repetition:
            max_repetition = repetition
            mot_choisi = mot

    return mot_choisi
resultat = mot_lettre_repetee(["On", "a", "effectuee", "plusieurs", "tests", "elementaire", "ce", "matin"])
print(resultat)
