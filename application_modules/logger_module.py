##################################################
# AUTHOR                                         #
# SABARISH VIJAYAKUMAR                           #
##################################################
import logging

class Logger_Module:
    
    _def_log_config = {
        "DEBUG":logging.DEBUG,
        "INFO":logging.INFO,
        "WARNING":logging.WARNING,
        "ERROR":logging.ERROR,
        "CRITICAL":logging.CRITICAL       
        }
    
    def configure(self, filePath, inputLogLevel):
        loggerLevel = self._def_log_config[(inputLogLevel.upper())]
        loggerFormat = "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s";
        logging.basicConfig(filename=filePath, level=loggerLevel, format=loggerFormat, filemode='w')
        
    def logDebug(self, message):
        logging.debug(message)
        
    def logInfo(self, message):
        logging.info(message);
        
    def logWarning(self, message):
        logging.warning(message);
        
    def logError(self, message):
        logging.error(message);
    
    def logCritical(self, message):
        logging.critical(message);
        
    def logDebug(self, message):
        logging.debug(message);
    