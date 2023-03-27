

sys.path.append('../../../')
from components.vehicle import Vehicle

_MOVE_TIMER = 0.2

def drive_motor:
      self.vehicle.move_forward()
      time.sleep(_MOVE_TIMER)
      self.vehicle.stop()


if __name__ == "__main__":
    drive_motor()
