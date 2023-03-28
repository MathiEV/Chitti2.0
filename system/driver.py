import threading
import time
import common.common_definitions as comm_def
from components.vehicle import Vehicle
from components.ultrasonic_handler import Ultrasonic_Handler
from application_modules.logger_module import Logger_Module
import queue

_ULTRASONIC_THRESHOLD_DIST = 50 #distance in cms
_MOVE_TIMER = 0.2 # in seconds

class Driver:
    
    _flag = True
    _logger = Logger_Module()
    def __init__(self, mode_monitor):
        print("Driver Init Started")
        self.__mode_monitor = mode_monitor
        #self.__alert_manager = alert_manager      
        self.ultrasonic_handler = Ultrasonic_Handler()
        self.vehicle = Vehicle()
        self.__Manual_com_queue = queue.Queue()              
        self.__mode = self.__mode_monitor.get_mode()
        self.__mode_monitor.register_mode_monitor_callback(self.mode_callback1)       
        threading.Thread(target=self.__drive_thread, daemon=True).start()
        print("Driver init exit")
            
    def mode_callback1(self, mode):
        self.__mode = mode
        print("mode callback executed",self.__mode)    
    
    def com_callback(self, direction):
        self.__Manual_com_queue.put(direction)    
    
    def __drive_thread(self):
        print("Drive Thread Started")
        #self._logger.logInfo("Drive Thread Started")
        print("mode=",self.__mode)
        while True:
            if self.__mode == comm_def._GUEST_MODE:
                self.auto_drive_start()
                print("entered guest mode")
            elif self.__mode == comm_def._SECURITY_MODE:
                self.auto_drive_start()
                print("security mode")
            elif self.__mode == comm_def._MANUAL_MODE:
                if self.__Manual_com_queue.empty() != True:
                   direction = self.__Manual_com_queue.get()
                   self.__manual_mode(direction)
                print("Manual mode")
            elif self.__mode == comm_def._FUN_MODE:
                print("entered fun mode")
                self.vehicle.stop()
                time.sleep(0.2)#Delay added to avoid thread crash
            else:
                self._logger.logInfo("No Valid Mode set")
                print("no valid mode set")
                self.vehicle.stop()
                time.sleep(0.2)#Delay added to avoid thread crash                
    
    def auto_drive_start(self):
        #while (self._flag) :
        object_distance = self.ultrasonic_handler.check_for_obstacles()
        if ((object_distance[1] <= _ULTRASONIC_THRESHOLD_DIST) and  object_distance[1] > 0):
            self.vehicle.stop()
            self.__decide_direction(object_distance)
        else :
            self.vehicle.move_forward()
            time.sleep(_MOVE_TIMER)
            #self.vehicle.stop()
    
    def auto_drive_stop(self):
        self._flag = False
        self.vehicle.stop()
    
    def __decide_direction(self, object_distance):
        if ((object_distance[0] <= _ULTRASONIC_THRESHOLD_DIST and  object_distance[0] > 0) 
            and (object_distance[2] <= _ULTRASONIC_THRESHOLD_DIST and  object_distance[2] > 0)):
            self.vehicle.move_left()
            time.sleep(1)
            #self.vehicle.stop()
        elif ((object_distance[0] <= object_distance[2]) or object_distance[2] == 0):
            self.vehicle.move_left()
            time.sleep(_MOVE_TIMER)
            #self.vehicle.stop()
        else:
            self.vehicle.move_right()
            time.sleep(_MOVE_TIMER)
            #self.vehicle.stop()
            
            
    def __manual_mode(self,direction):
        if direction == comm_def._CONTROL_LEFT:
            self.manual_drive_left()
        elif direction == comm_def._CONTROL_RIGHT:
            self.manual_drive_right()   
        elif direction == comm_def._CONTROL_FORWORD:
            self.manual_drive_forward()
        elif direction == comm_def._CONTROL_BACKWORD:
            self.manual_drive_backward()
        
        
            
    def manual_drive_forward(self):
        object_distance = self.ultrasonic_handler.check_for_obstacles()
        if (object_distance[1] <= _ULTRASONIC_THRESHOLD_DIST):
            self.vehicle.stop()
            return "Cant move further as we have obstrucle"
        else:
            self.vehicle.move_forward()
    
    def manual_drive_backward(self):
        self.vehicle.move_backward()
        time.sleep(_MOVE_TIMER)
        self.vehicle.stop()
    
    def manual_drive_left(self):
        self.vehicle.move_left()
            
    def manual_drive_right(self):
        self.vehicle.move_right()
