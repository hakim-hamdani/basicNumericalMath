import numpy as np

def build_matrix_A(m, n , init):
    # Nombre total d'éléments
    N = m * n
    
    # Initialisation de la matrice A de taille N x N
    A = np.zeros((N, N))

    af=init['kf']*init['Af']*init['dxf']
    ab=2*af

    for row in range(m):
        for col in range(n):
            # Calculer l'indice linéaire de l'élément
            i = row * n + col

            # Déterminer le coefficient ap selon la position (coin, bordure, centre)
            if (row == 0 or row == m-1) and (col == 0 or col == n-1):
                ap = af +af + ab + ab   # Coin
            elif row == 0 or row == m-1 or col == 0 or col == n-1:
                ap = 3*af + ab  # Bordure
            else:
                ap = 4*af  # Centre

            # Mettre ap sur la diagonale
            A[i, i] = ap

            # Connexion avec le voisin de gauche (Ouest)
            if col > 0:
                A[i, i-1] = -af  # aw

            # Connexion avec le voisin de droite (Est)
            if col < n-1:
                A[i, i+1] = -af  # ae

            # Connexion avec le voisin du dessus (Nord)
            if row > 0:
                A[i, i-n] = -af  # an

            # Connexion avec le voisin du dessous (Sud)
            if row < m-1:
                A[i, i+n] = -af  # as

    return A

def build_vector_b(m, n , init):
    # Nombre total d'éléments
    N = m * n
    
    # Initialisation de la matrice A de taille N x N
    b = np.zeros((N))

    af=init['kf']*init['Af']*init['dxf']
    ab=2*af

    for row in range(m):
        for col in range(n):
            # Calculer l'indice linéaire de l'élément
            i = row * n + col

            
            if (row == 0 and col == 0):
                b[i] = ab*init['Tbw'] + ab*init['Tbn']    # Coin
            elif (row == 0 and col == n-1):
                b[i] =  ab*init['Tbe'] + ab*init['Tbn']   # Coin
            elif (row == m-1 and col == 0):
                b[i] = ab*init['Tbw'] + ab*init['Tbs']    # Coin
            elif (row == m-1 and col == n-1):
                b[i] = ab*init['Tbe'] + ab*init['Tbs']    # Coin
            elif row == 0 :
                b[i] = ab*init['Tbn']  # Bordure
            elif row == m-1: 
                b[i] = ab*init['Tbs']  # Bordure
            elif col == 0: 
                b[i] = ab*init['Tbw']  # Bordure
            elif col == n-1:  
                b[i] = ab*init['Tbe']  # Bordure

    return b


