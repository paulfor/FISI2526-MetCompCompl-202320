import numpy as np
import sympy as sym

x = sym.Symbol('x',real=True)


#3.1

#3.1.1 Se hace de forma recursiva
def GetLaguerre(n,x):
    if n==0:
        poly = sym.Pow(1,1)
    elif n==1:
        poly = 1-x
    else:
        poly =(((2*n-1-x) * GetLaguerre(n-1, x)) - ((n-1) * GetLaguerre(n-2,x)))/n 
   
    return sym.expand(poly,x)


#3.1.2 se hace un proceso similar al de Legendre y el xn se acotan entre los intervalos dados
def GetDLaguerre(n,x):
    Pn = GetLaguerre(n,x)
    return sym.diff(Pn,x,1)

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        try:        
            xn1 = xn - f(xn)/df(xn)
            error = np.abs(f(xn)/df(xn))
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn

def GetRoots(f,df,x,tolerancia = 10):

    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots

def GetAllRootsGLag(n):
    xn = np.linspace(0,n+(n-1)*np.sqrt(n),1000)
   
    Lag = []
    DLag = []
   
    for i in range(n+1):
       Lag.append(GetLaguerre(i,x))
       DLag.append(GetDLaguerre(i,x))
   
    poly = sym.lambdify([x],Lag[n],'numpy')
    Dpoly = sym.lambdify([x],DLag[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
       ValueError('El número de raíces debe ser igual al n del polinomio.')
   
    return Roots
   

   
#3.1.3
def GetWeightsGLag(n):
   
    Roots = GetAllRootsGLag(n)
    W_Laguerre = []
    if n <= len(Roots):
        for k in range(n):
            xk = Roots[k]
            Ln = GetLaguerre(n + 1, xk)
            weight = xk / ((n + 1) ** 2 * Ln ** 2)
            W_Laguerre.append(weight)
    else:
        print("El n dado es mayor que el número de raices")
        return None
    
    Weights=np.array(W_Laguerre)
    Weights_f=np.unique(Weights)
    Weights_final=Weights_f.astype(float)

    return Weights_final
