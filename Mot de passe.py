import random

def generateur_password(caracteres_possibles):
    def password(longueur):
        return ''.join(random.choice(caracteres_possibles) for _ in range(longueur))
    return password
password_generator = generateur_password('Aer5-/')
mon_password = password_generator(7)
print(mon_password)
