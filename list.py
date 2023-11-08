def somme(liste):
    total = 0
    for nombre in liste:
        total += nombre
    return total
nombres = [5, 2, 6, 8, 9, 4]
resultat = somme(nombres)
print(resultat)
