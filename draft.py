import numpy as np
import matplotlib.pyplot as plt

nx=3; ny=3

dx = 1 #1/(nx-1)
dy = 1 #/1(ny-1)

diag_block =np.eye(nx-1)*(-2/dx**2-2/dy**2)
diag_block =diag_block + np.diag(np.ones(ny-2),1)/dy**2
diag_block =diag_block + np.diag(np.ones(ny-2),-1)/dy**2
matrix = np.kron(np.eye(nx-1),diag_block)
matrix = matrix + np.diag(np.ones((nx-2)*(ny-1))/dy**2,ny-1)  
matrix = matrix + np.diag(np.ones((nx-2)*(ny-1))/dx**2,-(ny-1))  


plt.spy(matrix, markersize=5)




