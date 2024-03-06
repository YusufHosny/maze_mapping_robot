from gpiozero import Device, Motor, DistanceSensor
import gpiozero.pins.pigpio as p
import time
from Libs import Gyroscope, Reading, PID_Controller

Device.pin_factory = p.PiGPIOFactory()

m1 = Motor(forward=23, backward=24, pwm=True) # left
m2 = Motor(forward=11, backward=5, pwm=True) # left
m3 = Motor(forward=15, backward=14, pwm=True) # right
m4 = Motor(forward=17, backward=27, pwm=True) # right


# adjust ratios for each motor
target_spd = 0.5
dt = 0.01
gyro = Gyroscope()

def easing(t): # t is normalized time from 0 to 1
    return 1 - 0.3 * t**3

def angle_between(alpha, beta):
    angle = beta - alpha
    angle += -360 if (angle>180) else 360 if (angle<-180) else 0
    return angle

def stp():
    m1.stop()
    m2.stop()
    m3.stop()
    m4.stop()

schmitt = "low"
angle_low = -2
angle_high = 2
def fwd(start_angle):
    global schmitt
    if angle_between(start_angle, gyro.angle) > angle_high and schmitt == "low":
        schmitt = "high"
    elif angle_between(start_angle, gyro.angle) < angle_low and schmitt == "high":
        schmitt = "low"

    ratio_up = 1.2
    ratio_down = 0.8

    if schmitt == "low":
        print("got here")
        m1.forward(target_spd*ratio_up)
        m2.forward(target_spd*ratio_up)
        m3.forward(target_spd*ratio_down)
        m4.forward(target_spd*ratio_down)
    elif schmitt == "high":
        m1.forward(target_spd)
        m2.forward(target_spd)
        m3.forward(target_spd)
        m4.forward(target_spd)


def right():
    start_angle = gyro.angle
    dtheta = abs(angle_between(gyro.angle, start_angle))
    while dtheta < 87:
        spdleft = target_spd * -easing(min(max(0, dtheta), 90)/90)
        spdright = target_spd * easing(min(max(0, dtheta), 90)/90)

        # drive all 4 motors
        if spdleft < 0:
            m3.backward(-spdleft)
            m4.backward(-spdleft)
        else:
            m3.forward(spdleft)
            m4.forward(spdleft)

        if spdright < 0:
            m1.backward(-spdright)
            m2.backward(-spdright)
        else:
            m1.forward(spdright)
            m2.forward(spdright)


        time.sleep(dt)
        dtheta = abs(angle_between(gyro.angle, start_angle))

    stp()
    print(gyro.angle)


def left():
    start_angle = gyro.angle
    dtheta = abs(angle_between(gyro.angle, start_angle))
    while dtheta < 87:
        spdleft = target_spd * easing(min(max(0, dtheta), 90)/90)
        spdright = target_spd * -easing(min(max(0, dtheta), 90)/90)

        # drive all 4 motors
        if spdleft < 0:
            m3.backward(-spdleft)
            m4.backward(-spdleft)
        else:
            m3.forward(spdleft)
            m4.forward(spdleft)

        if spdright < 0:
            m1.backward(-spdright)
            m2.backward(-spdright)
        else:
            m1.forward(spdright)
            m2.forward(spdright)


        time.sleep(dt)
        dtheta = abs(angle_between(gyro.angle, start_angle))

    stp()
    print(gyro.angle)


u1 = DistanceSensor(echo=6, trigger=13) # front (opposite to power bank cable)
u2 = DistanceSensor(echo=19, trigger=26) # left
u3 = DistanceSensor(echo=25, trigger=8) # back
u4 = DistanceSensor(echo=16, trigger=20) # right

u = (u1, u2, u3, u4)

def get_denoise(ix):
    iterations = 10
    dt = 0.01

    avg = 0
    values = []

    for i in range(iterations):
        values += [u[ix-1].distance]
        time.sleep(dt)

    avg = sum(values)/iterations

    max_deviation = 0.05
    for value in values:
        if abs(value - avg) > max_deviation:
             values.remove(value)

    avg = sum(values)/iterations

    return avg


from mapper import Mapper

m = Mapper()
grid_length = 0.2
def ca():

    s1 = get_denoise(1) > grid_length
    s2 = get_denoise(2) > grid_length
    s3 = get_denoise(3) > grid_length
    s4 = get_denoise(4) > grid_length

    return (s1, False, s2, s4)

m.check_around = ca

from maze_graph import Directions


def mv(dir):
    start_angle = gyro.angle
    if dir == Directions.UP:
        start = u1.distance
        while (start - get_denoise(1)) < grid_length:
            fwd(start_angle)
        stp()
    elif dir == Directions.DOWN:
        left()
        left()
        start = u1.distance
        while (start - get_denoise(1)) < grid_length:
            fwd(start_angle)
        stp()
    elif dir == Directions.LEFT:
        left()
        start = u1.distance
        while (start - get_denoise(1)) < grid_length:
            fwd(start_angle)
        stp()
    elif dir == Directions.RIGHT:
        right()
        start = get_denoise(1)
        while (start - get_denoise(1)) < grid_length:
            fwd(start_angle)
        stp()

m.mv = mv

# while True:
#     print("front", get_denoise(1))
#     print("left", get_denoise(2))
#     print("back", get_denoise(3))
#     print("right", get_denoise(4))

m.map()

# s = gyro.angle
# while get_denoise(1) > 0.1:
#     fwd(s)
#     print(gyro.angle)
# stp()