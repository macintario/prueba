import random
import math

import numpy as np
import pandas as pd

def calc_dist(xi,xj,yi,yj):
    xx = xi-xj
    xx = xx*xx
    yy = yi-yj
    yy = yy*yy

    distancia = math.sqrt(xx+yy)
    return distancia



puntos =[
    [1, 1],
    [1, 3],
    [2, 4],
    [2, 2],
    [2, 3],
    [8, 6],
    [7, 4],
    [9, 6],
    [7, 5],
    [5, 8]
    ]


print(puntos)

k=2

centroide = list()

for i in range(0, k):
    centroide.append([np.random.randint(0,10),np.random.randint(0,10)])
print("Centroides iniciales")
print(centroide)

for l in range(0,5):
    distancias = list()

    pertenece = 0
    n_punto = 0
    asignacion = list()
    for x, y in puntos:
        dist_min = 1000
        n_centroide = 0
        for i, j in centroide:
            distancia = calc_dist(i, x, j, y)
            if dist_min > distancia:
                dist_min=distancia
                pertenece = n_centroide
            n_centroide += 1
        print("Punto:"+str(x)+","+str(y)+" pertenece:"+str(pertenece)+" dist_min="+str(dist_min))
        asignacion.append([n_punto, pertenece])
        n_punto += 1
    #print(asignacion)

    for np, per in asignacion:
        sumx = 0
        sumy = 0
        i = 0
        for x, y in puntos:
            if np == i:
                sumx += x
                sumy += y
            i += 1
        sumx = sumx / k
        sumy = sumy / k
        centroide[per]=[sumx, sumy]
    print("Nuevos centroides")
    print(centroide)
        #nuevos_centroides[per] = [1,2]



print("OK")

