from goertzel import goertzemio
import numpy as np

fs=8000
N=1000
frows=[697,770,852,941]
fcolumns=[1209,1336,1477,1633]
errors=0
for frow in frows:
    for fcolumn in fcolumns:
        sine_wave = [np.sin(2 * np.pi *frow*x/fs) + np.sin(2 * np.pi *fcolumn*x/fs) for x in range(N)]
        freq1, freq2 = goertzemio (sine_wave,fs,N)
        if (freq1== frow or freq1== fcolumn) and (freq2== frow or freq2== fcolumn):
            print("Pass Tests: frecuencia de fila = ", frow, " frecuencia de columna = ", fcolumn," frecuencias encontradas: ", freq1, freq2 )
        else:
            print("Fail Test: frecuencia de fila = ", frow, " frecuencia de columna = ", fcolumn," frecuencias encontradas: ", freq1, freq2 )
            errors=+errors
    
if errors == 0:
    print("Test Pass")
else:
    print("Test Fail")