from gpiozero import DistanceSensor, Motor
import time
motor = Motor(forward=2, backward=3)

while True:
    motor.forward()
    time.sleep(1)
    motor.backward()
    time.sleep(1)