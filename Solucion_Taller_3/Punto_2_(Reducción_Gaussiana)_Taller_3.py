import numpy as np

# (2) Crear algoritmo de Reduccion Gaussiana para resolver sistemas de ecuaciones y retornar la matriz aumentada en su forma reducida junto a sus soluciones si las tiene


def Reduccion_Gaussiana (A, b):
    
    
    n= np.shape(A)[0]            #Se ajusta la matriz aumentada
    M= np.zeros(shape=(n,n+1))
    M[:,0:n] = A
    M[:,n] = b 
    
    for i in range(n):
        for k in range(i + 1, n):
            f = M[k, i] / M[i, i]
            M[k, i:] -= f * M[i, i:]

    
   
    x = np.zeros(n) #Sustitución en reversa para resolver los vectores

    for i in range(n-1,-1,-1):
        s= M[i, n] 
        for j in range(n-1, i, -1):
            s -= M[i,j]*x[j]
        x[i] = s/M[i,i]

    return M, x

            

        
# (a) Ejercicios

F= np.array([[3, 1, -1],\
             [1, -2, 1], 
             [4, -1, 1]])
    
b1= np.array([2, 0, 3])

Matriz_aumentada, x = Reduccion_Gaussiana(F, b1)

print("Para el punto (a) la matriz aumentada en su forma reducida es:")
print(Matriz_aumentada)
print("\n")
print("Las soluciones generales para las tres fuerzas son:")
print(x)
print("\n")

#(b)

I=np.array([[1, 1, 1],\
             [0, -8, 10], 
             [4, -8, 0]])
    
b2= np.array([0, 0, 6])

Matriz_aumentada, x = Reduccion_Gaussiana(I, b2)

print("Para el punto (b) la matriz aumentada en su forma reducida es:")
print(Matriz_aumentada)
print("\n")
print("Las soluciones generales para las tres corrientes son:")
print(x)
print("\n")
