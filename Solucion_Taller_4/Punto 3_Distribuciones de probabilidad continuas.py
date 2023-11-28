import numpy as np
import sympy as sym
import scipy as scp

x= sym.Symbol("x", real=True)
a= sym.Symbol("a", real=True)
b= sym.Symbol("b", real=True)

#3.1
def Funcion (x):
    if x >= -1 and x <= 2:
        return ((x**2)/3)
    
    else:
        return 0
    
a1, b1 = 0, 1  # para P(0 < X <= 1)
a2, b2 = 1, 2  # para P(1 < X <= 2)

# Se integrara manualmente en esta parte para verificar
integral_a = (1/3) * ((3/5) * b1**(5/3) - (3/5) * a1**(5/3))
integral_b = (1/3) * ((3/5) * b2**(5/3) - (3/5) * a2**(5/3))

print("La probabilidad P(0 < X <= 1) es:", integral_a)
print("\n")
print("La probabilidad P(1 < X <= 2) es:", integral_b)
print("\n")

#3.2

#Se define la funcion de densidad de probabilidad


def Funcion_normal (x):
    return (1/(6*(np.sqrt(2*np.pi)))) * sym.exp((-1/2)*((x-78)**2/6**2))


#3.2 (a) Se calcula la integral con los limites 

funcion_numerica = sym.lambdify(x, Funcion_normal(x), 'numpy')
probabilidad_mayor_72= scp.integrate.quad(funcion_numerica, 72, np.inf)


print("La probabilidad de que una persona que haga el examen alcance calificaciones mayores de 72 es:", probabilidad_mayor_72[0])
print("\n")


#3.2 (b)  

#Se plantea la ecuacion de la integral

ecuacion_integral_b = sym.integrate(Funcion_normal(x), (x, a, np.inf))

# Se resuelve la ecuación para encontrar el límite de calificación para A
calificacion_minima = sym.solve(ecuacion_integral_b - 0.1, a)  # Suponiendo que A es el 10% superior


print("la calificación mínima que un estudiante debe recibir para ganar una calificación de A es:", calificacion_minima[0])
print("\n")

#3.2 (c)

#Se realiza un proceso análogo al anterior punto

ecuacion_integral_c = sym.integrate(Funcion_normal(x), (x, a, np.inf))

punto_limite = sym.solve(ecuacion_integral_c - 0.281, a) 

print("El punto límite para pasar el examen es:", punto_limite[0])
print("\n")

#3.2 (d)

ecuacion_integral_d1 = sym.integrate(Funcion_normal(x), (x, a, np.inf))
calificacion_que_corta = sym.solve(ecuacion_integral_d1 - 0.75, a) 
calificacion_final= sym.integrate(Funcion_normal(x), (x, calificacion_que_corta[0] + 5, np.inf))



print("La proporcion de estudiantes con calificaciones de 5 o más puntos arriba de la calificacion es:", calificacion_final.evalf())
print("\n")

#3.2 (e)

excede_84 = ((sym.integrate(Funcion_normal(x), (x,84, np.inf))) /sym.integrate(Funcion_normal(x), (x,72,np.inf)))

print("La probabilidad de que su calificación exceda de 84 es:", excede_84.evalf())
print("\n")

