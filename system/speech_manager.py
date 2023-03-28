##################################################
# AUTHOR                                         #
# GOPINATH RAJA                                  #
##################################################

import datetime
import sys
sys.path.append('../../../')
from components.speech_worker import Speech_Worker
from components.speech_recognization_worker import Speech_Recognization_Worker

class Speech_Manager:
        
    def __init__(self, speechWorker):
        self.speechWorker=speechWorker
    
    def wish_me(self):
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<12:
            self.speechWorker.speak("Hello,Good Morning")
        elif hour>=12 and hour<18:
            self.speechWorker.speak("Hello,Good Afternoon")
        elif hour>=18 and hour<24:
            self.speechWorker.speak("Hello,Good Evening")
        else:
            self.speechWorker.speak("Hello,Good Night")
    
    def txt_to_speak(self, text):
        self.speechWorker.speak(text)
