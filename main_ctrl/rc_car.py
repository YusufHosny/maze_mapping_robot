from time import sleep
import api_manager as api
from robot import robot_controller


# INITIALIZATION
r = robot_controller(0.5, 0.01, 2, 0.2)

# MAIN LOOP
while True:
    # start API polling function, polls and returns when new rc request is received
    rq = api.rc_get()

    if rq == "forward":
        r.advance(r.gyro.angle)
    elif rq == "left":
        r.left_continuous()
    elif rq == "right":
        r.right_continuous()
    elif rq == "stop":
        r.stop()

    # update instruction as complete on API
    api.rc_set()

    # sleep between checks to allow API error tolerace
    sleep(0.3)
    
