def generer_email():
    prenom = input("Entrez votre prénom : ").strip().lower()
    nom = input("Entrez votre nom : ").strip().lower()
    email = f"{prenom}_{nom}@pythonboss.com"
    return email
adresse_email = generer_email()
print(f"Votre adresse email est : {adresse_email}")
