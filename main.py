# -*- coding: utf-8 -*-
"""
@Author: Mathiyazhagan Ramaniselva
@Date: 26.03.2023
"""
import signal
import threading
import sys
import os
from datetime import datetime

from system.mode_monitor import Mode_Monitor
from system.alert_manager import Alert_Manager
from system.face_recognizer import Face_Recognizer
from system.driver import Driver
from system.entertainer import Entertainer
from system.telegram_module import start_telegram_service
from system.communication_manager import __communication_manager_init__ 

from components.gpio_worker import GPIO_Worker

from application_modules.logger_module import Logger_Module
from application_modules.path_module import Path_Module

logger = Logger_Module()

def signal_handler(_SIGNO, _STACK_FRAME):
    logger.logDebug("Signal Received : Exiting...")
    sys.exit(0)
    
def _constructLogFilePath():
    path_module=Path_Module()
    logFileDirectory = os.path.join(path_module.getUserHomeDirectory(), "Chitti2.0", "app","log")
    if not os.path.exists(logFileDirectory):
        os.makedirs(logFileDirectory)
    logFilePath = os.path.join(logFileDirectory, "robot_log" + str(datetime.now()) + ".log")
    return logFilePath

def configureLogger():
    filePath = _constructLogFilePath()
    logger.configure(filePath,"critical")
    
def configureWorkingDirectory():
    path_module=Path_Module()
    workingDir = os.getcwd()
    path_module.setSystemPath(workingDir)

def main():
    configureWorkingDirectory()
    configureLogger()

    gpio_worker = GPIO_Worker()
    mode_monitor = Mode_Monitor()
    alert_manager = Alert_Manager(gpio_worker, mode_monitor.update_mode)
    face_recognizer = Face_Recognizer(mode_monitor, alert_manager)
    driver = Driver(mode_monitor)
    entertainer = Entertainer(mode_monitor, gpio_worker)

    __communication_manager_init__(mode_monitor, alert_manager, driver, entertainer)

    threading.Thread(target=start_telegram_service, daemon=True).start()

    signal.pause()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    main()
