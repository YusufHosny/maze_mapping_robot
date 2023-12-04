from gpiozero import DistanceSensor, Motor
import time
ultrasonic = DistanceSensor(echo=17, trigger=4)
motor = Motor(forward=2, backward=3)
while True:
    time.sleep(0.01)
    d = ultrasonic.distance
    if d > 0.2:
        motor.forward()
    else:
        motor.stop()