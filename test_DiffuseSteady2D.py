from remplissage_Ab import *
from initial_data import *
from Gauss_Siedel import *
import time
import matplotlib.pyplot as plt

init=intial_data()

m=15
n=15


A= build_matrix_A(m,n,init)
b= build_vector_b(m,n,init)
Tmean=(init['Tbe']+init['Tbw']+init['Tbs']+init['Tbn'])/4.0
x0=Tmean*np.ones_like(b)#*Tmean

start_time = time.time()  # Commence le chronométrage
solution = GS(A=A,x0=x0,nmax=1500,b=b)
end_time = time.time()  # Termine le chronométrage
execution_time = end_time - start_time
print(f"Temps d'exécution : {execution_time} secondes")

# print('num solution -->:\n', solution[0])
# print('numpy solution-----> :\n', np.linalg.solve(A, b))

# Transformation en 2D
T_2D = solution[0].reshape((m, n))

# Tracer le champ T
plt.figure(figsize=(8, 6))

plt.imshow(T_2D, cmap='viridis', aspect='auto')
plt.colorbar(label='Valeur de T')
plt.title('Champ T')
plt.xlabel('Colonnes (n)')
plt.ylabel('Lignes (m)')
plt.show()
