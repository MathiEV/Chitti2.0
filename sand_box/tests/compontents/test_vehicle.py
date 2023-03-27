import sys
import signal
import time

sys.path.append('../../../')
from components.gpio_worker import GPIO_Worker
from components.vehicle import Vehicle

_MOVE_TIMER = 1

gpio = GPIO_Worker()

def signal_handler(_SIGNO, _STACK_FRAME):
    logger.logDebug("Signal Received : Exiting...")
    gpio.clean_up()
    sys.exit(0)

def drive_motor():
      vehicle = Vehicle()
      vehicle.move_forward()
      time.sleep(_MOVE_TIMER)
      vehicle.stop()
      #time.sleep(_MOVE_TIMER)
      #vehicle.move_right()
      #time.sleep(_MOVE_TIMER)
      #vehicle.stop()
      #time.sleep(_MOVE_TIMER)
      #vehicle.move_left()
      #time.sleep(_MOVE_TIMER)
      #vehicle.stop()
      #time.sleep(_MOVE_TIMER)
      #vehicle.move_backward()
      #time.sleep(_MOVE_TIMER)
      #vehicle.stop()
      #time.sleep(_MOVE_TIMER)


if __name__ == "__main__":
    gpio.clean_up()
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    drive_motor()
    gpio.clean_up()
