def compter_occurences(chaine):
    result = []
    count = 1
    for i in range(1, len(chaine)):
        if chaine[i] == chaine[i - 1]:
            count += 1
        else:
            result.append((chaine[i - 1], count))
            count = 1
    result.append((chaine[-1], count))
    return result
chaine = 'aaaccdaad'
resultat = compter_occurences(chaine)
print(resultat)
