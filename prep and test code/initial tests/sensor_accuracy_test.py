from gpiozero import DistanceSensor
import time
u1 = DistanceSensor(echo=17, trigger=4)

while True:
    d = u1.distance
    print(d)
    time.sleep(0.1)