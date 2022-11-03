from pickle import TRUE
import speech_recognition as sr
from playsound import playsound 

r = sr.Recognizer()
with sr.Microphone() as device:
    #while TRUE:
    print("Dime algo")
    audio = r.listen(device)
    try:
        with open("audio.wav","wb") as fichero:
            fichero.write(audio.get_wav_data())
    except: 
        print("Lo siento no te entendi")
        
playsound('audio.wav')