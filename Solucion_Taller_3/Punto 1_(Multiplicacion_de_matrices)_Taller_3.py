import numpy as np


# (1) Construir el algoritmo de multiplicación de matrices y encontrar el resultado de las operaciones

def multiplicacion_matrices (M1, M2):
    M=np.zeros(shape=(len(M1),len(M2[0])))
    
    if len(M1[0]) == len(M2):
      
        for i in range (len(M1)):  # recorrer filas de M1
            for k in range (len(M2[0])): # recorrer columnas de M2
                for l in range (len(M2)): # recorrer filas de M2  y columnas de M1
                    M[i][k]=M[i][k]+M1[i][l]*M2[l][k]
        return M
    
    else:
        print("Las matrices no son multiplicables")
        return None

# (a) Pruebas
A=np.array([[5, -4, -2],\
             [5, -5, 4], 
             [2, 5, -4],
             [-5, 4, 3],
             [3, -4, -3]])
    
B=np.array([[5], \
            [-2], 
            [-3]])

multiplicacion_matrices(A, B)
print ("El resultado para el punto (a) es:") 
print(multiplicacion_matrices(A, B))
print("\n") 

#(b)    
C=np.array([[0, -1, -1, 3],\
             [5, -5, -2, 2], 
             [1, 0, 4, 5]])
    
D=np.array([[0, -3], \
            [-2, -1], 
            [3, -3]])
    
print ("El resultado para el punto (b) es:") 
print(multiplicacion_matrices(C, D))     
print("\n") 

        
    
#(c)

E=np.array([[2, -5, 5, 1],\
             [5, 2, -7, -6], 
             [-6, -1, 7, -4],
             [5, 4, 1, -5]])
    
F=np.array([[0, 4, -7, 1, -6], \
            [-1, -6, -5, 1, 1], 
            [2, -1, -6, 5, -5],
            [-3, -6, 6, 3, 5]])

print ("El resultado para el punto (c) es:")   
print(multiplicacion_matrices(E, F))
print("\n\n") 

#(1.2) Demostrar que la multiplicacion no es conmutativa

P=np.array([[1, 2], \
            [3, 4]])

O=np.array([[2, 1], \
            [4, 3]])
    

#Se tendrá que P*O != O*P, es decir, multiplicacion_matrices(P, O) != multiplicacion_matrices(O, P) 

print("Para dos matrices P y O cuadradas 2X2:")
print("P=",P)
print("\n")
print("O=",O)
print("\n")
print("Se tendrá que P*O != O*P:")

print("P*O=")
print(multiplicacion_matrices(P, O))
print("\n")
print("O*P=")
print(multiplicacion_matrices(O, P))
print("\n")
print("Comprobando así que la multiplicación entre matrices no es conmutativa")


            
