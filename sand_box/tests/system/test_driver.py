import sys
import signal
import time

sys.path.append('../../../')
from system.driver import Driver
from components.gpio_worker import GPIO_Worker

_MOVE_TIMER = 1

gpio = GPIO_Worker()
driver = Driver()

def signal_handler(_SIGNO, _STACK_FRAME):
    gpio.clean_up()
    sys.exit(0)

def drive_motor():
      driver.auto_drive_start();


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    drive_motor()