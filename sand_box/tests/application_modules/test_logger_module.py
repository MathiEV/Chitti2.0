import os
import sys
from datetime import datetime

sys.path.append('../../../')
from application_modules.logger_module import Logger_Module
from application_modules.path_module import Path_Module

logger = Logger_Module()
path_module=Path_Module()


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
    workingDir = os.getcwd()
    path_module.setSystemPath(workingDir)

if __name__ == "__main__":
    configureLogger()
    configureWorkingDirectory()
    logger.logCritical("Added log into file");
    