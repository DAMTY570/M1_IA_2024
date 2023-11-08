def somme_pair_impair():
    liste = input("Entrez chiffre ou nombre séparé par des virgule : ")
    liste = [int(x) for x in liste.split(",")]
    somme_pair = sum(liste[::2])
    somme_impair = sum(liste[1::2])
    return [somme_pair, somme_impair]
resultat = somme_pair_impair()
print(resultat)
