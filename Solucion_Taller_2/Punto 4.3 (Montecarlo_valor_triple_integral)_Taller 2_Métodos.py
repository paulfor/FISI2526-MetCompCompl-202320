import numpy as np

#4.3

R=1 #Radio de la esfera centrada en el origen
N=1000000

x = np.random.uniform(-R,R,N)
y = np.random.uniform(-R,R,N)
z = np.random.uniform(-R,R,N)

I=0

for i in range(N):
    if x[i]**2 + y[i]**2 + z[i]**2 <= R**2:
        I+= np.sin(x[i]**2+y[i]**2+z[i]**2) * np.exp(x[i]**2+y[i]**2+z[i]**2)
        

V= (4/3) * np.pi * R**3
I_final=(V/N) * (I) #Se calcula el valor aproximado con el método Montecarlo


print("El valor aproximado de esta integral será:", I_final)
