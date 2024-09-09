from Gauss_Siedel import *


A=np.array([[ 6.0 , -1.0 ,  0.0 , -1.0],
            [-1.0 ,  6.0 , -1.0 ,  0.0],
            [ 0.0 , -1.0 ,  6.0 , -1.0],
            [-1.0 ,  0.0 , -1.0 ,  6.0]], dtype='d')

b=np.array([800.0,1000.0,1200.0,1000.0], dtype='d')
x0=np.array([0,0,0,0], dtype='d')
solution,count= GS(A=A,b=b,nmax=20,x0=x0)
print('Num solution ', solution)
print('count : ', count)



print('*'*50)
print('solution analytique--->')
print(np.linalg.solve(A, b))
