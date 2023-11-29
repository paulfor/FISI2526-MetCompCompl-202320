import numpy as np

#4.1
T = np.array([[0.40,0.25,0.30,0.10],\
              [0.20,0.25,0.30,0.10],\
              [0.20,0.25,0.10,0.10],\
              [0.20,0.25,0.30,0.70],\
             ])
    
pi= np.array([0.25, 0, 0.5, 0.25 ])   

gen_g= np.array(["T", "G", "C", "T", "C", "A", "A", "A"])

probabilidad_g = pi[["ACGT".index(gen_g[0])]]

for i in range(1, len(gen_g)):
    probabilidad_g *= T["ACGT".index(gen_g[i - 1])]["ACGT".index(gen_g[i])]

print("La probabilidad de obtener el gen g es:", probabilidad_g[0])
print("\n")

#4.2

E = np.array([[0.8, 0, 0, 0.2],\
              [0.05, 0.9, 0.1, 0.1],\
              [0.05, 0.1, 0.9, 0],\
              [0.1, 0, 0, 0.7]])
              
gen_T= np.array(["A", "C", "G", "A", "G", "U", "U", "U"])

probabilidad_T = pi[["ACGT".index(gen_g[0])]]

for j in range(1, len(gen_T)):
    probabilidad_T *= E["UGCA".index(gen_T[j])]["ACGT".index(gen_g[j])]
    
print("La probabilidad de obtener el gen anterior es:", probabilidad_T[0])