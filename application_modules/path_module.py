##################################################
# AUTHOR                                         #
# SABARISH VIJAYAKUMAR                           #
##################################################
import sys
import os

class Path_Module:
    def setSystemPath(self, path):  
        sys.path.append(path)
    
    def getUserHomeDirectory(self):
        return os.path.expanduser( '~' )
    
    def checkPathExist(self, path):        
        os.path.exists(path)
        