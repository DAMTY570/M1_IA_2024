def distances_entre_nombres():
    liste_nombres = input("Entrez une liste de nombres séparés par des virgules : ")
    liste_nombres = [int(x) for x in liste_nombres.split(",")]
    distances = [liste_nombres[i + 1] - liste_nombres[i] for i in range(len(liste_nombres) - 1)]
    return distances
resultat = distances_entre_nombres()
print(resultat)
