from remplissage_Ab import *
from initial_data import *
from Gauss_Siedel import *
import time
import matplotlib.pyplot as plt


# parametres initiaux
init=intial_data()
n=init['Nxe'] # nombre de colonnes --> x-dir
m=init['Nye'] # nombre de lignes   --> y-dir ;if 1D --> m=1 

pb2D=type_problem(n,m,init)

if pb2D==0. :
    m=1

A= build_matrix_A(n,m,init)
# print(A)
b= build_vector_b(n,m,init)
Tmean=(init['T_top']+init['T_bottom']+init['T_right']+init['T_left'])/4.0
x0=Tmean*np.ones_like(b)#*Tmean

start_time = time.time()  # Commence le chronométrage
solution = GS(A=A,x0=x0,nmax=1500,b=b)
end_time = time.time()  # Termine le chronométrage
execution_time = end_time - start_time
print(f"Temps d'exécution : {execution_time} secondes")

# print('num solution -->:\n', solution[0])
print(solution[0])
# print('numpy solution-----> :\n', np.linalg.solve(A, b))

# # Transformation en 2D
# T_2D = solution[0].reshape((m, n))

# # Tracer le champ T
# plt.figure(figsize=(8, 6))

# plt.imshow(T_2D, cmap='viridis', aspect='auto')
# plt.colorbar(label='Valeur de T')
# plt.title('Champ T')
# plt.xlabel('Colonnes (n)')
# plt.ylabel('Lignes (m)')
# # plt.show()
