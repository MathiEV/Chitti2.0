import sys
import signal
import time

sys.path.append('../../../')
from system.driver import Driver
from components.gpio_worker import GPIO_Worker
from system.mode_monitor import Mode_Monitor
from system.alert_manager import Alert_Manager
import common.common_definitions as comm_def

_MOVE_TIMER = 1

gpio = GPIO_Worker()
mode_monitor = Mode_Monitor()
#alert_manager = Alert_Manager(mode_monitor.update_mode)
driver = Driver(mode_monitor)

def signal_handler(_SIGNO, _STACK_FRAME):
    gpio.clean_up()
    sys.exit(0)

def drive_motor():
      driver.auto_drive_start();


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
           
    mode_monitor.update_mode(comm_def._GUEST_MODE)
    time.sleep(10)
    mode_monitor.update_mode(comm_def._FUN_MODE)
    time.sleep(5)
    mode_monitor.update_mode(comm_def._SECURITY_MODE)
    time.sleep(2)
    mode_monitor.update_mode(comm_def._FUN_MODE)
    time.sleep(5)
    
    #drive_motor()
motor()
