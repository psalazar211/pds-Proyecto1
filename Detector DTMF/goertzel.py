import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

#goertzemio
def goertzemio (senal,fs,N):
    fbuscadas= [697,770,852,941,1209,1336,1477,1633]
    f_filas = [697,770,852,941]
    magnitud={}
    for fevaluada in fbuscadas: 
        k = round(fevaluada*N/fs)
        theta = 2*math.pi*k/N
        realW = math.cos(theta) 
        WkN = -cmath.exp(-theta*1j)
        sk1 = 0
        sk2 = 0
        for n in range(N):
            sk = senal[n] + 2*realW*sk1 -sk2
            yk = sk - WkN*sk1
            sk2=sk1
            sk1=sk
        
        magnitud[fevaluada] = abs(yk)
    #Get the frecuencies
    freq1 = [key for key, value in magnitud.items()
    if value == max(magnitud.values())][0]
    magnitud.pop(freq1)
    freq2 = [key for key, value in magnitud.items()
    if value == max(magnitud.values())][0]

    if freq1 in f_filas:
        f_fila = freq1
        f_col = freq2
    else:
        f_fila = freq2
        f_col = freq1

 
    return f_fila, f_col

