# -*- coding: utf-8 -*-
"""
@Author: Krushna kuamr 
@Date: 26.03.2023
"""
import signal
import sys
import os
import time
sys.path.append('../../../')
from datetime import datetime
from components.face_expressions import Face_Expressions
from system.mode_monitor import Mode_Monitor
from system.alert_manager import Alert_Manager
from application_modules.logger_module import Logger_Module
from application_modules.path_module import Path_Module

logger = Logger_Module()

def signal_handler(_SIGNO, _STACK_FRAME):
    logger.logDebug("Signal Received : Exiting...")
    sys.exit(0)
    
  

def main():
	face_expression = Face_Expressions()
	time.sleep(2)
	face_expression.set_expression_smile()
	time.sleep(2)
	face_expression.set_expression_sad()
	time.sleep(2)
	face_expression.set_expression_angry()
	


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    main()
