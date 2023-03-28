##################################################
# AUTHOR                                         #
# GOPINATH RAJA                                  #
##################################################
import sys
import speech_recognition as sr

sys.path.append('../../../')
from components.speech_worker import Speech_Worker

import datetime
import time

def controlSpeech():
    speech=Speech_Worker()
    while True:
            speech.speak('Hey this is CHITTI 2 point O, what can I do for you')
            time.sleep(2)
            speech.speak('I am your personal Assistant Chitti 2 point O. I am programmed to minor tasks like'',predict time,saying wishes''palying songs and so on!')
            time.sleep(2)
            speech.speak("I was built by My Team Golden Crow")
            time.sleep(2)
            speech.speak('Good bye')
            time.sleep(2)
            speech.speak('Thirudan Thirudan')

if __name__ == "__main__":
    controlSpeech()
