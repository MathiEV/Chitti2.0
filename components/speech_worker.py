##################################################
# AUTHOR                                         #
# GOPINATH RAJA                                  #
##################################################
import pyttsx3
import speech_recognition as sr

class Speech_Worker:

    _engine = pyttsx3.init()
    
    def __init__(self):
        print("Speech worker init started")
        self._engine.setProperty('rate', 150)
        self._engine.setProperty('volume', 0.9)
        voices = self._engine.getProperty('voices')
        self._engine.setProperty('voices', voices[1].id)            
        print("Speech worker init completed")
    
    def speak(self,word):
        self._engine.say(str(word))
        self._engine.runAndWait()
        self._engine.stop()
        

        
