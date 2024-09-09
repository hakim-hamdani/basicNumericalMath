from remplissage_Ab import *
from initial_data import *
from Gauss_Siedel import *

init=intial_data()

m=9
n=9

A= build_matrix_A(m,n,init)
b= build_vector_b(m,n,init)
Tmean=(init['Tbe']+init['Tbw']+init['Tbs']+init['Tbn'])/4
x0=Tmean*np.ones_like(b)#*Tmean
solution = GS(A=A,x0=x0,nmax=100,b=b)
print('num solution -->:\n', solution[0])
print('numpy solution-----> :\n', np.linalg.solve(A, b))


