# Pip install SpeechRecognition -> pra intalar a biblioteca que vai reconhecer o audio e converte em texto
# pip install pyaudio ->  vai fazer a captura de audio do seu microfone


import speech_recognition as sr

import os

def listening_microphone():
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microphone.listen(source)
   
    try:
        phrase = microphone.recognize_google(audio, language='pt-BR') 

        if "navegador" in phrase:
            os.system("start firefox.exe")

        print("Você disse: "+ phrase)
        return phrase
    except sr.UnknownValueError:  
        print("Não entendi o que você falou, poderia falar de novo")
        return None

listening_microphone()