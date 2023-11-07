import numpy as np

def devinette () :
    np.random.seed(0)


    x= np.random.randint(0,100)
    print (x)

    while True:
        y=int(input("entrer le nombre",))

        if (y>x):
            print("trop grand")
        elif (x>y):
            print('trop petit')
        else:
            print("execte")
            break
        return print("c'est fini")

devinette(2)