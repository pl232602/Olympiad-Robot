from serialcontroller import motor_controller
import time
import sys

##Use a string for motor values, not an int

##since daemon threading is used, time wait must be used to keep motor program running
if __name__ == "__main__":
    motor_controller(None,"straight",500)
    time.sleep(6)
