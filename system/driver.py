import threading
import time
from components.vehicle import Vehicle
from components.ultrasonic_handler import Ultrasonic_Handler


_ULTRASONIC_THRESHOLD_DIST = 30 #distance in cms
_MOVE_TIMER = 0.2 # in seconds

class Driver:
    
    _flag = True
    
    def __init__(self):
        self.ultrasonic_handler = Ultrasonic_Handler()
        self.vehicle = Vehicle()
        threading.Thread(target=self.auto_drive_start, daemon=True).start()
        
    def auto_drive_start(self):
        while (self._flag) :
            object_distance = self.ultrasonic_handler.check_for_obstacles()
            if (object_distance[0] <= _ULTRASONIC_THRESHOLD_DIST):
                self.vehicle.stop()
                self.__decide_direction(object_distance)
            else :
                self.vehicle.move_forward()
                time.sleep(_MOVE_TIMER)
                self.vehicle.stop()
    
    def auto_drive_stop(self):
        self._flag = False
        self.vehicle.stop()
    
    def __decide_direction(self, object_distance):
        if ((object_distance[0] <= _ULTRASONIC_THRESHOLD_DIST) and (object_distance[2] <= _ULTRASONIC_THRESHOLD_DIST)):
            self.vehicle.move_backward()
            time.sleep(_MOVE_TIMER)
            self.vehicle.stop()
        elif (object_distance[0] <= object_distance[2]):
            self.vehicle.move_right()
            time.sleep(_MOVE_TIMER)
            self.vehicle.stop()
        else:
            self.vehicle.move_left()
            time.sleep(_MOVE_TIMER)
            self.vehicle.stop()
            
    def manual_drive_forward():
        object_distance = self.ultrasonic_handler.check_for_obstacles()
        if (__center_dist <= _ULTRASONIC_THRESHOLD_DIST):
            self.vehicle.stop()
            return "Cant move further as we have obstrucle"
        else:
            self.vehicle.move_forward()
    
    def manual_drive_backward():
        self.vehicle.move_backward()
        time.sleep(_MOVE_TIMER)
        self.vehicle.stop()
    
    def manual_drive_left():
        self.vehicle.move_left()
            
    def manual_drive_right():
        self.vehicle.move_right()