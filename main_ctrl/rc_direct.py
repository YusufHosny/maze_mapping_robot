import time
from robot import robot_controller

# INITIALIZATION
r = robot_controller(0.5, 0.01, 2, 0.2)

# MAIN LOOP
while (v := input()) != 'q':
    if v == 'w':
        r.advance(r.gyro.angle)
    elif v == 'a':
        r.left_continuous()
    elif v == 'd':
        r.right_continuous()
    elif v == 's':
        r.reverse(r.gyro.angle)

    time.sleep(0.3)
    r.stop()

