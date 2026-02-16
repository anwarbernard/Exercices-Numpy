# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 10:04:04 2026

@author: anwar
"""
import matplotlib.pyplot as plt
import numpy as np

# Exo 1
# V = np.random.randint(0, 6, 30)
# d = V[1:] - V[:-1]
# P = np.arange(0, 18)
# P2 = 2**P

# print(P2)

# Exo 2
# T = np.random.randint(10, 31, size=(10, 10))
# T2 = np.zeros((10+6, 10+6), dtype=int)
# T2[3:-3, 3:-3] = T
# print(T2)

# Exo 3
# def verif(carre):   #condition 1 tous les entiers de 1 à n**2
#     nb = np.arange(1, len(carre)**2+1)
#     Cf = np.sort(carre.flatten)
#     if np.all(nb==Cf):  # condition 2 sommes
#     # première diagonale
#         D1 = np.sum(np.diag(carre))
#     # deuxième diagonale
#         cinv = carre[::-1]    
#         D2 = np.sum(np.diag(cinv))
#     # sommes des lignes et colonnes
#         L = np.sum(carre, axis=1) # lignes
#         C = np.sum(carre, axis=0) # colonnes
#         Lbool = np.all(L == D1)
#         Cbool = np.all(C == D1)
#         return D1 == D2 and Lbool and Cbool
#     return False

# def conscarre(n):
#     carre = np.zeros((n,n))
#     i, j = n//2+1, n//2 # division entière
#     carre[i,j] = 1
#     for s in range(2, n*n+1):# tous les nombres entre 2 et n**2 compris
#         K = (i+1)%n # case suivante
#         L = (j+1)%n # le modulo % permet de repartir sur le côté opposé
#         if carre[K,L] != 0: # si la case est déjà occupé
#             K = (i+2)%n
#             L = j
#         i,j = K,L
#         carre[i,j] = s
#     np.savetxt("carre.csv", carre, fmt="%i", delimiter=";")
#     return carre
# Clu = np.loadtxt("carre.csv", delimiter=";")# charger un carré d'un fichier
# print(verif(Clu))

# Exo 4

# x = np.linspace(0, 2*np.pi, 10)
# p = np.stack((np.cos(x), np.sin(x)), axis=1)
# p1 = p[np.newaxis, :, :]
# p2 = p[:, np.newaxis, :]
# s = p1-p2
# dist2 = np.sum(s**2, axis=-1)
# dist_numpy = np.sqrt(dist2)
# print(p)
# print(p1)
# print(p2)
# print(s)
# print(dist2)
# print(dist_numpy)

# Exo 5

v = np.arange(10)
m = np.tile(v, (10,1))
mt = np.copy(m.T)
t = np.stack((m, mt), axis=2)
trgsup = 1*(t[:,:,0]>t[:,:,1])

def koch_n(n,x,t=-np.pi/3):
    R1 = np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
    R2 = np.array([[np.cos((np.pi+t)/2),-np.sin((np.pi+t/2))],[np.sin((np.pi+t)/2),np.cos((np.pi+t)/2)]])
    for i in range(n):
        x1 = x/3
        x2 = x1 @ R1 + x1[-1]
        x3 = x1 @ R2 + x2[-1]
        x4 = x1 + x3[-1]
        x = np.concatenate((x1[:-1],x2[:-1],x3[:-1],x4), 0)
    return x
x, t, n = np.array([[0,0],[1,1]]), -np.pi/3, 6
f = koch_n(n,x,t)
fig, ax = plt.subplots(figsize=(20,20))
ax.plot(f[:,0],f[:,1])
ax.set_title('Flocon de koch à itération 6')
ax.axis('equal')
plt.show()

        
        
        
        

