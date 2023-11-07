import random

def devinette():
    nombre_aleatoire = random.randint(0, 100)
    while True:
        try:
            guess = int(input("Devinez le nombre entre 0 et 100 : "))
            if guess < nombre_aleatoire:
                print("Trop petit")
            elif guess > nombre_aleatoire:
                print("Trop grand")
            else:
                print("Exact")
                break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
devinette()
