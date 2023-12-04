from MPU6050 import Gyroscope, Reading

import time


gyro = Gyroscope()

while True:
    time.sleep(0.5)
    print("angle:", gyro.angle)