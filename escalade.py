def saisir_escales():
    escales = {}

    print ("Faite entrez dans le vide pour afficher le resultat final ")
    while True:
        ville = input("Ville: ")

        if ville == "":
            break

        duree = float(input("Nombre d'heures d'escale: "))
        escales[ville] = duree

    return escales

def afficher_escales(escales):
    print("\nListe des escales :\n")
    total_heures = 0

    for ville, duree in escales.items():
        total_heures += duree
        print(f"{ville} {duree},\n")

    print(f"\nNombre total d'heures d'escale : {total_heures}")
escales_enregistrees = saisir_escales()

afficher_escales(escales_enregistrees)
