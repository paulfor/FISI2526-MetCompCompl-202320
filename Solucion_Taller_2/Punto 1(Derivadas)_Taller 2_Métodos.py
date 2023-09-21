import matplotlib.pyplot as plt
import numpy as np

#1.1

#Condiciones Dadas
R=1750
r=0.125
Bo=0.05
f=7
omega=3.5
T=2*np.pi/omega

#tiempo y flujo magnetico
t = np.linspace(0, 2*T, 1000)

def flujo_magnetico(t):
    return np.pi * r**2 * Bo * np.cos(omega * t) * np.cos(2 * np.pi * f * t)

#Corriente Inducida a traves del tiempo
def I(t):
    d_phi = -2 * np.pi * np.pi * f * r**2 * Bo * np.cos(omega * t) * np.sin(2 * np.pi * f * t) #derivada del flujo magnetico con respecto al tiempo
    return -(1/R)*(d_phi)


flujos = [flujo_magnetico(ti) for ti in t]
dI = [I(ti) for ti in t]

#Graficas
plt.figure(figsize=(12, 7))
plt.plot(t, dI)
plt.xlabel('Tiempo (s)')
plt.ylabel('Corriente (A)')
plt.title('Corriente Inducida sobre el Bucle en función del tiempo')
plt.grid(True)
plt.show()


#1.2

tiempos_en_cero = [0]

corrientes= I(t)

for i in range(1, len(t)):
    if corrientes[i - 1] * corrientes[i] < 0:
        tiempos_en_cero.append(t[i])

primeros_tres_tiempos = tiempos_en_cero[:3]


tiempo1=tiempos_en_cero[0]
tiempo2=tiempos_en_cero[1]
tiempo3=tiempos_en_cero[2]
print("Los primeros tres instantes de tiempo en los que la corriente sobre el bucle es igual a cero son:")
print(tiempo1)
print(tiempo2)
print(tiempo3)

    
    



