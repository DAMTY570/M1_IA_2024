def wordcount(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        nb_caracteres = len(contenu)
        mots = contenu.split()
        nb_mots = len(mots)
        nb_lignes = contenu.count('\n') + 1
        vocabulaire = set(mots)
        nb_mots_distincts = len(vocabulaire)
        print(f"Le nombre de caractères (sans espaces) est {nb_caracteres}.")
        print(f"Le nombre de mots (avec espaces) est {nb_mots}.")
        print(f"Le nombre de lignes est {nb_lignes}.")
        print(f"Le nombre de mots distincts est {nb_mots_distincts} (taille du vocabulaire du fichier).")

chemin_fichier_test = 'datasets/count.txt'
wordcount(chemin_fichier_test)
