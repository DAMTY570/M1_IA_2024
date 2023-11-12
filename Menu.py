def restaurant(menu):
    total = 0

    print("Bienvenue dans notre Restaurant")

    while True:
        commande = input("Commande: ")

        if commande.lower() == "fin":
            print(f"Votre total est {total}. Merci de votre commande!")
            break

        if commande in menu:
            prix = menu[commande]
            total += prix
            print(f"{commande} coûte {prix}, total est {total}")
        else:
            print(f"Désolé, Nous n'offrons pas de {commande} aujourd'hui.")
            afficher_menu(menu)

def afficher_menu(menu):
    print("\nMenu:")
    for plat, prix in menu.items():
        print(f"{plat}: {prix}")
    print("\n")


menu = {
    "Burger": 10,
    "Cafe": 7,
    "Tiramitsu": 3.5,
    "Lasagne": 12,
    "Pates bolognaise": 13,
    "Pizza":14 
}

restaurant(menu)
