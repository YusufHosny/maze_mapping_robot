from gpiozero import Device, DistanceSensor, Motor
import gpiozero.pins.pigpio as p
import time
import math

Device.pin_factory = p.PiGPIOFactory()

s1 = DistanceSensor(echo=6, trigger=13) # front
s2 = DistanceSensor(echo=25, trigger=8) # left
s3 = DistanceSensor(echo=19, trigger=26) # right
s4 = DistanceSensor(echo=16, trigger=20) # back

m1 = Motor(forward=27, backward=17, pwm=True) # front left
m2 = Motor(forward=15, backward=14, pwm=True) # front right
m3 = Motor(forward=5, backward=11, pwm=True) # back left
m4 = Motor(forward=16, backward=20, pwm=True) # back right


# movement speed
spd = 0.5

# motor specific ratios
rat12 = 1
rat13 = 1
rat14 = 1

# move right motors at certain speed, negative speeds indicate backwards
def right(target_spd):
    if target_spd > 0:
        m2.forward(target_spd * rat12)
        m4.forward(target_spd * rat14)
    else:
        m2.backward(target_spd * rat12)
        m4.backward(target_spd * rat14)

# move left motors at certain speed, negative speeds indicate backwards
def left(target_spd): 
    if target_spd > 0:
        m1.forward(target_spd)
        m3.forward(target_spd * rat13)
    else:
        m1.backward(target_spd)
        m3.backward(target_spd * rat13)


dt = 0.01 # 10ms update interval

# main loop
while True:
    # wait time between updates
    time.sleep(dt)

    # rotate left
    right(spd)
    left(-spd)