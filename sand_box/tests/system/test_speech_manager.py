##################################################
# AUTHOR                                         #
# GOPINATH RAJA                                  #
##################################################
import sys
import time
import speech_recognition as sr

sys.path.append('../../../')
from system.speech_manager import Speech_Manager
from components.speech_worker import Speech_Worker

def validateSpeech():
    speechworker=Speech_Worker()
    speech=Speech_Manager(speechworker)
    speech.wish_me()
    speech.txt_to_speak("Signing off")
    
if __name__ == "__main__":
    validateSpeech()
