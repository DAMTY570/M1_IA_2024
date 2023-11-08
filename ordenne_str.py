def ordonne_str():
    chaine = input("Entrez un texte ou un mot : ")
    chaine_triee = ''.join(sorted(chaine))
    return chaine_triee
resultat = ordonne_str()
print(resultat)
