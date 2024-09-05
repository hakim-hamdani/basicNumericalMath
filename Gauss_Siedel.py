import numpy as np


def GS(A,x0,nmax,b):
    # Extraction de la diagonale principale
    diag_elements = np.diag(A)
    D = np.diag(diag_elements)

    # Extraction de la partie triangulaire inférieure
    L = np.tril(A) - D

    # Extraction de la partie triangulaire supérieure
    U = np.triu(A) - D


    # intialisation
    x_old=x0
    x=np.copy(x0)
    count=0
    while count < nmax:
        x = np.dot(np.linalg.inv( D + L ) , b - np.dot(U,x_old) )

        if np.max(np.abs(x-x_old)) < 1.0e-10:
            print("--------------> Yep converge")
            break
        x_old=x
        count+=1

    if count>=nmax:
            print("--------------> don't converge yet !")

    return x , count


