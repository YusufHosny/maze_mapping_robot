
from gpiozero import Device, DistanceSensor, Motor
import gpiozero.pins.pigpio as p
import time
import math

Device.pin_factory = p.PiGPIOFactory()

s1 = DistanceSensor(echo=6, trigger=13)
s2 = DistanceSensor(echo=25, trigger=8)
s3 = DistanceSensor(echo=19, trigger=26)
s4 = DistanceSensor(echo=16, trigger=20)

m1 = Motor(forward=27, backward=17, pwm=True)
m2 = Motor(forward=15, backward=14, pwm=True)
m3 = Motor(forward=5, backward=11, pwm=True)
m4 = Motor(forward=16, backward=20, pwm=True)

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


# get distances
cur_left = s2.distance * 100
cur_right = s3.distance * 100

# get initial distances to use as reference
reference_distance = cur_left - cur_right

from PID_control import PID_Controller
controller = PID_Controller(0.6, 1, 0.2, reference_distance, lims=(-0.3, 0.3))

dt = 0.01 # 10ms update interval

# main loop
while True:
    # wait time between updates
    time.sleep(dt)

    # get distances
    cur_left = s2.distance * 100
    cur_right = s3.distance * 100

    # distance difference
    d_distance = cur_left - cur_right

    # step controller to get manipulated variable
    mv = controller(round(d_distance))

    # print mv to check behavior for tuning
    print(mv)

    # move based on controller output
    right(spd - mv/2)
    left(spd + mv/2)

