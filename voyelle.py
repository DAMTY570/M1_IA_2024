def sans_voyelle():
    voyelles = 'aeiouyAEIOUY'
    chaine = input("Entrez votre mot ou votre texte: ")
    chaine_sans_voyelle = ''
    for char in chaine:
        if char not in voyelles:
            chaine_sans_voyelle += char
    return chaine_sans_voyelle
resultat = sans_voyelle()
print(resultat)
