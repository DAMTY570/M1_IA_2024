import random

def devinette():
    nombre_aleatoire = random.randint(0, 100)
    tentatives_restantes = 3
    while tentatives_restantes > 0:
        try:
            guess = int(input("Devinez le nombre entre 0 et 100 : "))
            if guess < nombre_aleatoire:
                print("Trop petit")
            elif guess > nombre_aleatoire:
                print("Trop grand")
            else:
                print("Exact")
                return
            tentatives_restantes -= 1
            if tentatives_restantes > 0:
                print(f"Il vous reste {tentatives_restantes} tentatives.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    print(f"Vous avez épuisé toutes vos chances. Le nombre était {nombre_aleatoire}.")
devinette()
