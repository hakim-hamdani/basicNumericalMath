import numpy as np
from TDMA_function import *


Af  = 1
kf  = 1
dX  = 1
dxf = 1

Sc=Sp=0

Tbe=400

Tbw = 100

N = 3

a,b,c,d = abcd_coeffs(N,kf,Af,dxf,dX,Sc,Sp,Tbw,Tbe)

# print(a)
# print(b)
# print(c)
# print(d)

P,Q=PQ_coeffs(N,a,b,c,d)

# print(P)
# print(Q)

solution = TDMA_1D(N,P,Q)

print (solution)
