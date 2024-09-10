import numpy as np


def GS(A,x0,nmax,b):
    # Extraction de la diagonale principale
    D = np.diag(np.diag(A))

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

        if np.max(np.abs(x-x_old)) < 1.0e-6:
            print("--------------> Yep converge", f' | {count} iterations')
            break
        x_old=x
        count+=1

    if count>=nmax:
            print("--------------> don't converge yet !")

    return x , count
