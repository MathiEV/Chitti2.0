##################################################
# AUTHOR                                         #
# GOPINATH                           #
##################################################

import signal
import sys
import os
import time

sys.path.append('../../../')
from datetime import datetime
from components.fun_manager import Fun_Manager
#from fun_manager import Fun_Manager
from system.mode_monitor import Mode_Monitor
from system.alert_manager import Alert_Manager
from application_modules.logger_module import Logger_Module
from application_modules.path_module import Path_Module

def controllfunmanager():
    fun_manager=Fun_Manager()
    fun_manager.set_mouth_open()
    time.sleep(2)
    first=85
    second=75
    while True:
        print("pan"+str(first))
        print("tilt"+str(second))
        fun_manager.move_face(first,second)
        first +=5
        second +=5
        time.sleep(1)
    
    fun_manager.close_funmanager()
    time.sleep(2)

    
if __name__ == "__main__":
    controllfunmanager()
