from serialcontroller import motor_controller
import multiprocessing as mp
import serialcontroller
import time

##Use a string for motor values, not an int

if __name__ == "__main__":
    while True:
        motor_controller("050","straight")
        time.sleep(1)
        motor_controller("-50","straight")
        time.sleep(1)
