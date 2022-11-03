import wave
import struct
import numpy as np
from playsound import playsound

def selectone(number):
    if number == '1': 
        frow = 697
        fcolumn = 1209
    elif number == '2':
        frow = 697
        fcolumn = 1336
    elif number == '3':
        frow = 697 
        fcolumn = 1477
    elif number == 'A':
        row = 697 
        fcolumn = 1633
    elif number == '4': 
        frow = 770
        fcolumn = 1209
    elif number == '5':
        frow = 770
        fcolumn = 1336
    elif number == '6':
        frow = 770 
        fcolumn = 1477
    elif number == 'B':
        row = 770 
        fcolumn = 1633
    elif number == '7': 
        frow = 852
        fcolumn = 1209
    elif number == '8':
        frow = 852
        fcolumn = 1336
    elif number == '9':
        frow = 852
        fcolumn = 1477
    elif number == 'C':
        row = 852
        fcolumn = 1633
    elif number == '*': 
        frow = 941
        fcolumn = 1209
    elif number == '0':
        frow = 941
        fcolumn = 1336
    elif number == '#':
        frow = 941
        fcolumn = 1477
    else:
        frow = 941 
        fcolumn = 1633
    return frow, fcolumn

def playtone(number):
    frow,fcolumn = selectone(number)
    # La frecuencia de muestreo es la conversión analógica-digital
    sampling_rate = 8000
    # Número de muestras
    num_samples = int(sampling_rate)*3
    # Amplitud de la onda 
    amplitud = 16000
    # Nombre del archivo a generar
    file = "tone.wav"
    # Generación de la señal
    sine_wave = [np.sin(2 * np.pi *frow*x/sampling_rate) + np.sin(2 * np.pi *fcolumn*x/sampling_rate) for x in range(num_samples)]
    # PARÁMETROS PARA GENERAR EL ARCHIVO DE AUDIO
    # Número de muestras
    nframes=num_samples
    # Tipo de compresión
    comptype="NONE"
    compname="not compressed"
    # Número de canales
    nchannels=1
    # ancho del muestreo en bytes
    sampwidth=2
    # Abrir el archivo para su creación y escritura
    wav_file=wave.open(file, 'w')
    # Colocar los parámetros del archivo de audio WAV
    wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
    # Se abre el archivo y se colocan los parámetros
    # struct es una librería de Python que empaqueta los datos como binarios
    # el parámetro 'h' significa que es a 16 bits
    for s in sine_wave:
        wav_file.writeframes(struct.pack('h', int(s*amplitud)))
    wav_file.close()
    playsound("tone.wav")
   

number = input('Digite numero: ')
playtone(number)
