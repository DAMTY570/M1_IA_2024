#!/usr/bin/env python
# coding: utf-8

# # Exo 1 : Devine le nombre

# Ecris une fonction nommée devinette qui ne prend aucun argument. Quand on l'exécute, elle choisit un nombre aléatoire en 0 et 100 (inclus)et demande à l'utilisateur de deviner ce nombre.A chaque fois que l'utilisateur entre un nombre, le programme affiche l'une de ces phrases :

# Trop grand
# Trop petit
# Exact

# Si l'utilisateur a choisit correctement, le programme s'arrete. Sinon, le programme demande encore à l'utilisateur de rentrer un nouveau nombre jusqu'à ce qu'il trouve la bonne solution et s'arrête.

# In[7]:


import numpy as np
def devinette():
    np.random.seed(0)
    
    x = np.random.randint(0,100)
    print(x)
    while True:
        y=int(input("entrer le nombre",))
       
        if (y>x):
            print("trop grad")
        elif (x>y): 
            print('trop petit')
        else:
            print('execte')
            break
        return print("c'est fini")


# In[ ]:


devinette()


# In[ ]:


np.random.seed(0)
    
x = np.random.randint(0,100)
x


# # Exo 2: Devine le nombre: Niveau 2

# Reprend ton code pour le programme précédent. Modifie le pour donner seulement 3 chances à l'utilisateur pour deviner le nombre aléatoire choisit. Après 3 tentatives echouées, le programme s'arrête et affiche à l'utilisateur qu'il a épuisé ses chances.

# In[5]:


import numpy as np

def devinette():
    np.random.seed(0)
    
    x = np.random.randint(0, 100)
    print(x)

    tentatives_restantes = 3

    while tentatives_restantes > 0:
        y = int(input("Entrez votre proposition : "))
       
        if y > x:
            print("Trop grand.")
        elif x > y:
            print('Trop petit.')
        else:
            print('Correct ! Vous avez deviné le nombre.')
            break
        
        tentatives_restantes -= 1
        if tentatives_restantes > 0:
            print(f"Il vous reste {tentatives_restantes} tentatives.")
        else:
            print(f"Désolé, vous avez épuisé vos chances. Le nombre à deviner était {x}.")
            break

devinette()


# # Exo 3 : La fonction sum

# En Python, la fonction sum te permet de faire la somme des nombres d'une liste. Par exemple:

# In[2]:


nombres = [5,2,6,8,9,4]
sum(nombres)


# In[3]:


def somme(liste):
    total = 0
    for nombre in liste:
        total += nombre
    return total

nombres = [5, 2, 6, 8, 9, 4]
resultat = somme(nombres)
print(resultat)


# # Exo 4 : Adresse email de nos employées

# Vous êtes chargé d'octroyer les emails des nouveaux employés de votre entreprise. Vous travaillez chez PythonBoss. L'adresse email de vos employés est sous le format prenom_nom@pythonboss.com. Vous souhaitez écrire un programme pour automatiser cela. La programme demande à un utilisateur son prenom, puis son nom et affiche son adresse email. Par exemple Kevin Degila aura comme adresse email : kevin_degila@pythonboss.com . Ici vous devrez remarquer que l'adresse email ne contient que des lettres miniscules: C'est la préférence du directeur de PythonBoss. Vous avez intérêt à le satisfaire.

# In[7]:


def generer_email(prenom, nom):
    prenom = prenom.lower()
    nom = nom.lower()
    adresse_email = f"{prenom}_{nom}@pythonboss.com"
    return adresse_email

# Demander le prénom et le nom de l'utilisateur
prenom_utilisateur = input("Entrez votre prénom : ")
nom_utilisateur = input("Entrez votre nom : ")

# Générer et afficher l'adresse email
adresse_email_utilisateur = generer_email(prenom_utilisateur, nom_utilisateur)
print("Votre adresse email est :", adresse_email_utilisateur)


# # Exo 5 : Ordonner une chaine de caractères

# In[1]:


def ordonne_str(chaine):
    return ''.join(sorted(chaine))

# Exemple d'utilisation
resultat = ordonne_str('python')
print(resultat)


# In[ ]:




