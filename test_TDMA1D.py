import numpy as np
from TDMA_function import *
import time

Af  = 1
kf  = 1
dX  = 1
dxf = 1

Sc=Sp=0

Tbe=400

Tbw = 100

N = 20

a,b,c,d = abcd_coeffs(N,kf,Af,dxf,dX,Sc,Sp,Tbw,Tbe)

# print(a)
# print(b)
# print(c)
# print(d)

P,Q=PQ_coeffs(N,a,b,c,d)

# print(P)
# print(Q)

start_time = time.time()  # Termine le chronométrage
solution = TDMA_1D(N,P,Q)
end_time = time.time()  # Termine le chronométrage
execution_time = end_time - start_time
print(f"Temps d'exécution : {execution_time} secondes")

print (solution)
