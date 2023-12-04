from gpiozero import Device, PWMOutputDevice, Motor
import gpiozero.pins.pigpio as p
import time

Device.pin_factory = p.PiGPIOFactory()

m1 = Motor(forward=27, backward=17, pwm=True)
m2 = Motor(forward=15, backward=14, pwm=True)
m3 = Motor(forward=5, backward=11, pwm=True)
m4 = Motor(forward=16, backward=20, pwm=True)


# adjust ratios for each motor
target_spd1 = 0.5
rat12 = 1
rat13 = 1
rat14 = 1


time.sleep(2)
# drive all 4 motors
m1.forward(target_spd1) # basis motor, probably pick the slowest one
m2.forward(target_spd1 * rat12) # calibration target
m3.forward(target_spd1 * rat13)
m4.forward(target_spd1 * rat14)



    
