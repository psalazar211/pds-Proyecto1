from pickle import TRUE
import speech_recognition as sr
from playsound import playsound 
import scipy.io.wavfile as waves
from goertzel import goertzemio

def listen(): 
    r = sr.Recognizer()
    filename = "audio.wav"
    with sr.Microphone() as device:
        #while TRUE:
        print("Escuchando")
        audio = r.listen(device)
    try:
        with open(filename,"wb") as fichero:
            fichero.write(audio.get_wav_data())
        return (filename)
    except: 
        print("Vuelva a marcar el digito")
        listen()
        
def get_tone():
    audiofile = listen()
    Fs, sonido = waves.read(audiofile)
    N = len(sonido)
    frow, fcolumn = goertzemio (sonido,Fs,N)
    if frow == 697 and fcolumn == 1209:
        number = '1'
        return number
    elif frow == 697 and fcolumn == 1336:
        number ='2'
        return number
    elif frow == 697 and fcolumn == 1477:
        number = '3'
        return number
    elif frow == 697 and fcolumn == 1633:
        number = 'A'
        return number
    elif frow == 770 and fcolumn == 1209:
        number = '4'
        return number
    elif frow == 770 and fcolumn == 1336:
        number = '5'
        return number
    elif frow == 770 and fcolumn == 1477:
        number = '6'
        return number
    elif frow == 770 and fcolumn == 1633:
        number = 'B'
        return number
    elif frow == 852 and fcolumn == 1209:
        number = '7'
        return number
    elif frow == 852 and fcolumn == 1336:
        number = '8'
        return number
    elif frow == 852 and fcolumn == 1477:
        number = '9'
        return number
    elif frow == 852 and fcolumn ==1633:
        number = 'C'
        return number
    elif frow == 941 and fcolumn == 1209:
        number = '*'
        return number
    elif frow == 941 and fcolumn == 1336:
        number = '0'
        return number
    elif frow == 941 and fcolumn == 1477:
        number = '#'
        return number
    elif frow == 941 and fcolumn == 1633:
        number = '.'
        return number
    else:
        print("Dgite nuevemente el numero: ")
        number= get_tone()
        return number

    
    

number = get_tone()
print(number)