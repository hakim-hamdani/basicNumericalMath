import numpy as np

def TDMA_1D(N,P,Q):
    #--------------------------------
    # (2) can be rewritten as follows:
    #   T[i] = P[i]*T[i+1] + Q[i]
    #--------------------------------

    T=np.zeros(N)

    # back substitution
    T_N=Q[-1]
    T[N-1]=T_N
    for i in range(N-2,-1,-1):
        T[i]=P[i]*T[i+1]+Q[i]

    return T

def PQ_coeffs(N,a,b,c,d):
    #--------------------------------
    # (2) can be rewritten as follows:
    #   T[i] = P[i]*T[i+1] + Q[i]
    #   where : 
    #         P[i] = b[i]/(a[i]-c[i]*P[i-1])
    #         Q[i] = (d[i]+b[i]*Q[i-1])/(a[i]-c[i]*P[i-1])
    #         with:
    #             P[1]=b[1]/a[1]  & Q[1]=d[1]/a[1]
    # --------------------------------

    P=np.zeros(N)
    Q=np.zeros(N)

    P[0]=b[0]/a[0]
    Q[0]=d[0]/a[0]

    # forward substitution 
    for i in range(1,N):
        P[i]=b[i]/(a[i]-c[i]*P[i-1])
        Q[i]=(d[i]+c[i]*Q[i-1])/(a[i]-c[i]*P[i-1])
    
    return P , Q


def abcd_coeffs(N,kf,Af,dxf,dX,Sc,Sp,Tbw,Tbe):

    #--------------------------------
    # FMV : ap*Tp = ae*Te + aw*Tw + b ---->(1)   
    # where : 
    #       b= Sc*dV ; and if BC --> b = Sc*dV+ ab*Tb
    #       ap = ae + aw -Sp  ; at BC --> 'aw' or 'aw' = ab (b=boundary)
    #       aw or ae ==> af= kf*Af/dxf  and if BC --> ab= 2*af 
    # 
    # (1) can be rewritten as follows:
    #   a[i]*T[i] = b[i]*T[i+1] + c[i]*T[i-1] + d[i] -----> (2)
    #   where : 
    #         a[i]=ap, b[i]=ae, c[i]=aw, d[i]=b
    #         with:
    #              c[1]=0  & b[N]=0 
    # --------------------------------



    a = np.zeros(N)
    b = np.zeros(N)
    c = np.zeros(N)
    d = np.zeros(N)


    af= kf*Af/dxf
    a = np.full(N, 2*af-Sp) 
    a[0] = a[-1] = af + 2*af -Sp


    b[:-1] = af
    c[1:]  = af

    d = Sc*(dX*Af)*np.ones(N) # with dV the cell volume : dV= dX*Af
    d[0] += 2*af*Tbw
    d[-1]+= 2*af*Tbe

    return a,b,c,d

