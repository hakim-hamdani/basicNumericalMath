import numpy as np


#TODO : modified "ap" to include newmann or dirichlet BC
# if newmann qb=10 in west side: aw=0 and b+=dAy*qb 


def build_matrix_A(n, m , init):

    pb2D=type_problem(n,m,init)

    Areaf=init['dX']*init['dZ']
    af=init['kf']*Areaf/init['dxf']
    ab=2*af # pour un maillage structuré et dx_bord = dxf/2 

    # source therme S = Sc + SpTp
    Sp=init['Sp']

    # Nombre total d'éléments
    N = m * n
    
    # Initialisation de la matrice A de taille N x N
    A = np.zeros((N, N))

    #cell volume in 2D
    dV=init['dY']*init['dX']*init['dZ']


    for row in range(m):
        for col in range(n):
            # Calculer l'indice linéaire de l'élément
            i = row * n + col

            flag = flag_BC( BC_type([n,m],row,col,init) )

            # print(row,col,flag,BC_type([n,m],row,col,init),(4 - flag[0] - flag[2] ))
            
            if pb2D==1.:
                ap=(4 - flag[0] - flag[2] )*af + flag[0]*ab + flag[2]*ab - Sp*dV
            else:  
                ap=(2 - flag[0])*af + flag[0]*ab - Sp*dV
            
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

def build_vector_b(n, m , init):

    pb2D=type_problem(n,m,init)

    # Nombre total d'éléments
    N = m * n
    
    #source term S=Sc+Sp*Tp
    Sc=init['Sc']

    #cell volume in 2D
    dV=init['dY']*init['dX']*init['dZ']

    # Initialisation de la matrice A de taille N x N
    b = Sc*dV*np.ones((N))

    Areaf=init['dX']*init['dZ']
    af=init['kf']*Areaf/init['dxf']
    ab=2*af



    for row in range(m):
        for col in range(n):
            # Calculer l'indice linéaire de l'élément
            i = row * n + col

            flag = flag_BC( BC_type([n,m],row,col,init) )


            dAy=init['dZ']*init['dX'] # dAy = dX*dZ avec dZ=1. for 2D case
            dAx=init['dZ']*init['dY'] 
            dAz=init['dX']*init['dY'] 

            # ----------------cell in the corner
            if ( col == 0 and row == 0 ):
                b[i] += flag[0]*ab*init['T_left'] + pb2D*flag[2]*ab*init['T_top'] + \
                        flag[1]*dAy*init['Q_left'] + pb2D*flag[3]*dAx*init['Q_top'] 
            elif (col == n-1 and row == 0):
                b[i] += flag[0]*ab*init['T_right'] + pb2D*flag[2]*ab*init['T_top'] + \
                        flag[1]*dAy*init['Q_right'] + pb2D*flag[3]*dAx*init['Q_top'] 
            elif (col == 0 and row == m-1):
                b[i] += flag[0]*ab*init['T_left'] + pb2D*flag[2]*ab*init['T_bottom'] + \
                        flag[1]*dAy*init['Q_left'] + pb2D*flag[3]*dAx*init['Q_bottom'] 
            elif (col == n-1 and row == m-1):
                b[i] += flag[0]*ab*init['T_right'] + pb2D*flag[2]*ab*init['T_bottom'] + \
                        flag[1]*dAy*init['Q_right'] + pb2D*flag[3]*dAx*init['Q_bottom']   
            
            # -----------------cell in the boundary
            elif col == 0: 
                b[i] += flag[0]*ab*init['T_left'] + flag[1]*dAy*init['Q_left'] 
            elif col == n-1:  
                b[i] += flag[0]*ab*init['T_right'] + flag[1]*dAy*init['Q_right'] 
            elif row == 0 :
                b[i] += pb2D*flag[2]*ab*init['T_top'] + pb2D*flag[3]*dAy*init['Q_top'] 
            elif row == m-1: 
                b[i] += pb2D*flag[2]*ab*init['T_bottom'] + pb2D*flag[3]*dAy*init['Q_bottom'] 


    return b


def flag_BC(boundary):

    flag=[0.,0.,0.,0.] # [Diric1 , Newman1, Diric2 , Newman2]
    # flag[0] et flag[1] for x-j-direction west or east  | left or right
    # flag[1] et flag[2] for y-i-direction north or south  | top or bottom

    if boundary[0]=='Dirichlet':
        flag[0]=1.
    elif boundary[0]=='Newmann':
        flag[1]=1.
    if boundary[1]=='Dirichlet':
        flag[2]=1.
    elif boundary[1]=='Newmann':
        flag[3]=1.

    return flag


def BC_type(domain_size,row,col,init):
            """
            x-directoon : j direction in python (colonnes-columns)
            y-directoon : i direction in python (lignes-raws)
            Boundary Conditions:
                i=0   : top-north
                i=m-1 : bottom-south
                j=0   : left-west
                j=n-1 : right-east
            """
            n=domain_size[0]
            m=domain_size[1]

            BC=['','']
            
            # cell in the corner :2sides
            if (col == 0 and row == 0): # Coin
                 BC[0]=init['BC_T_left'] 
                 BC[1]=init['BC_T_top'] 
            elif (col == n-1 and row == 0):
                 BC[0]=init['BC_T_right'] 
                 BC[1]=init['BC_T_top']  
            elif (col == 0 and row == m-1):
                 BC[0]=init['BC_T_left']
                 BC[1]=init['BC_T_bottom']
            elif (col == n-1 and row == m-1):
                 BC[0]=init['BC_T_right']
                 BC[1]=init['BC_T_bottom']
            
            # cell in the boundary : 1side
            elif col == 0: 
                BC[0]=init['BC_T_left'] 
            elif col == n-1:  
                BC[0]=init['BC_T_right'] 
            elif row == 0 :
                BC[1]=init['BC_T_top'] 
            elif row == m-1: 
                BC[1]=init['BC_T_bottom'] 

            
            return BC


def type_problem(n,m,init):
    """
    Type de probleme 1D ou 2D : booleen
    """
    pb2D=0.

    if (m > 1) or (init['1D_prob']==False):
       pb2D=1.
    if (init['1D_prob']==True) or (m==1):
        m=1
        pb2D=0.

    return pb2D