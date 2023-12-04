from gpiozero import Device, DistanceSensor, Motor
import gpiozero.pins.pigpio as p
import time
import math

Device.pin_factory = p.PiGPIOFactory()

s1 = DistanceSensor(echo=5, trigger=11) # front
s2 = DistanceSensor(echo=17, trigger=27) # left
s3 = DistanceSensor(echo=13, trigger=6) # right
s4 = DistanceSensor(echo=19, trigger=26) # back

m1 = Motor(forward=14, backward=15, pwm=True) # front left
m2 = Motor(forward=23, backward=24, pwm=True) # front right
m3 = Motor(forward=25, backward=8, pwm=True) # back left
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



# correction function
correction_step = 0.1
def correct(dir):
    print("correcting to ", dir)

    if dir == 'right':
        # we moved too far right
        right(spd + correction_step)
        cur_left = s2.distance
        cur_right = s3.distance
        while(cur_left > cur_right):
            cur_left = s2.distance
            cur_right = s3.distance
        
        right(spd)
    elif dir == 'left':
        # we moved too far left
        left(spd + correction_step)
        cur_left = s2.distance
        cur_right = s3.distance
        while(cur_left < cur_right):
            cur_left = s2.distance
            cur_right = s3.distance
        
        left(spd)
    
    print("corrected")
        



dt = 0.01 # 10ms update interval
threshold = 5 # 5 cm threshold, honestly no idea what would be best

# store initial left and right distances
init_left = s2.distance
init_right = s3.distance


# main loop
while True:
    # wait time between updates
    time.sleep(dt)

    # move with defined speed
    right(spd)
    left(spd)

    # get distances
    cur_left = s2.distance
    cur_right = s3.distance

    # get left and right deviations
    d_left = cur_left - init_left
    d_right = cur_right - init_right

    if math.abs(d_left) > threshold or math.abs(d_right) >= threshold:
        # both exceeded threshold
        if cur_left > cur_right:
            correct('right') # correct since we moved too far right
        else:
            correct('left') # correct since we moved too far left




    # TODO try this code too, allows for paths to appear supposedly    
    # if math.abs(d_left) > threshold:
    #     if math.abs(d_right) > 0.6*threshold:
    #         if cur_left > cur_right:
    #             correct('right') # correct since we moved too far right
    #         else:
    #             correct('left') # correct since we moved too far left
    #     else:
    #         # left changed, but right didnt, path appeared on left
    #         init_left = cur_left
    #     
    # elif math.abs(d_right) > threshold:
    #     if math.abs(d_right) < 0.6*threshold:
    #         if cur_left > cur_right:
    #             correct('right') # correct since we moved too far right
    #         else:
    #             correct('left') # correct since we moved too far left
    #     else:
    #         # right changed, but left didnt, path appeared on right
    #         init_right = cur_right