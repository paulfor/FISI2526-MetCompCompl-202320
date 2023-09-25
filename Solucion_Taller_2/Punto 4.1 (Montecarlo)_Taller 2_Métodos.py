import numpy as np
import matplotlib.pyplot as plt

N = 1000
a = 0 #parametro "a" de la integral definida
b = np.pi #parametro "b" de la integral definida
x = np.random.uniform(a,b,N) #N (número de muestras aleatorias que tomará)

def func_integrate(x):
    return np.exp(-x)*np.sin(x)


Iteo = 0.5*(1+np.exp(-np.pi)) #Se calcula la integral Real o Teórica


#4.1 Grafica error porcentual vs número de muestras N


error_porcentual= []

for N in x:
    fi = func_integrate(x)
    I = (b-a)*sum(fi)/N  #Aqui se calcula la integral con Montecarlo
    error = abs((I - Iteo) / Iteo) * 100
    error_porcentual.append(error)


plt.figure(figsize=(12, 7))
plt.scatter(x, error_porcentual, color="r")
plt.title("Error Porcentual Integral vs. Número de Muestras N")
plt.xlabel("Número de Muestras N")
plt.ylabel("Error Porcentual (%)")
plt.grid(True)
plt.show()

# utilizando escala logaritmica:

plt.figure(figsize=(12, 7))
plt.scatter(x, error_porcentual, color="r")
plt.title("Error Porcentual Integral vs. Número de Muestras N (escala Logaritmica)")
plt.xlabel("Número de Muestras N")
plt.ylabel("Error Porcentual (%)")
plt.xscale("log")
plt.yscale("log")
plt.grid(True)
plt.show()
