from typing import Tuple, List
from gpiozero import Device, Motor, DistanceSensor
import gpiozero.pins.pigpio as p
import time
from Libs import Gyroscope, Schmitt_Trigger, HIGH, LOW
from maze_graph import Directions

# easing (smoothing) function to smooth out robot movement so that it slows down as it reaches the desired angle/location
def easing(t: float) -> float: # t is normalized time from 0 to 1
    return 1 - 0.3 * t**3

# get smallest angle between 2 angles
def angle_between(alpha: int, beta: int) -> int:
    angle = beta - alpha
    angle += -360 if (angle>180) else 360 if (angle<-180) else 0
    return angle

def get_denoise(u: Tuple[DistanceSensor,DistanceSensor,DistanceSensor,DistanceSensor], ix: int) -> float:
    ITERATIONS = 10
    DT = 0.01
    avg = 0
    values = []

    for i in range(ITERATIONS):
        values += [u[ix-1].distance]
        time.sleep(DT)

    avg = sum(values)/ITERATIONS

    max_deviation = 0.05
    for value in values:
        if abs(value - avg) > max_deviation:
            values.remove(value)

    avg = sum(values)/ITERATIONS

    return avg


class robot_controller:
    def __init__(self, target_spd: float, update_interval: float, max_angular_noise: float, grid_length: float) -> None:
        Device.pin_factory = p.PiGPIOFactory()

        self.target_spd = target_spd
        self.dt = update_interval
        self.angle_low = -max_angular_noise
        self.angle_high = max_angular_noise
        self.grid_length = grid_length
        self.schmitt = Schmitt_Trigger(self.angle_low, self.angle_high)

        self.gyro = Gyroscope()

        self.m1 = Motor(forward=23, backward=24, pwm=True) # left
        self.m2 = Motor(forward=11, backward=5, pwm=True) # left
        self.m3 = Motor(forward=15, backward=14, pwm=True) # right
        self.m4 = Motor(forward=17, backward=27, pwm=True) # right

        self.facing = Directions.UP

        u1 = DistanceSensor(echo=6, trigger=13) # front (opposite to power bank cable)
        u2 = DistanceSensor(echo=19, trigger=26) # left
        # u3 = DistanceSensor(echo=25, trigger=8) # back
        u4 = DistanceSensor(echo=16, trigger=20) # right

        self.u = (u1, u2, None, u4)

        self.stop()

    def stop(self) -> None:
        self.m1.stop()
        self.m2.stop()
        self.m3.stop()
        self.m4.stop()



    # moves robot forward
    def advance(self, start_angle: int) -> None:

        self.schmitt(angle_between(start_angle, self.gyro.angle))

        # how much to speed up/slow down motors when the robot moves too far left
        # decided experimentally based on how strong left side is vs right side
        ratio_up = 1.2
        ratio_down = 0.8

        if self.schmitt.state == LOW:
            self.m1.forward(self.target_spd*ratio_up)
            self.m2.forward(self.target_spd*ratio_up)
            self.m3.forward(self.target_spd*ratio_down)
            self.m4.forward(self.target_spd*ratio_down)
        elif self.schmitt.state == HIGH:
            self.m1.forward(self.target_spd)
            self.m2.forward(self.target_spd)
            self.m3.forward(self.target_spd)
            self.m4.forward(self.target_spd)


    def advance(self, start_angle: int) -> None:

        self.schmitt(angle_between(start_angle, self.gyro.angle))

        # how much to speed up/slow down motors when the robot moves too far left
        # decided experimentally based on how strong left side is vs right side
        ratio_up = 1.2
        ratio_down = 0.8

        if self.schmitt.state == LOW:
            self.m1.backward(self.target_spd*ratio_up)
            self.m2.backward(self.target_spd*ratio_up)
            self.m3.backward(self.target_spd*ratio_down)
            self.m4.backward(self.target_spd*ratio_down)
        elif self.schmitt.state == HIGH:
            self.m1.backward(self.target_spd)
            self.m2.backward(self.target_spd)
            self.m3.backward(self.target_spd)
            self.m4.backward(self.target_spd)

    # right 90 degrees
    def right(self) -> None:
        start_angle = self.gyro.angle
        dtheta = abs(angle_between(self.gyro.angle, start_angle))
        while dtheta < 92:
            spdleft = self.target_spd * -easing(min(max(0, dtheta), 90)/90)
            spdright = self.target_spd * easing(min(max(0, dtheta), 90)/90)

            # drive all 4 motors
            if spdleft < 0:
                self.m3.backward(-spdleft)
                self.m4.backward(-spdleft)
            else:
                self.m3.forward(spdleft)
                self.m4.forward(spdleft)

            if spdright < 0:
                self.m1.backward(-spdright)
                self.m2.backward(-spdright)
            else:
                self.m1.forward(spdright)
                self.m2.forward(spdright)


            time.sleep(self.dt)
            dtheta = abs(angle_between(self.gyro.angle, start_angle))

        self.stop()

    # left 90 degrees
    def left(self) -> None:
        start_angle = self.gyro.angle
        dtheta = abs(angle_between(self.gyro.angle, start_angle))
        while dtheta < 85:
            spdleft = self.target_spd * easing(min(max(0, dtheta), 90)/90)
            spdright = self.target_spd * -easing(min(max(0, dtheta), 90)/90)

            # drive all 4 motors
            if spdleft < 0:
                self.m3.backward(-spdleft)
                self.m4.backward(-spdleft)
            else:
                self.m3.forward(spdleft)
                self.m4.forward(spdleft)

            if spdright < 0:
                self.m1.backward(-spdright)
                self.m2.backward(-spdright)
            else:
                self.m1.forward(spdright)
                self.m2.forward(spdright)


            time.sleep(self.dt)
            dtheta = abs(angle_between(self.gyro.angle, start_angle))

        self.stop()

    def right_angle(self, angle) -> None:
        start_angle = self.gyro.angle
        dtheta = abs(angle_between(self.gyro.angle, start_angle))
        while dtheta < 0.95*angle:
            spdleft = self.target_spd * -easing(min(max(0, dtheta), angle)/angle)
            spdright = self.target_spd * easing(min(max(0, dtheta), angle)/angle)

            # drive all 4 motors
            if spdleft < 0:
                self.m3.backward(-spdleft)
                self.m4.backward(-spdleft)
            else:
                self.m3.forward(spdleft)
                self.m4.forward(spdleft)

            if spdright < 0:
                self.m1.backward(-spdright)
                self.m2.backward(-spdright)
            else:
                self.m1.forward(spdright)
                self.m2.forward(spdright)


            time.sleep(self.dt)
            dtheta = abs(angle_between(self.gyro.angle, start_angle))

        self.stop()

    def left_angle(self, angle) -> None:
        start_angle = self.gyro.angle
        dtheta = abs(angle_between(self.gyro.angle, start_angle))
        while dtheta < 2*angle:
            spdleft = self.target_spd * easing(min(max(0, dtheta), angle)/angle)
            spdright = self.target_spd * -easing(min(max(0, dtheta), angle)/angle)

            # drive all 4 motors
            if spdleft < 0:
                self.m3.backward(-spdleft)
                self.m4.backward(-spdleft)
            else:
                self.m3.forward(spdleft)
                self.m4.forward(spdleft)

            if spdright < 0:
                self.m1.backward(-spdright)
                self.m2.backward(-spdright)
            else:
                self.m1.forward(spdright)
                self.m2.forward(spdright)


            time.sleep(self.dt)
            dtheta = abs(angle_between(self.gyro.angle, start_angle))

        self.stop()

    def left_continuous(self):
        spdleft = self.target_spd
        spdright = self.target_spd * -1

        # drive all 4 motors
        if spdleft < 0:
            self.m3.backward(-spdleft)
            self.m4.backward(-spdleft)
        else:
            self.m3.forward(spdleft)
            self.m4.forward(spdleft)

        if spdright < 0:
            self.m1.backward(-spdright)
            self.m2.backward(-spdright)
        else:
            self.m1.forward(spdright)
            self.m2.forward(spdright)

    def right_continuous(self):
        spdleft = self.target_spd * -1
        spdright = self.target_spd

        # drive all 4 motors
        if spdleft < 0:
            self.m3.backward(-spdleft)
            self.m4.backward(-spdleft)
        else:
            self.m3.forward(spdleft)
            self.m4.forward(spdleft)

        if spdright < 0:
            self.m1.backward(-spdright)
            self.m2.backward(-spdright)
        else:
            self.m1.forward(spdright)
            self.m2.forward(spdright)

    def check_sensors(self) -> Tuple[bool]:
        s1 = get_denoise(self.u, 1) > self.grid_length # front
        s2 = get_denoise(self.u, 2) > self.grid_length # left
        # s3 = get_denoise(self.u, 3) > self.grid_length # TODO fix/remove
        s4 = get_denoise(self.u, 4) > self.grid_length # right

        if self.facing == Directions.UP: results = (s1, False, s2, s4)
        elif self.facing == Directions.LEFT: results = (s4, s2, s1, False)
        elif self.facing == Directions.DOWN: results = (False, s1, s4, s2)
        elif self.facing == Directions.RIGHT: results = (s2, s4, False, s1)

        return results

    def grid_block_forward(self, start_angle):
        start = get_denoise(self.u, 1)
        while (start - get_denoise(self.u, 1)) < self.grid_length:
            self.advance(start_angle)
        self.stop()
        print(f"moved from {start} to {get_denoise(self.u, 1)}")

    def move_to(self, dir):
        # if input(f"keep going to {dir}?") == 'n': exit(0)

        start_angle = self.gyro.angle
        if dir == self.facing:
            self.grid_block_forward(start_angle)
        elif dir == Directions.opposite(self.facing):
            self.facing = Directions.opposite(self.facing)
            self.left()
            self.stop()
            time.sleep(0.25)
            self.left()
            self.grid_block_forward(start_angle)
        elif dir == Directions.left_of(self.facing):
            self.facing = Directions.left_of(self.facing)
            self.left()
            self.grid_block_forward(start_angle)
        elif dir == Directions.right_of(self.facing):
            self.facing = Directions.right_of(self.facing)
            self.right()
            self.grid_block_forward(start_angle)

    def get_angular_denoise(self, angular_range):
        ITERATIONS = 20
        vals = []

        increment = angular_range/ITERATIONS
        anchor = angular_range/2

        self.left_angle(anchor)
        time.sleep(0.1)

        for _ in range(ITERATIONS):
            self.right_angle(increment)
            vals += [get_denoise(self.u, 1)]
            time.sleep(0.05)
        avg = sum(vals)/ITERATIONS

        time.sleep(0.1)
        self.left_angle(anchor)

        max_deviation = 0.085

        for value in vals:
            if abs(value - avg) > max_deviation:
                vals.remove(value)

        avg = sum(vals)/ITERATIONS
        return avg



    ## DEBUGGING ##
    def read_sensors(self, delay) -> None:
        while True:
            print("front:", get_denoise(self.u, 1))
            print("left:", get_denoise(self.u, 2))
            # print("back:", get_denoise(self.u, 3))
            print("right:", get_denoise(self.u, 4))
            time.sleep(delay)

    def check_moves_straight(self) -> None:
        start = self.gyro.angle
        while get_denoise(self.u, 1) > 0.1:
            self.advance(start)
            print("angle:", self.gyro.angle)
        self.stop()

    def get_denoised_angular(self):
        print(self.get_angular_denoise(10))
