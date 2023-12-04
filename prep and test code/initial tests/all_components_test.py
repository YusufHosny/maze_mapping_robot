from gpiozero import Device
from gpiozero import DistanceSensor, Motor
import gpiozero.pins.pigpio as p
import time

Device.pin_factory = p.PiGPIOFactory()

s1 = DistanceSensor(echo=6, trigger=13)
s2 = DistanceSensor(echo=25, trigger=8)
s3 = DistanceSensor(echo=19, trigger=26)
s4 = DistanceSensor(echo=16, trigger=20)

m1 = Motor(forward=27, backward=17, pwm=True)
m2 = Motor(forward=15, backward=14, pwm=True)
m3 = Motor(forward=5, backward=11, pwm=True)
m4 = Motor(forward=16, backward=20, pwm=True)




while True:
    time.sleep(0.01)
    d = s1.distance
    if d > 0.2:
        m1.forward(0.2)
    else:
        m1.backward(0.8)

    d = s2.distance
    if d > 0.2:
        m2.forward(0.2)
    else:
        m2.backward(0.8)

    d = s3.distance
    if d > 0.2:
        m3.forward(0.2)
    else:
        m3.backward(0.8)

    d = s4.distance
    if d > 0.2:
        m4.forward(0.2)
    else:
        m4.backward(0.8)
